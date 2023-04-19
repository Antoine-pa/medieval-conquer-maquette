from engine import *
from main import Main
from inspect import *#getmembers

class Doc:
    def __init__(self):
        self.list_class = [Main, Game, Map, Menu, Tools, Button, Building, JunctionBuilding, ProductionBuilding, ResourceTransportation, Doc]
        self.not_attribut = ["__name__", "append", "__init__", "super", "time", "cst", "update_buttons"]
        self.class_not_attribut = {"Main" : ["DICT_BUILDINGS", "Info", "_map", "current_h", "current_w", "display", "init", "load_map", "pygame", "set_all_const", "set_mode", "t"]}
        for c in self.list_class:
            self.not_attribut.append(c.__name__)
        self.rendu()
    
    def get_attributes_methods_size(self, c) -> tuple:
        attributes = []
        methods = []
        size = 0
        members = getmembers(c)
        for member in members:
            if not member[0].startswith("__") and not member[0].endswith("__"):
                methods.append(member[0])
        for member in members:
            try:
                size += member[1].__code__.co_stacksize
                if '__init__' in member:
                        attributes = [a for a in member[1].__code__.co_names if (a not in methods and a not in self.not_attribut)]
            except:
                pass
        attributes.sort()
        methods.sort()
        return attributes, methods, size

    def rendu(self):
        output = ""
        for c in self.list_class:
            attributes, methods, size = self.get_attributes_methods_size(c)
            output += c.__name__ + " :\n    size : " + str(size)
            output += "\n    attributes :"
            for att in attributes:
                output += "\n        - " + att
            if not attributes:
                output += "\n        /"
            output += "\n    methods :"
            for me in methods:
                output += "\n        - " + me
            if not methods:
                output += "\n        /"
            output += "\n\n"
        with open("doc/doc_class.txt", "w") as f:
            f.write(output)