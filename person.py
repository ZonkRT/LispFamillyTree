class person:
    def __init__(self, x):
        self.name = x
        self.children = list()
        self.siblings = list()
        self.parents = list()

    def get_name(self):
        return self.name

    def add_children(self, kid):
        self.children.append(kid)

    def get_children(self):
        return self.children

    def add_siblings(self, sib):
        self.siblings.append(sib)

    def get_siblings(self):
        return self.siblings

    def add_parents(self, par):
        self.parents.append(par)

    def get_parents(self):
        return self.parents
