import os

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
                return 0
            else:
                return 1
        elif type == "hint":
            if self.hint == True:
                self.hint = False
                return 0
            else:
                return 1
        elif type == "double":
            if self.double == True:
                self.double = False
                return 0
            else:
                return 1



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

    qnaDict = {1 : "The Great Emu War", 2 : "Dong", 3 : "Adolf Dassler", 4 : "Toshihiro Mibe", 5 : "Health", 6 : "Carousel", 7 : "Communism", 8 : "Chatty", 9 : "Diwali", 10 : "Blackbeard"}
    questionsList = ["A wildlife management military operation occurred in Australia in 1932, this event is also known as", "Vietnam's national currency is", "Who founded the popular sportswear brand Adidas?", "Who is the current CEO of Honda Motor Company", "In the UK, the abbreviation NHS stands for National what Service?", "What name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?", "The hammer and sickle is one of the most recognisable symbols of which political ideology?", "What does the word loquacious mean?",  "Which of these religious observances lasts for the shortest period of time during the calendar year?", "In 1718, which pirate died in a battle off the coast of what is now North Carolina?"]
    answersDict = {1 : ["The Great Emu War", "Operation Zebra", "Integrated National Resources Management", "The Washburn Fire"], 2 : ["Ding", "RMB", "Dong", "Baht"], 3 : ["Adi Dassler", "Adolf Dassler", "Adira Dast", "Bill Bowerman"], 4 : ["Hiroshi Honda", "Suzune Miru", "Kiichiro Toyonda", "Toshihiro Mibe"], 5 : ["Humanity", "Health", "Household", "Honour"], 6 : ["Carousel", "Revolver", "Belt Track", "Baggage Claim"], 7 : ["Socialism", "Capitalism", "Neo-Nazism", "Communism"], 8 : ["Extremely Hungry", "Irritable", "Chatty", "Impatient"], 9 : ["Diwali", "Lent", "Ramadhan", "Easter"], 10 : ["Jack Sparrow", "Blackbeard", "Calico Jack", "William Kidd"]}

    # Game Begins
    os.system("CLS")
    print("Press Enter to start the game.")
    startGame = input()
    while player.lives > 1 and player.level < 11:
        print("Welcome to level {}, you have {} lives left.".format(player.level, player.lives))
        print("For ${}, {}".format(Player.prizeDict[player.level], questionsList[player.level - 1]))
        print("A. {}\nB. {}\nC. {}\nD. {}".format(answersDict[player.level][0], answersDict[player.level][1], answersDict[player.level][2], answersDict[player.level][3]))
        playerAnswer = input()
        player.level += 1
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