def hangman(word):
    wrong = 0
    stages = ["",
              "_______      ",
              "|     |      ",
              "|     0      ",
              "|    /|\     ",
              "|    / \     ",
              "             ",
              ]
    rletters = list(word)      # ze słowa ktore podam tworze liste
    board = ["_"] * len(word) # elementy stages mnoze razy ilosc liter w podanym slowie
    win = False
    print("Enter The Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter: ")

        if guess in rletters:
            idx = rletters.index(guess)
            board[idx] = guess
            rletters[idx] = '$'
        else:
            wrong += 1

        print((" ".join(board)))
        print("\n".join(stages[0:wrong + 1]))

        if "_" not in board:
            print("You absolutely cheated!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose, down you go! The word was: {}".format(word))
            # print("You lose, down you go! The word was: " + "".join(board))


hangman("dupa")