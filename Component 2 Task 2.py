from statistics import mean


def miles_to_km_conversion_array(values_in_mph):
    # This returns Kilometers, whenever i call this function (return) it lets us capture the value
    values_in_kmph = [] # this is an empty list witch stores the values also known as array

    for value in values_in_mph:
        values_in_kmph.append(value * 1.60934)  # this adds the values to the end of the list in kmph 

    return values_in_kmph


def km_to_miles_conversion(km):
    # This returns Miles, whenever i call this function (return) it lets us capture the value and lets us use the value 
    miles = km * 0.621371
    return miles


def compute_output(speed_per_hour):         # this does the calculation for finding the mean, max and minimum speed
    avg_mean = mean(speed_per_hour)         # to find the mean we used the statistics library and only imported mean to calculate the speed 
    max_number = max(speed_per_hour)        #using the inbuilt python min and max function to find the minimum and largest number entered 
    min_number = min(speed_per_hour)

    print(
        f'mean = {str(avg_mean)} \n max = {str(max_number)} \n min = {str(min_number)}')  # used a f string to make it look cleaner and easier to tell what is using what variable.
        


def main():             # this is the main functionw here we will be doing the checks and 
    values_in_mph = []  # the list for mph 
    while True:     # using a while loop to do the checks and this make this loop run indefinately 
        user_input = input(  
            "Please enter a number after the U or E\n Once entered all values enter C to calculate the conversions: ") # this takes the user input 
        first_char = user_input[0].upper() #then using slicing we take letter from the user input and get rid of the number.

        if first_char.isalpha() == False:       # this then takes the first character to make sure the user has enters either U or E
            print("Error please use U(MPH) or E(KMPH) as the first character ") 
            continue # used a continue here to stop here and start the while loop over again if there is no character entered. 

        if 'C' == first_char:                   # this divides the 2 letters and if the lette is C it then uses the compute fuction to do the calculations 
            print('Output (in MPH): ')
            compute_output(values_in_mph)

            print('Output (in KM): ')             # this divides the 2 letters and if the lette is C it then uses the compute fuction to do the calculations 
            compute_output(miles_to_km_conversion_array(values_in_mph))
            break                  # since all the conversions have happened we dont need to do the rest so we use a break 

        if 'Q' == first_char:               # if the user enters Q then the program exits 
            exit()

        number = user_input[1:]     # this is gets the number enterd by using a splitting
        if number.isdigit() == False:   # this checks if the user enters a digit after the Letter. 
            print("Error please enter a number after the U or E")
            continue    # by using continue it loops if this statement is true 

        if 'E' == first_char:       # this checks to see what the first character is. 
            mph_conversion = km_to_miles_conversion(float(number))  # the float makes sure that it isnt a string and changes it to a float. 
            values_in_mph.append(mph_conversion)    # when typing in E it is doing the conversion from km to mph  
            continue

        elif 'U' == first_char:         # the float makes sure that it isnt a string and changes it to a float.
            values_in_mph.append(float(number))     # when typing in E it is doing the conversion from km to mph  
            continue


if __name__ == '__main__':
    main() # this runs main function. 
