
poem ='''
Εγώ μετράω τα ρέστα μου να βγάλω κι άλλο μήνα
ανοίγω και δε βλέπω ουρανό 
εσύ έχεις στο πιάτο σου ολόκληρη Αθήνα
ανοίγεις και χαζεύεις το κενό

'''
print(poem)
#alfabitiki lista lekseon


list_words = poem.split()
list_words.sort()
print(list_words)

#plithos lekseon


print("to plithos ton lekseon einai:{}".format(len(list_words)))


#plthos xaraktiron

poem = poem.replace(" ", "").replace("\n", "")
print("Το πλήθος γραμμάτων είναι: {}".format(len(poem)))
