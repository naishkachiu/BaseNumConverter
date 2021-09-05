
#Loop the program so that we ask for next number after finishing the last question
while True:
  #Ask for an input number --> input_num
  input_num = str(input('Please enter number:'))
  #Prepare a variable for the final result
  output_num = 0 

  #loop through each character from input_num
  for char in range(len(input_num)):
    #if the character is valid
    if int(input_num[char]) <= 1:
      #Multiply the value by the base to the power of the place number --> this_place_value
      this_place_value = int(input_num[char]) * (2**(len(input_num)-char-1))

      #Add this_place_value to the current output_num
      output_num += this_place_value
      # The following are for showing process and debugging
      # Print out the debug information
      print(char, input_num[char], this_place_value, 
      output_num)
  #Print out the final output_num value
  print('The final result is: ', output_num)