
class Relation:
    def xMethod(self, name1, name2, relation):
        if relation == 'parent':
            if name2 in name1.get_parents():
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

        if relation == 'cousin':

        if relation == 'unrelated':

    def wMethod(self, name1, relation):
        #a brainstorm to help you Andrew -Jamie
        output = list()
        if relation == "half-siblings":
            return self.getHalfSiblings(name1)

        if relation == 'parent':
            parents = name1.get_parents()
            return parents

        if relation == 'sibling':
            siblings = name1.get_siblings
            return siblings

        if relation == 'ancestor':
            return self.getAncestors(name1)

        if relation == 'cousin':
            return self.getCousins(name1)

        if relation == 'unrelated':
            

    def getHalfSiblings(self, name):
        list1 = name.get_parents()[0].get_children()
        list2 = name.get_parents()[1].get_children()
        halfies = list()
        temp = list(set(list1.append(list2)))
        for a in temp:
            for b in name.get_sibling():
                if a != b:
                    halfies.append(a)
        return list(set(halfies))

    def getAncestors(self, name):
        ancestors = list()
        if(name == null):
            return null
        if(name.get_parents[0] == null || name.get_parents[1] == null):
            return null
        else:
            ancestors.append(name.get_parents[0])
            ancestors.append(name.get_parents[1])
            ancestors.extend(self.getAncestors(name.get_parents[0]))
            ancestors.extend(self.getAncestors(name.get_parents[1]))

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
