# lista me Noumera kai strings

Li= [5,6,"ela","ole",9,"omos"]
l1=[]
l2=[]
for i in Li :
    if isinstance(i,int) == True :
        l1.append(i)

    else :
        l2.append(i)

print (f"{l1}\n {l2}")