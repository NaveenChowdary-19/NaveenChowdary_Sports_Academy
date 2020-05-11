import random

Mumbai_Indians_Squad = []

Team_II_Squad = []



# ==========================================================================================================

class Cricketer:
    def __init__(self, Mumbai_Indians_Squad):

        self.Runs = random.randint(20, 80)

        self.Balls = random.randint(10, 40)

        self.Total_Balls = 0

        self.Total_Runs = 0

        #self.Total_Runs_Team_II = 0

        self.Total_Sixes = 0

        self.Sixes = self.Runs // 12

        self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)

    def Batting_Mumbai(self):

        print("--------------------::  Innings I  ::------------------" , end = "\n\n")

        print("{:<5}{:<25} {:<29} {:<10} {:<10} {:<10} Strike Rate".format(" ","Batsman"," " ,"Runs", "Balls", "Sixes"),end = "\n\n\n")

        for squad in range(0, 11):
            self.Runs = random.randint(0,60)

            self.Sixes = self.Runs // 12

            self.Total_Runs_Mumbai  = 0

            self.Total_Sixes += self.Sixes



            if self.Runs > 45:
                self.Balls = random.randint(30 , 40)
            else:
                self.Balls = random.randint(20 , 30)

            self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)


            if self.Total_Balls <= 120:
                print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Mumbai_Indians_Squad[squad]," " ,self.Runs,self.Balls, self.Sixes, self.Strike_Rate), end="\n\n")
                self.Total_Runs += self.Runs
                self.Total_Balls += self.Balls



            else:
                break
            # print(self.Runs , self.Balls , self.Sixes , self.Strike_Rate)

        print("" , end = "\n")
        print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} ".format(" ", "Total", " ", self.Total_Runs, "120",self.Total_Sixes), end="\n\n\n")



    #===================================================================================================================


        print("{:<5}{:<25} {:<29} {:<10} {:<10} {:<10} Economy".format(" ", "Bowler", " ", "Overs", "Runs", "Wickets" ),
            end = "\n\n\n")

        for squad in range(6 , 11):

            self.Overs = 4

            self.Runs_given = random.randint(24 , 52)

            self.Wickets = random.randint(0 , 3)

            self.Economy = round(self.Runs_given/4 ,1)

            print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Team_II_Squad[squad], " ", self.Overs,
                                                                      self.Runs_given, self.Wickets, self.Economy), end="\n\n")






    def Batting_Team_II(self):

        print("",end = "\n\n\n")

        print("------------------:: Innigs II :: ------------" , end = "\n\n")

        print("{:<5}{:<25} {:<29} {:<10} {:<10} {:<10} Strike Rate".format(" ","Batsman"," " ,"Runs", "Balls", "Sixes"),end = "\n\n\n")

        for squad in range(0, 11):

            self.Runs = random.randint(10, 60)

            self.Sixes = self.Runs // 12

            #self.Total_Runs = 0

            self.Total_Sixes += self.Sixes


            if self.Runs >= 50:
                self.Balls = random.randint(30, 40)
            else:
                self.Balls = random.randint(20, 30)

            self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)


            if self.Total_Balls <= 120:
                print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Team_II_Squad[squad]," " ,self.Runs,self.Balls, self.Sixes, self.Strike_Rate), end="\n\n")
                self.Total_Runs += self.Runs
                self.Total_Balls += self.Balls


            else:
                break

        print("", end="\n")
        print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} ".format(" ", "Total", " ", self.Total_Runs, "120",
                                                                self.Total_Sixes), end="\n\n\n")



     #=====================================================================================



        print("{:<5}{:<25} {:<29} {:<10} {:<10} {:<10} Economy".format(" ", "Bowler", " ", "Overs", "Runs", "Wickets"),
              end="\n\n\n")

        for squad in range(6, 11):
            pass
            self.Overs = 4

            self.Runs_given = random.randint(24, 52)

            self.Wickets = random.randint(0, 3)

            self.Economy = round(self.Runs_given / 4, 1)

            print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Mumbai_Indians_Squad[squad], " ", self.Overs,
                                                                      self.Runs_given, self.Wickets, self.Economy),
                  end="\n\n")


"""
    def Match_Result(self):


        if self.Total_Runs_Mumbai > self.Total_Runs_Team_II:

            self.Result_Runs = self.Total_Runs_Mumbai - self.Total_Runs_Team_II

            print("Mumbai Indians Won By {} ".format(self.Result_Runs))


        else:

            self.Result_Runs = self.Total_Runs_Mumbai - self.Total_Runs_Team_II

            print("Chennai Super Kings Won By {}".format(self.Total_Runs_Team_II - self.Total_Runs_Mumbai))


"""


#======================================================================================================================================

if __name__ == "__main__":
    import json

    Teams = input().split(",")

    Mumbai_Team = json.loads(input())

    Team_II = json.loads(input())

Coin_Spin = ['Bat', 'Bowl']
Toss = random.choice(Coin_Spin)

# ========================================================================================================================================================


print(" ", end="\n\n\n")

Toss_won = random.choice(Teams)
print(
    "Hello... We Bleed Blue.. Welcome To The Wankade .. Its Time For The Toss.. Ganguly Will Spin Coin.. Rohith Calls Annnddddd... ",
    end="\n\n")
print("{}Won The Toss And Choice To {} First".format(Toss_won, Toss))

for keys in Mumbai_Team:
    Mumbai_Indians_Squad.append(Mumbai_Team[keys])

for keys in Team_II:
    Team_II_Squad.append(Team_II[keys])

playing_XI = len(Mumbai_Indians_Squad)

print(" ", end="\n\n\n")

print("{:>10}Mumbai Indians Playing XI are :".format(" ") + "{:>70}".format(" ") + "Chennai Kings Playing XI are :")

print("{:>10}=============================".format(" ") + "{:>72}".format(" ") + "============================",
      end="\n\n")

for player in range(playing_XI):
    print("{:>11}{}. {:<30} {:<66}".format(" ", str(player + 1), str(Mumbai_Indians_Squad[player]), " "),
          "{}. {:<30}".format(str(player + 1), str(Team_II_Squad[player])), end="\n\n")

print(" ", end="\n\n\n")

# ===============================================================================================================================


Team_Mumbai = Cricketer(Mumbai_Indians_Squad)
Team_Chennai = Cricketer(Team_II_Squad)


Team_Mumbai.Batting_Mumbai()
Team_Chennai.Batting_Team_II()


#Team_Mumbai.Match_Result()

#Team_Chennai.Match_Result()


"""

Mumbai Indians , Chennai Kings
{"1":"Rohith Sharma (Cap)" , "2":"Quinton DeKock (Wk)" , "3":"Chris Lynn" , "4":"Yuvaraj Singh" , "5":"Kerion Pollard" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Lasith Malinga" , "9":"Nathan Coulter-Nile" , "10":"Dhawal Kulakarni" , "11":"Jasprith Bumrah"}
{"1":"Shane Watson" , "2":"Ambati Rayudu" , "3":"Sursh Raina" , "4":"Faf Duplesis" , "5":"M S Dhoni (Cap)&(Wk)" , "6":"Dwayne Bravo" , "7":"Ravindra Jadeja" , "8":"Harbajan Singh" , "9":"Deepak Chahar" , "10":"Shardaul Thakur" , "11":"Josh Hazlewood"}

"""
