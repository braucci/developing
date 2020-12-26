     _       _        
#  __| | __ _| |_ __ _ 
# / _` |/ _` | __/ _` |
#| (_| | (_| | || (_| |
# \__,_|\__,_|\__\__,_|
# semplice uso di date                      



from datetime import date

## Creating an instance
x = date(2020,10,25)
d = x.toordinal()
print("Ordinal number of date ",x," is:", d)
print()

## Using today' date
x1 = date.today()
d1 = x1.toordinal()
print("Ordinal number of date ",x1," is:", d1)
print()

intervallo=d1-d

print("Intervallo tra le due date: ", intervallo, "gg")
