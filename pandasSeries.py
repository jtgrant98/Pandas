import pandas as pd

grades = pd.Series([87,100,90])


#print(grades)

grades2 = pd.Series(98.6, range(3))

#print(grades.describe())

grades = pd.Series([87,100,90], index = ['Wally','Eva','Sam'])

grades = pd.Series({'Wally': 87, 'Eva' : 100,'Sam' : 94 })

#print(grades)

print(grades['Eva'])

print(grades.Wally)

print(grades.dtype)

print(grades.values)

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

print(hardware)

print(hardware.str.contains('a'))

print(hardware.str.upper())

