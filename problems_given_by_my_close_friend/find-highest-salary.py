salary = {
    "raj": 10000,
    "payal": 28000,
    "jinal": 25000,
    "nayan": 28000
}
index, (max_key, max_value) = max(enumerate(salary.items()))
names_with_max_salary = list(filter(lambda k: salary[k] == max_value, salary.keys()))
max_salary = dict(name=names_with_max_salary,salary=max_value)


print(max_salary)
