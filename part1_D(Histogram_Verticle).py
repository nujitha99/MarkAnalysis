count = 0     # number of students
range1 = 0    # 0-29
range2 = 0    # 30-39
range3 = 0    # 40-69
range4 = 0    # 70-100
mark = 0
passcount = 0 # number of passed students
tot = 0
highest = 0
lowest = 0

print('_____Histogram_____')

try:
    mark = int(input("Please enter a mark :"))
    lowest = mark

except ValueError:
    print("you entered something wrong...")

while mark != -1:   # process iterates until the sentinel value

    if 0 <= mark <=100: 
    
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
            
        if 0 <= mark < 30:   # handles the values in range 1
            
            range1 += 1
            count += 1  # increment statement
            tot += mark
            
        elif 30 <= mark < 40:   # handles the values in range 2

            range2 += 1
            
            count += 1  # increment statement
            tot += mark
                
        elif 40 <= mark < 70:   # handles the values in range 3

            range3 += 1
            passcount += 1
            count += 1  # increment statement
            tot += mark
                
        elif 70 <= mark <= 100:   # handles the values in range 4

            range4 += 1
            passcount += 1
            count += 1  # increment statement
            tot += mark
            
    elif mark > 100:   # out of range value are eliminated

        print("The mark you entered is out of range or invalid...")

    elif mark < 0:
        print("The mark you entered is out of range or invalid...")        
        
    try:
        mark = int(input("Please enter a mark :"))

    except ValueError:
        print("you entered something wrong...")

        

############# end of the loop after sentinel value ############


print('\n')

# begins printing the analysis section

print("0-29 ", end='')
print("30-39  ", end='')
print("40-69  ", end='')
print("70-100 ", end='\n')

maxrange = range1       # checks for the longest vertical line
if range2 > maxrange:
    maxrange = range2

if range3 > maxrange:
    maxrange = range3

if range4 > maxrange:
    maxrange = range4

for i in range(0, maxrange):     # prints the * vertically, line by line

    if i < range1:
        print(' * ', end='   ')
    else:
        print('   ', end='   ')

    if i < range2:
        print(' * ', end='    ')
    else:
        print('   ', end='    ')

    if i < range3:
        print(' * ', end='     ')
    else:
        print('   ', end='     ')

    if i < range4:
        print(' * ', end='      ')
    else:
        print('   ', end='      ')

    print('')

print(count,' students in total')

try:    # division by zero is eliminated
    avg = tot/count
    print("The average mark is                 :", round(avg))

except ZeroDivisionError:
    print("Average cannot be calculated")

print("Number of students with a pass mark :", passcount)
print("The highest mark is                 :", highest)
print("The lowest mark is                  :", lowest)

