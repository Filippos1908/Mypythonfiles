a=["1","oLe","oXi","1234"]
a1= []
a2= []
for i in a:
    if i.isalpha() :
        a1.append(i)

    else:
        a2.append(i)

        print(f"{a1}\t\t{a2}")
        print(f"{sorted(a1)}\t\n{sorted(a2)}")
