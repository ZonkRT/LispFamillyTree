class Person:
    n = 100
    name = ""
    children = list()
    sibling = list()
    parents = list()

    def __init__(self, x):
        name = x

    def get_name(self):
        return self.name

    def add_children(self, kid):
        self.children.append(kid)

    def get_children(self):
        return self.children

    def add_sibling(self, sib):
        self.sibling.append(sib)

    def get_sibling(self):
        return self.sibling

    def add_parent(self, par):
        self.parent.append(par)

    def get_parent(self):
        return self.parent
