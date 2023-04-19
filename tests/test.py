from inspect import getmembers

class Test:
    def __init__(self):
        self.a = 0

def get_attributes_methods(c) -> tuple:
    attributes = []
    methods = []
    members = getmembers(Test)
    for member in members:
        if not member[0].startswith("__") and not member[0].endswith("__"):
            methods.append(member[0])
    for member in members:
        if '__init__' in member:
            try:
                attributes = [a for a in member[1].__code__.co_names if a not in methods]
            except:
                pass
    attributes.sort()
    methods.sort()
    return attributes, methods

def test(c):
    attributes, methods = get_attributes_methods(c)

    output = ""
    output += c.__name__ + " :\n    attributes :"
    for att in attributes:
        output += "\n        - " + att
    if not attributes:
        output += "\n        /"
    output += "\n    methods :"
    for me in methods:
        output += "\n        - " + me
    if not methods:
        output += "\n        /"
    return output
    
print(test(Test))