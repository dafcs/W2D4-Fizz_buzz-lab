# def fizz_buzz_obs(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return str(number)

def fizz_buzz(dictionary,number):
    word = ""
    for key in dictionary:
        if number % key == 0:
            word += dictionary[key]
    if word == "":
        return str(number)
    return word

