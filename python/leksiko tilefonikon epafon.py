#leksiko til epafon
epafes={"Nikos": 111222, "Maria":333444}
#eisagogi eoafis
print("oi epafes einai:\n", epafes)
print("dose mia nea epafi:")
name= input("dose onoma:")
tel= input("dose tel")
epafes[name]= int(tel)
print("oi epafes einai:\n", epafes)
# taksinomisi epafon
epafes_list = list(epafes.items())
print(epafes_list)
epafes_list.sort()
print("taksinimimeni lista einai: \n", epafes_list
      ) 
