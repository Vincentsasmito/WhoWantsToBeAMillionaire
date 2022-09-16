import os
import random

class Player:
    # Initialize player values
    prizeDict = {1 : 1000, 2 : 2000, 3: 5000, 4 : 10000, 5: 25000, 6 : 50000, 7 : 100000, 8: 250000, 9 : 500000, 10 : 1000000}
    def __init__(self, lives = 3, ff = True, hint = True, double = True, level = 1, winnings = 0):
        self.level = level
        self.winnings = winnings
        self.lives = lives
        self.ff = ff
        self.hint = hint
        self.double = double
    
    # Update player status (Win/Loss)
    def update(self, result):
        if result == "Win":
            self.winnings = Player.prizeDict[self.level]
            self.level += 1
        elif result == "Loss":
            self.lives -= 1

    # Use powerup
    def powerUp(self, type):
        if type == "ff":
            if self.ff == True:
                self.ff = False
                return "ff"
            else:
                return print("Fifty-Fifty Unavailable.")
        elif type == "hint":
            if self.hint == True:
                self.hint = False
                return "hint"
            else:
                return print("Hint Unavailable.")
        elif type == "double":
            if self.double == True:
                self.double = False
                return "double"
            else:
                return print("Double Unavailable")



def main():
    diff = ""
    inputList = ["easy", "medium", "hard", "test"]
    # Interface & Explanation for players
    while diff.lower() not in inputList:
        print("Welcome to Who Wants To Be A Millionaire!\nPlease choose a difficulty\nEasy | Medium | Hard")
        print("Enter Hint for an explanation")
        diff = input()

        if diff.lower() == "hint":
            print("Easy Difficulty : 3 Lives, Full Powerups | Fifty-Fifty: Delete 2 Wrong Answers | Hint: Self explanatory to be honest | Double: Double the wins, double the risk")
            print("Medium Difficulty: 3 Lives, no powerups")
            print("Hard Difficulty : 1 Life, no powerups\n\n\n")
    
    if diff.lower() == "easy":
        player = Player()

    elif diff.lower() == "medium":
        player = Player(3, False, False, False)

    elif diff.lower() == "hard":
        player = Player(1, False, False, False)
    #Lists and Dicts filled with Answer Keys and their associated questions
    qnaDict = {1 : "a", 2 : "c", 3 : "b", 4 : "d", 5 : "b", 6 : "a", 7 : "d", 8 : "c", 9 : "a", 10 : "b"}
    questionsList = ["A wildlife management military operation occurred in Australia in 1932, this event is also known as", "Vietnam's national currency is", "Who founded the popular sportswear brand Adidas?", "Who is the current CEO of Honda Motor Company", "In the UK, the abbreviation NHS stands for National what Service?", "What name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?", "The hammer and sickle is one of the most recognisable symbols of which political ideology?", "What does the word loquacious mean?",  "Which of these religious observances lasts for the shortest period of time during the calendar year?", "In 1718, which pirate died in a battle off the coast of what is now North Carolina?"]
    answersDict = {1 : ["The Great Emu War", "Operation Zebra", "Integrated National Resources Management", "The Washburn Fire"], 2 : ["Ding", "RMB", "Dong", "Baht"], 3 : ["Adi Dassler", "Adolf Dassler", "Adira Dast", "Bill Bowerman"], 4 : ["Hiroshi Honda", "Suzune Miru", "Kiichiro Toyonda", "Toshihiro Mibe"], 5 : ["Humanity", "Health", "Household", "Honour"], 6 : ["Carousel", "Revolver", "Belt Track", "Baggage Claim"], 7 : ["Socialism", "Capitalism", "Neo-Nazism", "Communism"], 8 : ["Extremely Hungry", "Irritable", "Chatty", "Impatient"], 9 : ["Diwali", "Lent", "Ramadhan", "Easter"], 10 : ["Jack Sparrow", "Blackbeard", "Calico Jack", "William Kidd"]}
    ffLst = ["The Great Emu War", "Dong", "Adolf Dassler", "Toshihiro Mibe", "Health", "Carousel", "Communism", "Chatty", "Diwali", "Blackbeard"]
    hintList = ["It involved machine guns and birds", "Definitely not Ding", "He was born in Germany during the 1900s", "It's not the obvious answer", "This service played a crucial role during the Covid-19 Pandemic", "Has the same exact name as a carnival attraction", "An ideology that the Americans wholeheartedly hate", "Synonymous with Verbose", "This festival is not celebrated by any of the Abrahamic Religions", "Some say he had a dark coloured beard"]

    # Game Begins
    os.system("CLS")
    print("Press Enter to start the game.")
    startGame = input()
    while player.lives >= 1 and player.level < 11:
        ifDouble = False
        print("Welcome to level {}, you have {} lives left.".format(player.level, player.lives))
        print("For ${}, {}".format(Player.prizeDict[player.level], questionsList[player.level - 1]))
        print("A. {}\nB. {}\nC. {}\nD. {}".format(answersDict[player.level][0], answersDict[player.level][1], answersDict[player.level][2], answersDict[player.level][3]))
        if diff.lower() == "easy":
            print("Enter FF for Fifty-Fifty, Hint for Hint, Double for Double")
            playerAnswer = input()
            if playerAnswer.lower() == "ff" or playerAnswer.lower() == "hint" or playerAnswer.lower() == "double":
                pUp = player.powerUp(playerAnswer.lower())
                if pUp == "ff":
                    # Reveals 2 wrong answers
                    decoyLst = []
                    while len(decoyLst) < 2:
                        decoy = random.choice(answersDict[player.level])
                        if decoy != ffLst[player.level - 1] and decoy not in decoyLst:
                            decoyLst.append(decoy)
                    print("{} and {} are Incorrect.".format(decoyLst[0], decoyLst[1]))
                    playerAnswer = input()

                elif pUp == "hint":
                    # Provides a Hint
                    print(hintList[player.level - 1])
                    playerAnswer = input()

                elif pUp == "double":
                    # Doubles wins and losses
                    ifDouble = True

                    playerAnswer = input()
                    if playerAnswer.lower() == qnaDict[player.level]:
                        player.winnings += Player.prizeDict[player.level]
                        player.level += 1
                        player.winnings += Player.prizeDict[player.level]
                        player.level += 1
                    else:
                        player.level += 2
                        player.lives -= 2
                else:
                    playerAnswer = input()
        else:
            playerAnswer = input()
        if(ifDouble == False):
            if playerAnswer.lower() == qnaDict[player.level]:
                player.winnings += Player.prizeDict[player.level]
                player.level += 1
            else:
                player.level += 1
                player.lives -= 1

    if player.lives < 1:
        player.level -= 1
    if player.winnings > 1000000:
        print("Congratulations Player, You have successfully completed all levels, you are")
    elif player.level > 5:
        print("Congratulations Player, You have finished {} levels and will be taking home ${}".format(player.level - 1, player.winnings))
    else:
        print("Unforunately, you have only cleared {} levels and will be going home with ${}. Better luck next time!".format(player.level - 1, player.winnings))

def new_func():
    ifDouble = True
    return ifDouble
        
"""
    #Testing
    elif diff.lower() == "test":
        playerEasy = Player()
        playerMedium = Player(3, False, False, False)
        playerHard = Player(1, False, False, False)

        print("Player Easy Lives = {} ff = {}, hint = {}, double = {}".format(playerEasy.lives, playerEasy.ff, playerEasy.hint, playerEasy.double))
        print("Player Medium Lives = {} ff = {}, hint = {}, double = {}".format(playerMedium.lives, playerMedium.ff, playerMedium.hint, playerMedium.double))
        print("Player Hard Lives = {} ff = {}, hint = {}, double = {}".format(playerHard.lives, playerHard.ff, playerHard.hint, playerHard.double))
"""
if __name__=="__main__":
    main()