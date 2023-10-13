def main():
    temp_list = []
    # for loop will print input statements 7 times for each day of week
    for x in range(7):
        if x == 0:
            day = 'Sunday'
        elif x == 1:
            day = 'Monday'
        elif x == 2:
            day = 'Tuesday'
        elif x == 3:
            day = 'Wednesday'
        elif x == 4:
            day = 'Thursday'
        elif x == 5:
            day = 'Friday'
        else:
            day = 'Saturday'
        temp = float(input('Please enter the temperature for ' + str(day) + ': '))
        temp_list.append(temp)
        # temp_list.append adds the temperatures entered to the list
        # Print statements will print all the temps for each day assuming index 0 is for sun, index 1 for mon, etc.
    print('Temperature on Sunday was', temp_list[0])
    print('Temperature on Monday was', temp_list[1])
    print('Temperature on Tuesday was', temp_list[2])
    print('Temperature on Wednesday was', temp_list[3])
    print('Temperature on Thursday was', temp_list[4])
    print('Temperature on Friday was', temp_list[5])
    print('Temperature on Saturday was', temp_list[6])
    avg = calc_average(temp_list)
    print('Average temperature:', format(avg, ',.2f'))
    equalAvg = count_days(temp_list, avg, 1)
    lessAvg = count_days(temp_list, avg, 2)
    greatAvg = count_days(temp_list, avg, 3)
    print('Number of days above average: ', greatAvg)
    print('Number of days below average: ', lessAvg)
    print('Number of days equal to average: ', equalAvg)

def calc_average(temps):
    x = [temps]
    average = sum(temps) / len(temps)
    return average


def count_days(listA, average, value):
    count = 0
    index = 0
    # if value is 1, count_days will calculate how many temps = avg
    if value == 1:
        for index in listA:
            if index == average:
                count = count + 1
                index = index + 1
            else:
                index = index + 1
    # if value is 2, count_days will calculate how many temps less than avg
    if value == 2:
        for index in listA:
            if index < average:
                count = count + 1
                index = index + 1
            else:
                index = index + 1
    # if value is 3, count_days will calculate how many temps greater than avg
    if value == 3:
        for index in listA:
            if index > average:
                count = count + 1
                index = index + 1
            else:
                index = index + 1
    return count


main()
