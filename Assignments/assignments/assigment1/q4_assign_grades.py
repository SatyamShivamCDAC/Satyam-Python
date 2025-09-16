# 4. Assign grades or remarks based on marks

marks = int(input('Marks: '))

if marks <= 0 or marks > 100:
    print('Enter valid marks.')
elif marks >= 76:
    print('Distinction')
elif marks >= 54:
    print('Second Class')
elif marks >= 41:
    print('Pass')
else:
    print('Fail')