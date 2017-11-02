from person import person

class run_tree:
    #queries = Relation() #for relation object
    familyTree = dict()
    answer = "hi"
    while input != "no":
        answer = input()
        if answer == "":
            print("Empty query entered")
        else:
            key, d1, d2, d3 = answer.split()
            if key == "E":
                #add to family tree dictionary if not in familytree
                if d1 not in familyTree:
                    familyTree[d1] = person(d1)
                if d2 not in familyTree:
                    familyTree[d2] = person(d2)
                if d3 != "":
                    if d3 not in familyTree:
                        familyTree[d3] = person(d3)
                        child = familyTree[d3]
                        child.add_parents(familyTree[d1])
                        child.add_parents(familyTree[d2])

                        print("p3 parents: ")
                        for a in familyTree[d3].get_parents():
                            print(a.get_name())
                        print()

                        #added children to make a siblings list
                        familyTree[d1].add_children(child)
                        familyTree[d2].add_children(child)

                        print("p1 kids: ")
                        for a in familyTree[d1].get_children():
                            print(a.get_name())
                        print()
                        print("p2 kids: ")
                        for a in familyTree[d2].get_children():
                            print(a.get_name())

                        #get children born from the two parents + make them kid's sibling
                        temp1 = familyTree[d1].get_children()
                        temp2 = familyTree[d2].get_children()
                        temp = set(temp1).intersection(temp2)
                        #check if siblings is not kid or already on list
                        for a in temp:
                            if a.get_name() != d3 and a not in child.get_siblings():
                                child.add_siblings(a)
                    print()
                    print("p3 siblings: ")
                    for a in familyTree[d3].get_siblings():
                        print(a.get_name())

            elif key == 'W':
                print("W")
                #print(queries.wMethod(d1, d2))
            elif key == 'X':
                print("X")
                #print(queries.xMethod(d1, d3, d2))
            else:
                print("Error: query doesn't exist")






