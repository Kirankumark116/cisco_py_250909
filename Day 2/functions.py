def find_salaries_sum(first, second):
    return first + second
print(find_salaries_sum(1000,2000))
# print(find_salaries_sum(1000,2000, 3000)) # we get error 

print(find_salaries_sum(second=2000,first=1000))


# 002 | variable parameters -> end of the params
# variable args is of type tuple  
def find_salaries_sum(first, second, *salaries):
    result = first + second 
    for salary in salaries:
        result += salary 
    return result 
#usage 
print(find_salaries_sum(1000,2000))
print(find_salaries_sum(1000,2000,3000))
print(find_salaries_sum(1000,2000,3000,4000))