#String Method format()

# using print("{data will apper here}").format(date_you_want)

output = "{} {} {}".format("Hello", "Python", "is easy")
print(output)

# can change the order of the output
output = "{2} {0} {1}".format("Hello", "Python", "is easy")
print(output)

# can custom datatype like point of the float
output = "|{0:10d}|{0:.2f}|{1:10.2f}".format(23, 45.6789)
print(output)

# can make and use parameter inside format 
output = "|{id:>15s}|{name}|{score:7.2f}".format(
        id='6010406999', name='Stop Jeep', score=100)
print(output)