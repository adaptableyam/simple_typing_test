import random
from time import sleep, time

def txt_grabber(filename):
    six_letter = []
    with open(filename) as file:
        for line in file:
            word = file.readline()
            word = word.replace("\n", "")
            six_letter.append(word)
    return six_letter


def main():
    WORD_COUNT = 10
    MINUTE = 60
    correct = 0
    total_time = 0.00
    wpm = 0.00
    test_list = []
    word_list = txt_grabber("6letter.txt")
    for i in range(WORD_COUNT):
        word = word_list[random.randrange(0, len(word_list))]
        test_list.append(word)
    
    print("Welcome to my basic typing test!")
    start = input("Would you like to begin? (Y/N) ").upper()
    if start != "Y" and start != "YES":
        return 1
    else:
        print("Ok, test will begin!")
        sleep(2)
        print("words will appear one at a time, please type them as quickly and as accurately as possible.")
        sleep(2)
        #start test
        for i in range(WORD_COUNT):
            start_time = time()
            print(test_list[i])
            answer = input()
            end_time = time()
            word_time = end_time - start_time
            total_time += word_time
            if answer == test_list[i]:
                correct += 1
        wpm = round((MINUTE/(total_time / WORD_COUNT)), 2)
        print(f"You got {correct} out of {WORD_COUNT}, this means you got an accuracy of {correct/WORD_COUNT*100}%")
        print(f"You took {round(total_time, 2)} seconds, this means you averaged {wpm} wpm!")




    




if __name__ == '__main__':
    main()