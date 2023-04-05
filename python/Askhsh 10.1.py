# Dimiourgo mia lista me stoixeia pleiades pou periexoun ton kodika k ton xaraktira ton proton

umnos = '''
Σὲ γνωρίζω ἀπὸ τὴν κόψι
τοῦ σπαθιοῦ τὴν τρομερή,
σὲ γνωρίζω ἀπὸ τὴν ὄψι,
ποὺ μὲ βιὰ μετράει τὴν γῆ.
'''

umnos = umnos.split()
print(umnos)

li = [(x[0], ord(x[0])) for x in umnos]
print(li)
