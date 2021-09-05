
#Create a library for mapping characters of all bases (up to 36)
digit_library = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Loop the program so that we ask for next number after finishing the last question
while True:
  #An error class to help catch problems
  class Problem(Exception): pass
  #Try block helps to catch any errors
  try:
    #Ask for an input number --> input_num, and reverse it
    input_num = str(input('Please enter number to convert:'))[::-1]
    #Ask for base of input
    input_base = int(input('What base is the input number in? (2-36)'))
    #Ask for base of output
    output_base = int(input('What base do you wish to output? (2-36)'))
    #Prepare a variable for the final result
    base10_num = 0
    #Create a library of just the numbers in the input_base
    input_library = digit_library[0:input_base]

    # Print out some debug header information
    print("place, digit, value base 10, running ttl")

    #loop through each character from input_num
    for char in range(len(input_num)):
      #check if digit is valid (not out of range)
      if input_num[char] in input_library:
        #Multiply the value by the base to the power of the place number --> this_place_value
        this_place_value = input_library.index(input_num[char]) * (input_base**char)

        #Add this_place_value to the current base10_num
        base10_num += this_place_value
        # The following are for showing process and debugging
        # Print out the debug information
        print(char, input_num[char], this_place_value,
        base10_num)
      #If a character is invalid, print an error message to say which digit is problematic and raise an error
      else:
        print('Problem in number: ', input_num[char])
        raise Problem

    #Print out the base10_num value
    print('In base 10 this is: ', base10_num)

    #Convert Decimal to Output Base
    #create a variable to hold the final output (string)
    output_num = ''
    #create a temporary variable that will hold the value as we divide it by the output_base
    temp_quotient = base10_num
    #While the most recent divided number is greater than the output_base
    while (temp_quotient >= output_base):
      #Get the remainder value by dividing by output_base
      temp_remainder = temp_quotient%output_base
      #search the library for the character value and add to the output text
      output_num += digit_library[temp_remainder]
      #divide the value by the output_base and get the new temporary quotient
      temp_quotient = int(temp_quotient / output_base)
    #Get the final remainder value
    temp_remainder = temp_quotient%output_base
    #search the library for the final character value and add to the output text  
    output_num += digit_library[temp_remainder]

    #Print the final answer (the reverse of the output_num)
    print(input_num, ' of base ', input_base, ' converted to base ', output_base, ' is: ', output_num[::-1])

  #If a Problem has been raised, send a general error message
  except Problem:
    print('Please check your number and try again.')

  #print a line divider
  print('---')