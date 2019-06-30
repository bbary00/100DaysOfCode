"""Write program to evaluate (a or not b) and (c or not a) expression
 for boolean varibles a, b, c showing result
 for all possible variables combinations.
"""

for a in range(2):
    for b in range(2):
        for c in range(2):
            print(f"({a} or not {b}) and ({c} or not {a}) = "
                  f"{bool((a or not b) and (c or not a))}")


"""Write a function to return the sum of the numbers in the array, 
returning 0 for an empty array. Since the number 13 is very unlucky, 
it does not count, and numbers that come immediately after a 13 
also do not count. Array could contain strings and boolean values 
(do not count them too):

sum13([1, 2, 2, 1]) -> 6
sum13([1, 1]) -> 2
sum13([1, 2, 2, 1, 13]) -> 6
sum13([1, 2, 2, 1, 13, 5, 4, 2]) -> 6
sum13([1, 2, 2, "Hello", 1, 13, 5, 4, 2]) -> 6
sum13([1, "hi", True, 2, 2, 1, 13, 5, 4, 2]) -> 6
"""

print()
def sum13(lst):
    if 13 in lst:
        lst = lst[:lst.index(13)]
    lst = [el for el in lst if type(el) is int]
    print(sum(lst))


sum13([1, 2, 2, 1])
sum13([1, 1])
sum13([1, 2, 2, 1, 13])
sum13([1, 2, 2, 1, 13, 5, 4, 2])
sum13([1, 2, 2, "Hello", 1, 13, 5, 4, 2])
sum13([1, "hi", True, 2, 2, 1, 13, 5, 4, 2])


"""Write a program to generate list with all numbers 
divisible by 2 and 3 between 1 and 10000 using two approaches:

list comprehension
filter function

"""

list_comprehension = [i for i in range(6, 1001, 3) if not i % 2]
filter_function = list(filter(lambda x: x % 6 == 0, range(1, 1001)))
print(list_comprehension)
print(filter_function)


"""
We need to decrease issues 
count and priority in Python for QA - bugs 
list - Sheet1.csv. Write a program to decrease each issue 
priority to one level (critical -> high, high -> medium, medium -> low), 
issues that have low level now should be removed. 
Save result into new CSV file.
"""


import csv


def decrease_issues():
    priority_by_lvl = {
        0: 'low',
        1: 'medium',
        2: 'high',
        3: 'critical'
    }
    priority_by_name = {
        'low': 0,
        'medium': 1,
        'high': 2,
        'critical': 3
    }
    decrease_issues_list = ['medium', 'high', 'critical']

    with open('data.csv', 'r') as fin:
        reader = list(csv.reader(fin))
        for line in reader:
            if line[-3] in decrease_issues_list:
                new_lvl = priority_by_name[line[-3]] - 1
                line[-3] = priority_by_lvl[new_lvl]
        info = reader

    with open('decreased_data.csv', 'w') as fout:
        writer = csv.writer(fout)
        for line in info:
            writer.writerow(line)


decrease_issues()

