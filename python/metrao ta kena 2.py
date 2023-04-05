a = ("To onoma mou einai    F K")
b= a.count(" ") #methodos count
count = []
count2 = 0
for i in a :
    if i == " " :
        count.append(i)  #methodos apeend se lista
for z in a:
    if z == " " :
        count2 += 1 #me methodo metablitis midenikis kai +
print(f"the spaces are:"{count})