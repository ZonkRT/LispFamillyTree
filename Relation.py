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
        if relation == "half-siblings":
            list1 = name1.get_parent()[0].get_children()
            list2 = name1.get_parent()[1].get_children()
            halfies = list()
            temp = list(set (list1.append(list2)))
            for a in temp:
                for b in name1.get_sibling():
                    if a != b:
                        halfies.append(a)
            return list(set(halfies))



    
