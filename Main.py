class run_tree:
    #queries = Relation() #for relation object
    familyTree = list()
    input = "E Bob Diana Matthew"
    key, d1, d2, d3 = input.split()
    if key == "E":
        #check if familyTree has the person on them and if no, add to list
        #p1 and p2 are the parents
        p1 = {"Name": d1, "Value": Person(d1)}
        p2 = {"Name": d2, "Value": Person(d2)}

        print(p1["Value"].get_name())
        print(p2["Value"].get_name())

        """""
        if p1 not in familyTree:
            familyTree.append(p1)
        else:
            i = 0
            while i < len(familyTree):
                if familyTree[i]['Name'] == d1:
                    p1 = familyTree[i]
                    break
                +i

        if p2 not in familyTree:
            familyTree.append(p2)
        else:
            i = 0
            while i < len(familyTree):
                if familyTree[i]['Name'] == d2:
                    p2 = familyTree[i]
                    break
                +i
        """

        if d3 != "":
            p3 = {"Name": d3, "Value": Person(d3)}
            if p3 not in familyTree:
                child = p3["Value"]
                child.add_parents(d1)
                child.add_parents(d2)

                #added children to make a siblings list
                p1["Value"].add_children(d3)
                p2["Value"].add_children(d3)

                p1["Value"].add_children("Elisa")
                p1["Value"].add_children("Son")

                p2["Value"].add_children("Elisa")
                p2["Value"].add_children("Nutter")

                print("p1 kids", p1["Value"].get_children())
                print("p2 kids", p2["Value"].get_children())

                #get children born from the two parents + make them kid's sibling
                temp1 = p1["Value"].get_children()
                temp2 = p2["Value"].get_children()
                temp = set(temp1).intersection(temp2)
                #check if siblings is not kid or already on list
                for a in temp:
                    if a != d3 and a not in child.get_siblings():
                        child.add_siblings(a)

                familyTree.append(p3)
            print("p3 siblings", p3["Value"].get_siblings())

    if key == 'W':
        print("W")
        #print(queries.wMethod(d1, d2))
    if key == 'X':
        print("X")
        #print(queries.xMethod(d1, d3, d2))
