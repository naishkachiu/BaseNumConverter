# This is a basic binary to decimal converter. It takes the assumption that we are using 8 bit binary numbers.

#Prepare a variable for the final result
output_num = 0

#Ask for first input number --> input_num
input_num = input('Please enter 1st bit:')
output_num += int(input_num) * 1

#Ask for second input number --> input_num
input_num = input('Please enter 2nd bit:')
output_num += int(input_num) * 2

#Ask for third input number --> input_num
input_num = input('Please enter 3rd bit:')
output_num += int(input_num) * 4

#Ask for fourth input number --> input_num
input_num = input('Please enter 4th bit:')
output_num += int(input_num) * 8

#Ask for fifth input number --> input_num
input_num = input('Please enter 5th bit:')
output_num += int(input_num) * 16

#Ask for sixth input number --> input_num
input_num = input('Please enter 6th bit:')
output_num += int(input_num) * 32

#Ask for first input number --> input_num
input_num = input('Please enter 7th bit:')
output_num += int(input_num) * 64

#Ask for first input number --> input_num
input_num = input('Please enter 8th bit:')
output_num += int(input_num) * 128

print('The final result is: ', output_num)