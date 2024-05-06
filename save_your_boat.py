print("""
      Welcome to save your boat game :D 
      
      Description :

        1) you have a boat that have 5 lives when boat lives end it will drown
        2) you should guess the word by choosing a letter from the Eeglish laphapet
        3) if you got a letter wrong you will lose a live
        4) when you guess the letter right you will be provided with the updated word
        5) if you guess everything right you will win
        6) if you finish your lives and did not guess the word you will lose
        7) to quit you can write exit
      """)


words = [
    {
        'name': "cat",
        'hint': [
            "mewo mewo",
            "Likes to chase mice",
            "Purrs when happy",
            "Has sharp retractable claws",
            "Often depicted in memes",
            "Famous cartoon character: Garfield",
            "Known for its whiskers",
            "Can see well in low light",
            "STrst",
            "strat"
        ]
    },
    {
        'name': "bird",
        'hint': [
            "Feathered creature",
            "Flies using wings",
            "Builds nests",
            "Can sing melodious tunes",
            "Often migrates during seasons",
            "Symbolizes freedom and liberty",
            "Has hollow bones for lightness",
            "Variety of species include sparrows, eagles, and parrots"
        ]
    },
    {
        'name': "fish",
        'hint': [
            "Lives underwater",
            "Breathes through gills",
            "Can be cooked and eaten",
            "Found in both freshwater and saltwater",
            "Includes species like salmon, tuna, and cod",
            "Has scales covering its body",
            "Some species migrate long distances",
            "Uses fins for swimming and steering"
        ]
    }
]


lives = 5
def guess_the_letter(attempts):
    global lives
    word = words[attempts]
    answer = word['name']
    print("Guess this")
    guess_blank = f'{"_" * len(answer)}'
    print(guess_blank)
    print("hint :\n" + word['hint'].pop(0))
    counter = 0
    guess_list = list(guess_blank)

    while(True): 
        guess = input("choose a letter ->")
        if guess != "exit":
            if(guess != answer[counter]):
                print("wrong answer") 
                print("hint :\n" + word['hint'].pop(0))
                lives-=1
                print(f'boat lives {lives}')
                if lives == 1:
                    print("hint :\n" + word['hint'].pop(0))
                    print("hint :\n" + word['hint'].pop(0))
            else:
                print("Correct answer")
                guess_list[counter] = guess
                counter+=1
            print("".join(guess_list))
            if("".join(guess_list) == word['name'] ):
                break
            if(lives == 0):
                return 0
        else:
            return 0
        
if __name__=="__main__":
    attempts=0
    response=input("do you want to play (y,n)")

    while response.lower() != "n" and response.lower() !="exit":
        flag = guess_the_letter(attempts)
        attempts +=1
        if(flag == 0 or attempts > len(words)-1):
            print("Game over")
            break
        

    