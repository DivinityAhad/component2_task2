from statistics import mean


def miles_to_km_conversion_array(values_in_mph):
    # This returns Kilometers, whenever i call this function (return) it lets us capture the value
    values_in_kmph = []

    for value in values_in_mph:
        values_in_kmph.append(value * 1.60934)

    return values_in_kmph


def km_to_miles_conversion(km):
    # This returns Miles, whenever i call this function (return) it lets us capture the value
    miles = km * 0.621371
    return miles


def compute_output(speed_per_hour):
    avg_mean = mean(speed_per_hour)
    max_number = max(speed_per_hour)
    min_number = min(speed_per_hour)

    print(
        f'mean = {str(avg_mean)} \n max = {str(max_number)} \n min = {str(min_number)}')


def main():
    values_in_mph = []
    while True:
        user_input = input(
            "Please enter a number after the U or E\n Once entered all values enter C to calculate the conversions: ")
        first_char = user_input[0].upper()

        if first_char.isalpha() == False:
            print("Error please use U(MPH) or E(KMPH) as the first character ")
            continue

        if 'C' == first_char:
            print('Output (in MPH): ')
            compute_output(values_in_mph)

            print('Output (in KMPH): ')
            compute_output(miles_to_km_conversion_array(values_in_mph))
            break

        if 'Q' == first_char:
            exit()

        number = user_input[1:]
        if number.isdigit() == False:
            print("Error please enter a number after the U or E")
            continue

        if 'E' == first_char:
            mph_conversion = km_to_miles_conversion(float(number))
            values_in_mph.append(mph_conversion)
            continue

        elif 'U' == first_char:
            values_in_mph.append(float(number))
            continue


if __name__ == '__main__':
    main()
