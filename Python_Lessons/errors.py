# print("Give me two numbers and I will divide them")
# print("Enter 'q' to quit.")

# while True:
#     try:
#         first_number = int(input("\nFirst number: "))
#         if first_number == 'q':
#             break

#         second_number = int(input("\nSecond number: "))
#         if second_number == 'q':
#             break
#         answer = (first_number) / (second_number)
#     except ZeroDivisionError:
#         print('Cannot divide by 0')
#     except ValueError:
#         print('Enter numbers only')
#     except Exception:
#         print('There was an error')
#     else:
#         print(answer)
#     finally: #for code that we want to run even if there is an exception
#         print('Goodbye')



# values = [10, 9, 8, 0, 5]
# for value in values:
#     try:
#         print(10/ value)
#     except:
#         pass

def calculate_average(numbers):
    """Calculates the average of a list of numbers"""
    total = sum(numbers)
    average = total / len(numbers)
    return average

def get_numbers():
    """Gets a list of numbers from user"""
    numbers = []
    while True:
        user_input = input("Enter numbers or type 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        try:
            number_strings = user_input.split()
            for number_string in number_strings:
                number = float(number_string)
                numbers.append(number)
                return numbers
        except ValueError:
            print('Enter a number.')
    
            

if __name__ == "__main__":
    numbers = get_numbers()
    if numbers:
        average = calculate_average(numbers)
        print(f"The average is: {average}")
    else:
        print("No numbers entered.")
    