class Relation:
    def xMethod(self, name1, name2, relation):
        if relation == 'parent':
            if name1 in name2.get_parents():
                return 'yes'
            else:
                return 'no'
        if relation == 'sibling':
            if name2 in name1.get_siblings():
                return 'yes'
            else:
                return 'no'

        if relation == 'half-sibling':
            if name2 in self.getHalfSiblings(name1):
                return 'yes'
            else:
                return 'no'

        if relation == 'ancestor':
            if name2 in self.getAncestors(name1):
                return 'yes'
            else:
                return 'no'

        if relation == 'cousin':
            if self.isCousin(name1, name2) is True:
                return 'yes'
            else:
                return 'no'
        if relation == 'unrelated':
            if self.isRelated(name1, name2) is True:
                return 'no'
            else:
                return 'yes'

    def wMethod(self, name1, relation, tree):
        if relation == "half-sibling":
            hflist = list()
            for a in self.getHalfSiblings(name1):
                if a.get_name() not in hflist:
                    hflist.append(a.get_name())
            hflist.sort()
            return hflist

        if relation == 'parent':
            plist = list()
            for a in name1.get_parents():
                plist.append(a.get_name())

            plist.sort()
            return plist

        if relation == 'sibling':
            slist = []
            for a in name1.get_siblings():
                slist.append(a.get_name())

            slist.sort()
            return slist

        if relation == 'ancestor':
            alist = list()
            for a in self.getAncestors(name1):
                if a.get_name() not in alist:
                    alist.append(a.get_name())

            alist.sort()
            return alist

        if relation == 'cousin':
            clist = list()
            for a in self.getCousins(name1, tree):
                if a.get_name() not in clist:
                    clist.append(a.get_name())

            clist.sort()
            return clist
        if relation == 'unrelated':
            rlist = list()
            for a in self.getUnrelated(name1, tree):
                if a.get_name() not in rlist:
                    rlist.append(a.get_name())

            rlist.sort()
            return rlist

    def getHalfSiblings(self, name):
        temp1 = name.parents[0].get_children()
        temp2 = name.parents[1].get_children()
        list1 = []
        halfies = []
        for i in temp1:
            list1.append(i)
        for i in temp2:
            list1.append(i)
        list1 = list(set(list1))
        list1.remove(name)

        for a in list1:
            if a not in name.get_siblings():
                halfies.append(a)
        return list(set(halfies))

    def getAncestors(self, name):
        ancestors = list()
        if name is None:
            return []
        if len(name.get_parents()) == 0:
            return []
        else:
            ancestors.append(name.get_parents()[0])
            ancestors.append(name.get_parents()[1])
            ancestors.extend(self.getAncestors(name.get_parents()[0]))
            ancestors.extend(self.getAncestors(name.get_parents()[1]))

        return ancestors

    def isRelated(self, name1, name2):
        result = False
        memberAncestors = self.getAncestors(name1)
        relativeAncestors = self.getAncestors(name2)

        #check if they share common ancestor
        for person1 in memberAncestors:
            for person2 in relativeAncestors:
                if person1 == person2:
                    result = True

        #check if one is a direct ancestor
        for person in memberAncestors:
            if person == name2:
                result = True

        for person in relativeAncestors:
            if person == name1:
                result = True

        return result

    def isCousin(self, name1, name2):
        result = False
        memberAncestors = self.getAncestors(name1)
        relativeAncestors = self.getAncestors(name2)

        #check if they share common ancestor
        for person1 in memberAncestors:
            for person2 in relativeAncestors:
                if person1 == person2:
                    result = True

        #check if one is a direct ancestor
        for person in memberAncestors:
            if person == name2:
                result = False

        for person in relativeAncestors:
            if person == name1:
                result = False

        return result
    
        def getUnrelated(self, name, familyTree):
        unRelated = list()
        if name is None:
            return []
        else:
            for person1 in familyTree:
                if person1.isRelated(person1, name) == false:
                    unRelated.append(person1)

        return unRelated
