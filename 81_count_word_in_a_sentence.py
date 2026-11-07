#  Count words in a sentence

def count_word():

    sentence = input("Enter a sentence: ")

    count = 0
    in_word = False

    for ch in sentence:
        if ch != " " and in_word == False:
            count += 1
            in_word = True

        elif ch == " ":
            in_word = False

    print("Total words:", count)
        

count_word()