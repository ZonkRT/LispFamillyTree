from person import person

class run_tree:
    #queries = Relation() #for relation object
    familyTree = dict()
    while input != "no":
        answer = input()
        list = answer.split(" ")
        num = len(list) # check if query is complete
        if (num <= 2):
            print("Empty query")
        #check if it is E, and if there are queries filled in
        else:
            if list[0] == "E":
                #add to family tree dictionary if not in familytree
                if list[1] not in familyTree:
                    familyTree[list[1]] = person(list[1])
                if list[2] not in familyTree:
                    familyTree[list[2]] = person(list[2])
                if num == 4: #people make a kid
                    if list[3] not in familyTree:
                        familyTree[list[3]] = person(list[3])
                        child = familyTree[list[3]]
                        child.add_parents(familyTree[list[1]])
                        child.add_parents(familyTree[list[2]])

                        #added child to parents
                        familyTree[list[1]].add_children(child)
                        familyTree[list[2]].add_children(child)

                        #get children born from the two parents + make them kid's sibling
                        temp1 = familyTree[list[1]].get_children()
                        temp2 = familyTree[list[2]].get_children()
                        temp = set(temp1).intersection(temp2)
                        #check if siblings is not kid or already on list
                        for a in temp:
                            if a.get_name() != list[3] and a not in child.get_siblings():
                                child.add_siblings(a)

            elif list[0] == 'W':
                print("W")
                #print(queries.wMethod(list[1], list[2]))
            elif list[0] == 'X' and num == 4:
                print("X")
                #print(queries.xMethod(list[1], list[3], list[2]))
            else:
                print("Error: query doesn't exist")






