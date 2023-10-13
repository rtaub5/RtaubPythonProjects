my_list = []
total = 0
for x in range(7):
    sales = int(input('Please enter the number of sales for each day of the week: '))
    my_list.append(sales)
for value in my_list:
    total += value
print(my_list)
print(total)



