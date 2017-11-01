class run_tree:
    familyTree = list()
    input = "E Bob Diana Matthew"
    plist = input.split()
    if plist[0] == "E":
        #check if familyTree has the person on them and if no, add to list
        p1 = {"Name": plist[1], "Value": Person(plist[1])}
        p2 = {"Name": plist[2], "Value": Person(plist[2])}

        """""
        if p1 not in familyTree:
            familyTree.append(p1)
        else:
            i = 0
            while i < len(familyTree):
                if familyTree[i]['Name'] == plist[1]:
                    p1 = familyTree[i]
                    break
                +i

        if p2 not in familyTree:
            familyTree.append(p2)
        else:
            i = 0
            while i < len(familyTree):
                if familyTree[i]['Name'] == plist[2]:
                    p2 = familyTree[i]
                    break
                +i
        """

        if len(plist) == 4:
            p3 = {"Name": plist[3], "Value": Person(plist[3])}
            if p3 not in familyTree:
                child = p3["Value"]
                child.add_parent(plist[1])
                child.add_parent(plist[2])
                p1["Value"].add_children(plist[3])
                p2["Value"].add_children(plist[3])

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
                for a in temp:
                    if a != plist[3] and a not in child.get_sibling():
                        child.add_sibling(a)

                familyTree.append(p3)
            print("p3 siblings", p3["Value"].get_sibling())

    if plist[0] == 'W':
        print("W")
    if plist[0] == 'X':
        print("X")
