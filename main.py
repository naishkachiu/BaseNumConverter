
#Loop the program so that we ask for next number after finishing the last question
#Create a library for mapping characters of all bases (up to 36)
digit_library = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
  #Ask for an input number --> input_num, and reverse it
  input_num = str(input('Please enter number:'))[::-1]
  #Ask for base of input
  input_base = int(input('What base is the input number in? (2-36)'))
  #Ask for base of output
  output_base = int(input('What base do you wish to output? (2-36)'))
  #Prepare a variable for the final result
  base10_num = 0
  input_library = digit_library[0:input_base]

  #loop through each character from input_num
  for char in range(len(input_num)):
    #check if digit is valid
    if input_num[char] in input_library:
      #Multiply the value by the base to the power of the place number --> this_place_value
      this_place_value = input_library.index(input_num[char]) * (input_base**char)

      #Add this_place_value to the current base10_num
      base10_num += this_place_value
      # The following are for showing process and debugging
      # Print out the debug information
      print(char, input_num[char], this_place_value, 
      base10_num)

  #Print out the final base10_num value
  print('In base 10 this is: ', base10_num)

  #Convert Decimal to Output Base
  output_num = ''
  temp_quotient = base10_num
  finished = (temp_quotient < output_base)
  while (temp_quotient >= output_base):
    temp_remainder = temp_quotient%output_base
    output_num += digit_library[temp_remainder]
    temp_quotient = int(temp_quotient / output_base)
  temp_remainder = temp_quotient%output_base
  output_num += digit_library[temp_remainder]

  #Print the final answer
  print('Answer in base ', output_base, ': ', output_num[::-1])
  print('---')
    