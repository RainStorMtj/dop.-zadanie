grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]] # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sredniy_bal = [sum(grades[0]) / len(grades[0]),
               sum(grades[1]) / len(grades[1]),
               sum(grades[2]) / len(grades[2]),
               sum(grades[3]) / len(grades[3]),
               sum(grades[4]) / len(grades[4])]

list_students = list(sorted(students))
dic_students = {list_students[0]: sredniy_bal[0],
                list_students[1]: sredniy_bal[1],
                list_students[2]: sredniy_bal[2],
                list_students[3]: sredniy_bal[3],
                list_students[4]: sredniy_bal[4]}
print(dic_students)