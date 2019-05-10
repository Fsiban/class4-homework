#!usr/bin/env python
# for class 3 homework:
        # identify what type of data each value is, and cast it
        # to the appropriate type, then print the new, properly-typed
        # list to the screen.
        # I.e. ['0.04741', '0.00', '11.930', '0', '0.5730', '6.0300', '80.80', '2.5050', '1', '273.0', '21.00', '396.90', '7.88', '11.90']
        # becomes: [0.04741, 0.0, 11.93, 0, 0.573, 6.03, 80.8, 2.505, 1, 273.0, 21.0, 396.90, 7.88, 11.90]

import os

#grabs breast canncer dataset file from its location
file_path = 'wdbc.data'

#checks if file path and/or file exists
if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')

file = open('wdbc.data')

#strip data that came as lines of strings to string entries in line_values list
for line in file.readlines():
    clean_line = line.replace('  ', ' ').replace('  ', ' ').strip()
    line_values = clean_line.split(' ')

    corrected_line = []
    corrected_file = []

#casting strings in line_values to appropriate type
    for value in line_values:

        if value.isdigit() != True: #using isdigit funtion to seperate the string M and B from the digits (int and float)
            corrected_line.append((value.strip("'")))
            corrected_file.append(corrected_line)
            ##print(corrected_file)

        elif value.find('.') != -1: # check if entry has a point '.' --> float, then add to end of corrected line and add corrected line to end of corrected file
            corrected_line.append(float(value.strip("'")))
            corrected_file.append(corrected_line)

        else: # if no point '.' --> int, and add to end of corrected line and add corrected line to end of corrected file
            corrected_line.append(int(value.strip("'")))
            corrected_file.append(corrected_line)
            ##print(corrected_file)

print(corrected_file) # To print a single line

file.close()


#File update to push to git after conflict








