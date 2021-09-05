
#Loop the program so that we ask for next number after finishing the last question
#Create a library for mapping characters of all bases (up to 36)
digit_library = [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
while True:
  #Ask for an input number --> input_num, and reverse it
  input_num = str(input('Please enter number:'))[::-1]
  #Prepare a variable for the final result
  output_num = 0

  #loop through each character from input_num
  for char in range(len(input_num)):
    #if the character is valid
    if int(input_num[char]) <= 1:
      #Multiply the value by the base to the power of the place number --> this_place_value
      this_place_value = int(input_num[char]) * (2**char)

      #Add this_place_value to the current output_num
      output_num += this_place_value
      # The following are for showing process and debugging
      # Print out the debug information
      print(char, input_num[char], this_place_value, 
      output_num)
  #Print out the final output_num value
  print('The final result is: ', output_num)