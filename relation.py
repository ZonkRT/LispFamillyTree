#All queries except for "E" go in here

class Relation:
    def xMethod(name1, name2, relation):
        if relation == 'parent':
            if name1.getPare
        if relation == 'sibling':

        if relation == 'half-sibling':

        if relation == 'ancestor':

        if relation == 'cousin':

        if relation == 'unrelated':

    def wMethod(name1, relation):
        #a brainstorm to help you Andrew -Jamie
        output = list()
        if relation == "half-siblings":
            list1 = name1.get_parents()[0].get_children()
            list2 = name1.get_parents()[1].get_children()
            halfies = list()
            temp = list(set (list1.append(list2)))
            for a in temp:
                for b in name1.get_sibling():
                    if a != b:
                        halfies.append(a)
            return list(set(halfies))

        if relation == 'parent':
            parents = name1.get_parents()
            return parents

        if relation == 'sibling':
            siblings = name1.get_siblings
            return siblings

        if relation == 'ancestor':
            return getAncestors(name1)

        if relation == 'cousin':


        if relation == 'unrelated':

    def getAncestors(name):
        ancestors = list()
        if(name == null):
            return null
        if(name.get_parents[0] == null || name.get_parents[1] == null):
            return null
        else:
            ancestors.append(name.get_parents[0])
            ancestors.append(name.get_parents[1])
            ancestors.extend(getAncestors(name.get_parents[0]))
            ancestors.extend(getAncestors(name.get_parents[1]))

        return ancestors

    def isRelated(name1, name2):
        result = false
        memberAncestors = getAncestors(name1)
        relativeAncestors = getAncestors(name2)

        #check if they share common ancestor
        for person1 in memberAncestors:
            for person2 in relativeAncestors:
                if person1 == person2:
                    result = true

        #check if one is a direct ancestor
        for person in memberAncestors:
            if person == name2:
                result = true

        for person in relativeAncestors:
            if person == name1:
                result = true

        return result 
