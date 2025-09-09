name1 = 'Alice'
Marks1 = 25

name2 = 'Bob'
Marks2 = 23

name3 = 'Charlie'
Marks3 = 24

if Marks1 >= Marks2 and Marks1 >= Marks3:
    print(f'Topper: {name1}')
    
elif Marks2 >= Marks1 and Marks2 >= Marks3:
    print(f'Topper: {name2}')
    
else:
    print(f'Topper: {name3}')