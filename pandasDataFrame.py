import pandas as pd

grades_dict = {'Wally': [87,96,70],
                'Eva': [100,87,90],
                'Sam': [94,77,90],
                'Katie': [100,81,82],
                'Bob': [83,65,85]}

grades = pd.DataFrame(grades_dict)

print(grades)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

print(grades['Eva'])

print(grades.Sam)

print(grades.loc['Test1'])

print(grades.iloc[1])   #iloc does not include upper limit

print(grades.loc['Test1':'Test3']) #loc includes upper limit

print(grades.iloc[0:2])

print(grades.loc[['Test1','Test3']])

print(grades.iloc[[0, 2]])

print(grades.loc['Test1':'Test2',['Eva','Katie']])

print(grades.iloc[0:2,[1,3]])



grades90 = grades[grades>=90]

#print(grades90) #NAN means not a number and didnt pass the test 

gradesB = grades[(grades>=80) & (grades < 90)]

gradesAorB = grades[(grades > 90) | (grades >= 90)]

#print(gradesAorB)


#print(grades.at['Test2','Eva'])

#grades.at['Test2','Eva'] = 100

#print(grades)

#print(grades.iat[1,1])

#print(grades.describe())

pd.set_option('Precision',2)

print(grades.describe())

print(grades.T.describe())      #T = Transpose which changes columns and rows

#sort by index or sort by value

print(grades.sort_index(ascending = False))

print(grades.sort_index(axis = 1))


print(grades.sort_index(axis = 0))


print(grades.sort_values(by='Test1', axis = 1, ascending = False))

print(grades.T.sort_values(by='Test1', ascending = False))

print(grades.loc['Test1'].sort_values(ascending = False))