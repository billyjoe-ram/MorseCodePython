from morse import Morse

print("""
Welcome to Morse Code Parser! A simple, easy to use and tested application, 
to provide you fast output in any occasion you need!\n""")


def main():
    user_option = handle_input()

    if user_option == 'N':
        print('Okay, bye!')
        return

    convert_sentence()
    main()


def handle_input():
    allowed_options = ['Y', 'N']
    user_option = input("Would you like to translate a sentence to morse code? Y / n ")

    user_option = user_option.strip().upper()

    if user_option not in allowed_options:
        print('Invalid input! Pick again')
        return

    return user_option


def convert_sentence():
    parser = Morse()
    user_sentence = input('Type a sentence: ')

    print('Your sentence in morse code is: \n')
    print(parser.parse_sentence(user_sentence))


if __name__ == '__main__':
    main()
