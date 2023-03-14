import json
import pygame
from functools import lru_cache
class Tools:
    def __init__(self):
        self.data = self.reload_data()
        self.cst = self.const

    def load_img(self, name, x, y):
        img = pygame.image.load(name)
        img = pygame.transform.scale(img,(x, y))
        return img

    def reload_data(self):
        with open("const.json", "r") as f:
            data = json.load(f)
        return data
        
    @lru_cache
    def const(self, name):
        r = self.data.get(name, None)
        return r
    
    def set_const(self, name, val):
        self.const.cache_clear()
        if isinstance(val, tuple):
            val = list(val)
        self.data[name] = val
        with open("const.json", "w") as f:
            f.write(json.dumps(self.data, indent=4))

t = Tools()

def cst(name):
    return t.cst(name)