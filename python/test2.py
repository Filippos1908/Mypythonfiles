grammata = {}
tonoumena = {"ά": "α",
             "έ": "ε",
             "ή": "η",
             "ί":"ι",
             "ό":"ο",
             "ύ": "υ",
             "ώ":"ω"}
keimeno = input("Δώσε το κείμενο :")
for c in keimeno :
    if c.isalpha():
         if c in tonoumena:
             c = tonoumena[c]
        c = c.upper()
         grammata[c] = grammata.get(c,0) + 1

for c in sorted(grammata.keys()) :
    print ( c, ":", grammata[c], end=", ")
    
