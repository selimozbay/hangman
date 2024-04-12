# libraries
# for choice random words
import random
# for clean terminal screen
import os

# available chars
abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
       'i̇', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's', 't', 'u', 'v', 'w', "x", 'y', 'z')

# 2nd list for delete used chars
abc2 = []

# for used chars
used_abc = []

# game categories
categories = [
    # countries
    ("italy", "france", "turkey", "portugal", "brasil", "japan", "thailand", "russia", "china", "canada", "austria",
     "germany"),
    # world capitals
    ("rome", "paris", "ankara", "lisbon", "brasilia", "tokyo", "bangkok", "moscow", "beijing", "ottawa", "vienna",
     "berlin"),
    # fruits & vegetables
    ("apple", "banana", "coconut", "mango", "eggplant", "lemon", "peppers", "broccoli", "carrot", "potato", "cucumber")
]

hangman = ""
chosen_one = ""
chosen_one_hidden = ""
wrong_guess_counter = 0
new_game = ""
chosen_one_list = []
goon = True
users_guess = ""


def add_to_abc2():
    # adds abc list elements to abc2
    abc2.clear()
    for j in abc:
        abc2.append(j)


def show_hangman(h):
    # prints hangman based on the number of wrong guesses
    global hangman
    os.system('cls||clear')

    if h == 5:
        hangman = "＿＿＿＿\n│     │\n│     0\n│    /│\\\n│    / \\\n"
        print("Unfortunately!")
        print(hangman, "\nAnswer is", chosen_one)
        new_game_f()

    elif h == 4:
        hangman = "＿＿＿＿\n│     │\n│     0\n│    /│\\\n│    /   \n(♥    )"

    elif h == 3:
        hangman = "＿＿＿＿\n│     │\n│     0\n│    /│\\\n│        \n(♥♥   )"

    elif h == 2:
        hangman = "＿＿＿＿\n│     │\n│     0\n│    /│  \n│        \n(♥♥♥  )"

    elif h == 1:
        hangman = "＿＿＿＿\n│     │\n│     0\n│     │  \n│        \n(♥♥♥♥ )"

    else:
        hangman = "＿＿＿＿\n│     │\n│      \n│        \n│        \n(♥♥♥♥♥)"

    print(hangman)
    if h != 5:
        print_abc()


def game_helper():
    # provides information about the game
    print(
        "\nHELP\n"
        "You have to guess the randomly selected word from the selected category by choosing a letter.\n"
        "You have the right to make a total of 5 mistakes.\n"
        "With every wrong choice, the man on the gallows comes closer to the end."
        "You can press the letter q at any time to exit the game.\n"
        "You can make your prediction whenever you want.\n"
        "Every wrong guess takes away one of your rights."
    )
    input("")


def print_abc():
    # shows available letters
    print("\nAvailable letters")
    for a in abc2:
        print(a, end=" ")

    if used_abc:
        # shows used letters
        print("\n\nUsed Letters")
    for b in used_abc:
        print(b, end=" ")


def print_chosen_one_hidden():
    # prints the selected word in a hidden format
    print("\n")
    for c in chosen_one_hidden:
        print(c, end=" ")
    print("\n")


def hide(h):
    # hides the selected word
    global chosen_one_hidden, chosen_one_list

    for _ in h:
        chosen_one_hidden += "＿"

    for z in chosen_one_hidden:
        chosen_one_list.append(z)

    show_hangman(0)

    print_chosen_one_hidden()


def new_game_f():
    # endgame function used to replay the game
    global new_game, goon

    while True:

        new_game = input("New game? y/n").lower()

        if new_game == "y":
            goon = True
            go_on_f()
            break

        elif new_game == "n":
            game_helper()

        elif new_game == "n" or new_game == "q":
            print("Good Bye")
            goon = False
            break

        else:
            print("Incorrect entry!")


def p_game():
    global goon
    print("\n_____ HANGMAN ____")
    print("Help (h), Quit (q)")
    goon = False


def clean_up():
    # clears temporary variables
    global chosen_one, chosen_one_hidden, wrong_guess_counter, chosen_one_list, used_abc, goon, abc2, users_guess, abc

    chosen_one = ""
    chosen_one_hidden = ""
    wrong_guess_counter = 0
    chosen_one_list = []
    used_abc = []
    add_to_abc2()
    users_guess = ""


p_game()


def go_on_f():
    global chosen_one, goon

    clean_up()

    while goon:
        chosen_category = input("\nCategories\n1 Countries\n2 Cities\n3 Fruits - Vegetables\n4 Random\n")

        if chosen_category == "1":
            chosen_one = random.choice(categories[0])
            hide(chosen_one)
            break

        elif chosen_category == "2":
            chosen_one = random.choice(categories[1])
            hide(chosen_one)
            break

        elif chosen_category == "3":
            chosen_one = random.choice(categories[2])
            hide(chosen_one)
            break

        elif chosen_category == "4":
            chosen_one = random.choice(categories[random.randint(0, 2)])
            hide(chosen_one)
            break

        elif chosen_one == "h":
            game_helper()

        elif chosen_one == "q":
            pass

        else:
            print("Incorrect entry!")


def won():
    clean_up()
    os.system('cls||clear')
    print("Congratulations!")

    new_game_f()


while True:
    shall_we_begin = input("Wanna start? y/n\n").lower()

    if shall_we_begin == "y":
        goon = True
        break

    elif shall_we_begin == "n":
        game_helper()

    elif shall_we_begin == "q":
        print("Good Bye")
        break

    else:
        print("Incorrect entry!")

go_on_f()

while goon and wrong_guess_counter < 6:

    print("\n")
    users_guess = input("Letter Selection / Prediction: ").strip().lower()

    if users_guess != "":

        if users_guess in used_abc:
            print(users_guess, "has been tried before!")
        else:

            if len(users_guess) != 1 and len(users_guess) == len(chosen_one):
                if users_guess == chosen_one:
                    won()

                else:
                    print("Wrong guess")
                    wrong_guess_counter += 1
                    show_hangman(wrong_guess_counter)

            elif len(users_guess) == 1:
                if users_guess in abc2:
                    abc2.remove(users_guess)
                    used_abc.append(users_guess)

                    if users_guess in chosen_one:

                        for x, y in enumerate(chosen_one):
                            if users_guess == y:
                                chosen_one_list[x] = users_guess

                        chosen_one_hidden = ""
                        for t in chosen_one_list:
                            chosen_one_hidden += t

                        if chosen_one_hidden == chosen_one:
                            won()
                        else:
                            show_hangman(wrong_guess_counter)
                            print_chosen_one_hidden()

                    else:
                        print("Wrong answer!")
                        wrong_guess_counter += 1
                        show_hangman(wrong_guess_counter)
                        print_chosen_one_hidden()
                else:
                    print("Incorrect entry")
            else:
                print("Incorrect entry")
    else:
        print("Incorrect entry")
