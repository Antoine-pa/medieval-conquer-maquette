from . import JunctionBuilding
import pygame
from engine import t, cst
import time
import random

class ResourceTransportation(JunctionBuilding):
    """
    interface
    """
    def __init__(self, name, size, pos, angle, lvl, life, kind, stock, layer, speed_transport, capacity_transport, t = None):
        super().__init__(name, size, pos, angle, lvl, life, kind, stock, layer, t)
        self.speed_transport = speed_transport
        self.capacity_transport = capacity_transport
        self.dir_transport = [0, 0, 0, 0] #0 = no junction, 1 = input, 2 = output
        self.last_transport = time.time()

    def transport(self, _map) -> None:
        t = time.time()
        if t - self.last_transport < self.speed_transport:
            return
        self.last_transport = t
        pos = []
        for x in range(2):
            pos.append((self.pos[0] - 1 + x * 2, self.pos[1]))
            pos.append((self.pos[0], self.pos[1] - 1 + x * 2))
        list_build = []
        for p in pos:
            b = _map.dict_pos_build[self.layer].get(p)
            if b is not None and isinstance(b, ResourceTransportation):
                list_build.append(b)
        if not list_build:
            return
        ress = {}
        for _ in range(self.capacity_transport):
            if self.stock:
                r = random.choice(list(self.stock.keys()))
                self.stock[r] -= 1
                if self.stock[r] == 0:
                    del self.stock[r]
                if r not in ress:
                    ress[r] = 0
                ress[r] += 1
        list_build = []
        list_build_transport = []
        for i in range(4):
            if self.dir_transport[i] == 2: #output
                if i == 0: coords = (self.pos[0]+1, self.pos[1])
                elif i == 1: coords = (self.pos[0], self.pos[1]-1)
                elif i == 2: coords = (self.pos[0]-1, self.pos[1])
                else: coords = (self.pos[0], self.pos[1]+1)
                list_build.append(_map.dict_pos_build[self.layer].get(coords))
            if self.dir_transport[i] == 1: #input
                if i == 0: coords = (self.pos[0]+1, self.pos[1])
                elif i == 1: coords = (self.pos[0], self.pos[1]-1)
                elif i == 2: coords = (self.pos[0]-1, self.pos[1])
                else: coords = (self.pos[0], self.pos[1]+1)
                list_build_transport.append(_map.dict_pos_build[self.layer].get(coords))
        if list_build:
            for i in range(sum(list(ress.values()))):
                b = random.choice(list_build)
                r = random.choice(list(ress.keys()))
                ress[r] -= 1
                if ress[r] == 0:
                    del ress[r]
                if r not in b.stock:
                    b.stock[r] = 0
                b.stock[r] += 1
        for b in list_build_transport:
            b.transport(_map)
        if ress and self.name == "ExitGallery":
            self.exit(_map, ress)
        if self.name == "EntranceGallery":
            b = _map.dict_pos_build[0].get(tuple(self.pos))
            if b is not None:
                for i in range(min(self.capacity_transport, sum(list(b.stock.values())))):
                    r = random.choice(list(b.stock.keys()))
                    if r not in self.stock:
                        self.stock[r] = 0
                    self.stock[r] += 1
                    b.stock[r] -= 1
                    if b.stock[r] == 0:
                        del b.stock[r]
                if b.stock:
                    print(b)
        del pos
        del ress
        del list_build
        del list_build_transport
    
    def update_links(self, _map, b_update: list) -> list:
        list_build = [b for b in self.get_build_adj([_map.dict_pos_build[self.layer]]) if (b not in b_update and b.name != "EntranceGallery")]
        for b in list_build:
            if isinstance(b, ResourceTransportation):
                if b.pos[0] <= self.pos[0] < b.pos[0] + b.size[0]:
                    if b.pos[1] < self.pos[1]: #positionnement en bas d'une autre muraille
                        self.dir_transport[1] = 2
                        b.dir_transport[3] = 1
                    elif b.pos[1] > self.pos[1]: #positionnement en haut d'une autre muraille
                        self.dir_transport[3] = 2
                        b.dir_transport[1] = 1
                elif b.pos[1] <= self.pos[1] < b.pos[1] + b.size[1]:
                    if b.pos[0] > self.pos[0]: #positionnement à gauche d'une autre muraille
                        self.dir_transport[0] = 2
                        b.dir_transport[2] = 1
                    elif b.pos[0] < self.pos[0]: #positionnement à droite d'une autre muraille
                        self.dir_transport[2] = 2
                        b.dir_transport[0] = 1
                b_update.append(self)
                if b.name != "ExitGallery":
                    b.update_links(_map, b_update)
        del list_build
        return b_update
