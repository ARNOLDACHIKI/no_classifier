def no_classifier ():
    number = input("Enter a numberbetween 0 and 100")
    if not number.isdigit(): 
        raise ValueError("Input is not a valid integer")
    number = int(number)
    is_within_range = (number >= 0) 
    and (number <= 100) 
    if not is_within_range:
        raise ValueError("number out of range. Enter a nnumberbetween o and 100")
    if number % 2 == 0:
        print f("The number {number} is even.")
        else: 
            print f("the number {number} is odd.")
            except ValueError as e: 
                print f("Error: {e}")

                check_odd_or_even() 