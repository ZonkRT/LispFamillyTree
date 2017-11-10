class person:
    def __init__(self, x):
        self.name = x
        self.children = list()
        self.parents = list()

    def get_name(self):
        return self.name

    def add_children(self, kid):
        self.children.append(kid)

    def get_children(self):
        return self.children

    def get_siblings(self):
        if len(self.parents) > 0:
            temp1 = self.parents[0].get_children()
            temp2 = self.parents[1].get_children()
            temp = set(temp1).intersection(set(temp2))
            temp.remove(self)
            return temp
        else:
            return []

    def add_parents(self, par):
        self.parents.append(par)

    def get_parents(self):
        return self.parents
