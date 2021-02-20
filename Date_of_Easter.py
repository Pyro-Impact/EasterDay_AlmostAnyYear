from Shift15.Restart_Function import confirm_restart

print("Calculate the date for Easter for a certain year.")


def easterdate(user_input):
    if user_input == 1954 or user_input == 1981 or user_input == 2049 or user_input == 2076:
        user_input = user_input - 7
        a = user_input % 19
        b = user_input % 4
        c = user_input % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        return 22 + d + e

    else:
        a = user_input % 19
        b = user_input % 4
        c = user_input % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        return 22 + d + e


def printdate(datenum, year):
    if datenum > 31:
        return "The date for Easter is April " + str(datenum - 31) + "th, " + str(year) + "."
    else:
        return "The date for Easter is March " + str(datenum) + "th, " + str(year) + "."


while True:
    while True:
        year_input = int(input("Choose the year: "))
        if isinstance(year_input, int) is True and year_input in range(1900, 3000):
            break
        else:
            print("Please enter a valid integer for a year that is between 1900 and 2099.")
            continue

    print(printdate(easterdate(year_input), year_input))

    if confirm_restart() == "yes":
        continue
    else:
        break
