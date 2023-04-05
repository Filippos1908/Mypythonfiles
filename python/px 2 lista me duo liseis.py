#lisi me for
l=[5,8,12,7]
l1=[]
for i in l :
    if i%2 == 1 :
        l1.append(i+10)
print(l1)

#lisi me list comprehensive

l=[5,8,12,7]
l=[x+10 for x in l if x%2==1]
print(l)
