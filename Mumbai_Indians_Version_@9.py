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

        self.Total_Runs_Team_II = 0

        self.Total_Runs_Mumbai = 0

        self.Total_Sixes = 0

        self.Sixes = self.Runs // 12

        self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)

    def Series(self):


        for i in range(5):
            self.Total_Balls = 0

            self.Total_Runs = 0

            self.Total_Sixes = 0

            count = 0

            #def Batting_Mumbai(self):

            print("{}   MATCH NO -- {}   {}".format(60 * "#" ,i+1 , 60 * "#" ) , end = "\n\n\n")

            print("--------------------::  Innings I  ::------------------" , end = "\n\n")

            print("{:<5}{:<25} {:<9} {:<43} {:<19} {:<10} {:<10} {:<10} Strike Rate".format(" ","Batsman"," " , " " , " " , "Runs", "Balls", "Sixes"),end = "\n\n\n")


            for squad in range(0, 11):

                self.Runs = random.randint(0,60)

                self.Sixes = self.Runs // 12


                if self.Runs > 45:
                    self.Balls = random.randint(30 , 40)
                else:
                    self.Balls = random.randint(20 , 30)

                self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)

                #================================================

                Bowled_By_List_Team_II = []

                for bowl in range(6,11):
                    Bowled_By_List_Team_II.append(Team_II_Squad[bowl])


                wicket_type = ["Caught ", "Hit Wicket", "Bowled", "Stumped" , "Caught And Bowled"]

                caught_by = random.choice(Team_II_Squad)

                wicket_type_given = random.choice(wicket_type)

                is_wk = "(Wk)"


                for players in range(0, 11):
                    if is_wk in Team_II_Squad[players]:
                        Wicky = Team_II_Squad[players]

                if wicket_type_given == "Stumped":
                    type = wicket_type_given + " By " + Wicky

                elif wicket_type_given == "Bowled" or wicket_type_given == "Hit Wicket" or wicket_type_given == "Caught And Bowled":

                    Bowled_by = random.choice(Bowled_By_List_Team_II)

                    type = wicket_type_given + " By " + Bowled_by


                else:

                    type = wicket_type_given + " By " + caught_by

                if self.Total_Balls <= 120:
                    print("{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} {}".format(" ", Mumbai_Indians_Squad[squad]," "  , type ,  " " ,self.Runs,self.Balls, self.Sixes, self.Strike_Rate), end="\n\n")
                    self.Total_Runs += self.Runs
                    self.Total_Balls += self.Balls
                    self.Total_Sixes += self.Sixes
                    count = count+1



                else:
                    print("{:<5}{:<25} ".format(" " , Mumbai_Indians_Squad[squad]) , end = "\n\n")
                    # print(self.Runs , self.Balls , self.Sixes , self.Strike_Rate)



            print("" , end = "\n")
            print("{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} ".format(" ", "Total", " "," " , " " ,   self.Total_Runs, "120",self.Total_Sixes), end="\n\n\n")

            self.Total_Runs_Mumbai = self.Total_Runs

            #print("Total Runs Of Mumbai Indians Are ::===== {}".format(self.Total_Runs_Mumbai))

            #print(count)



    #===================================================================================================================

            print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} Economy".format(" ", "Bowler", " ", "Overs", "Runs", "Wickets"),
                end="\n\n\n")

            i = 0
            self.Bowler_1 = 0
            self.Bowler_2 = 0
            self.Bowler_3 = 0
            self.Bowler_4 = 0
            self.Bowler_5 = 0

            self.Bowler_1_wick = 0
            self.Bowler_2_wick = 0
            self.Bowler_3_wick = 0
            self.Bowler_4_wick = 0
            self.Bowler_5_wick = 0

            Var = True

            while Var:
                if self.Bowler_1 + self.Bowler_2 + self.Bowler_3 + self.Bowler_4 + self.Bowler_5 == self.Total_Runs_Mumbai and self.Bowler_1_wick + self.Bowler_2_wick + self.Bowler_3_wick + self.Bowler_4_wick + self.Bowler_5_wick == count:
                    Var = False

                else:
                    self.Bowler_1 = random.randint(10, 52)
                    self.Bowler_2 = random.randint(10, 52)
                    self.Bowler_3 = random.randint(10, 52)
                    self.Bowler_4 = random.randint(10, 52)
                    self.Bowler_5 = random.randint(10, 52)

                    self.Bowler_1_wick = random.randint(0 , 2)
                    self.Bowler_2_wick = random.randint(0 , 2)
                    self.Bowler_3_wick = random.randint(0 , 2)
                    self.Bowler_4_wick = random.randint(0 , 2)
                    self.Bowler_5_wick = random.randint(0 , 2)


            List = [self.Bowler_1 , self.Bowler_2 , self.Bowler_3 , self.Bowler_4 , self.Bowler_5]

            List_wick = [self.Bowler_1_wick , self.Bowler_2_wick , self.Bowler_3_wick , self.Bowler_4_wick , self.Bowler_5_wick]
            #print(List)

            for squad in range(6, 11):
                self.Overs = 4

                # self.Runs_given = random.randint(24, 52)

                self.Wickets = random.randint(0, 3)

                self.Economy = round(List[i] / 4, 1)

                print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Team_II_Squad[squad], " " ,  self.Overs,
                                                                      List[i], List_wick[i], self.Economy),
                    end="\n\n")
                i = i + 1



            #def Batting_Team_II(self):

            print("",end = "\n\n\n")

            print("------------------:: Innigs II :: ------------" , end = "\n\n")

            print("{:<5}{:<25} {:<9} {:<43}{:<19} {:<10} {:<10} {:<10} Strike Rate".format(" ","Batsman"," " , " " , " " ,  "Runs", "Balls", "Sixes"),end = "\n\n\n")

            self.Total_Balls = 0
            self.Total_Runs = 0
            self.Total_Sixes = 0

            count = 0

            for squad in range(0, 11):



                self.Runs = random.randint(10, 60)

                self.Sixes = self.Runs // 12


                if self.Runs >= 50:
                    self.Balls = random.randint(30, 40)
                else:
                    self.Balls = random.randint(20, 30)

                self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)

                #==================================================================

                Bowled_By_List_Mumbai = []

                for bowl in range(6, 11):
                    Bowled_By_List_Mumbai.append(Mumbai_Indians_Squad[bowl])

                wicket_type = ["Caught ", "Hit Wicket", "Bowled", "Stumped" , "Caught And Bowled"]

                caught_by = random.choice(Mumbai_Indians_Squad)

                Bowled_by  = random.choice(Bowled_By_List_Mumbai)

                wicket_type_given = random.choice(wicket_type)


                wicket_type_given = random.choice(wicket_type)

                is_wk = "(Wk)"

                for players in range(0 , 11):
                    if is_wk in Mumbai_Indians_Squad[players]:
                        Wicky = Mumbai_Indians_Squad[players]

                if wicket_type_given == "Stumped":
                    type = wicket_type_given + " By " + Wicky

                elif wicket_type_given == "Bowled" or wicket_type_given == "Hit Wicket" or wicket_type_given == "Caught And Bowled":
                    type = wicket_type_given + " By " + Bowled_by

                else:

                   type = wicket_type_given + " By " + caught_by

                if self.Total_Balls <= 120:
                    print("{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} {}".format(" ", Team_II_Squad[squad]," " , type , " " ,  self.Runs,self.Balls, self.Sixes, self.Strike_Rate), end="\n\n")
                    self.Total_Runs += self.Runs
                    self.Total_Balls += self.Balls
                    self.Total_Sixes += self.Sixes

                    count = count + 1

                else:

                    print("{:<5}{:<25}".format(" " , Team_II_Squad[squad]) , end = "\n\n")


            print("", end="\n")
            print("{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} ".format(" ", "Total", " " , " " , " " ,  self.Total_Runs, "120",
                                                                self.Total_Sixes), end="\n\n\n")

            self.Total_Runs_Team_II = self.Total_Runs
            #print("Total Runs Of Chennai Kings Are:::======{}".format(self.Total_Runs_Team_II))
            #print(count)


     #=====================================================================================


            print("{:<5}{:<25} {:<29} {:<10} {:<10} {:<10} Economy".format(" ", "Bowler", " ", "Overs", "Runs", "Wickets"),
                end="\n\n\n")

            i = 0
            self.Bowler_1 = 0
            self.Bowler_2 = 0
            self.Bowler_3 = 0
            self.Bowler_4 = 0
            self.Bowler_5 = 0

            self.Bowler_1_wick = 0
            self.Bowler_2_wick = 0
            self.Bowler_3_wick = 0
            self.Bowler_4_wick = 0
            self.Bowler_5_wick = 0


            var = True

            while var:
                if self.Bowler_1 + self.Bowler_2 + self.Bowler_3 + self.Bowler_4 + self.Bowler_5 == self.Total_Runs_Team_II and self.Bowler_1_wick + self.Bowler_2_wick + self.Bowler_3_wick + self.Bowler_4_wick + self.Bowler_5_wick == count:
                    var = False

                else:
                    self.Bowler_1 = random.randint(10 , 52)
                    self.Bowler_2 = random.randint(10 , 52)
                    self.Bowler_3 = random.randint(10 , 52)
                    self.Bowler_4 = random.randint(10 , 52)
                    self.Bowler_5 = random.randint(10 , 52)

                    self.Bowler_1_wick = random.randint(0, 2)
                    self.Bowler_2_wick = random.randint(0, 2)
                    self.Bowler_3_wick = random.randint(0, 2)
                    self.Bowler_4_wick = random.randint(0, 2)
                    self.Bowler_5_wick = random.randint(0, 2)



            List = [self.Bowler_1 , self.Bowler_2 , self.Bowler_3 , self.Bowler_4 , self.Bowler_5]

            List_wick = [self.Bowler_1_wick, self.Bowler_2_wick, self.Bowler_3_wick, self.Bowler_4_wick,  self.Bowler_5_wick]
            #print(List)

            for squad in range(6, 11):
                self.Overs = 4

                #self.Runs_given = random.randint(24, 52)

                self.Wickets = random.randint(0, 3)

                self.Economy = round(List[i] / 4, 1)

                print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Mumbai_Indians_Squad[squad], " ", self.Overs,
                                                                      List[i], List_wick[i], self.Economy),
                    end="\n\n")
                i = i+1




            if self.Total_Runs_Mumbai > self.Total_Runs_Team_II:

                self.Result_Runs = self.Total_Runs_Mumbai - self.Total_Runs_Team_II

                print("" , end = "\n\n")


                print("{:<40}{} Won By {} ".format(" " ,Teams[0] ,self.Result_Runs)  , end = "\n\n\n")
                print(58 * "===" , end = "\n\n\n")


            elif self.Total_Runs_Mumbai < self.Total_Runs_Team_II:

                self.Result_Runs = self.Total_Runs_Team_II - self.Total_Runs_Mumbai

                print("" , end = "\n\n")

                print("{:<40} {} Won By {}".format(" " , Teams[1] ,self.Total_Runs_Team_II - self.Total_Runs_Mumbai) , end = "\n\n\n")
                print(58 * "===" , end = "\n\n\n")


            else:

                print("", end="\n\n")

                print("Wwwwwwoooooooowwwwww  Are You Kidding Me Avengers..... You Gotta be Assemble  Nowww.... It Its Tie  Can you Believe It.. ....... ",end="\n\n")

                print(" We Are Going To Witness A Super Over Tonigt   ... Here We Go ...")
                Super_Over = random.choice[Teams]

                Super_Over_Runs = random.randint(1 , 10)

                print("{} {} Won By {} Runs In The Mighty Super Over...".format(45 * " " , Super_Over , Super_Over_Runs) , end = "\n\n")
                print(58 * "===", end="\n\n\n")



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

#==============================================================

#Stats_Of_Mumbai = {}
#Stats_Of_Team_II = {}


Stats_Of_Mumbai = {player : 0 for player in Mumbai_Indians_Squad}
print(Stats_Of_Mumbai)

Stats_Of_Team_II = {player :0 for player in Team_II_Squad}
print(Stats_Of_Team_II)


#=============================================================================================================================================


print(" ", end="\n\n\n")

print("{:>10} {} Playing XI are :".format(" " , Teams[0]) + "{:>68}".format(" ") + "{} Playing XI are :".format(Teams[1]))

print("{:>10}=============================".format(" ") + "{:>72}".format(" ") + "================================",
      end="\n\n")

for player in range(playing_XI):
    print("{:>11}{}. {:<30} {:<66}".format(" ", str(player + 1), str(Mumbai_Indians_Squad[player]), " "),
          "{}. {:<30}".format(str(player + 1), str(Team_II_Squad[player])), end="\n\n")

print(" ", end="\n\n\n")

# ===============================================================================================================================


Team_Mumbai = Cricketer(Mumbai_Indians_Squad)
Team_Chennai = Cricketer(Team_II_Squad)


#Team_Mumbai.Batting_Mumbai()
#Team_Chennai.Batting_Team_II()
Obj = Team_Mumbai.Series()




"""

Mumbai Indians , Chennai Kings
{"1":"Rohith Sharma (Cap)" , "2":"Quinton DeKock (Wk)" , "3":"Chris Lynn" , "4":"Yuvaraj Singh" , "5":"Kerion Pollard" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Lasith Malinga" , "9":"Nathan Coulter-Nile" , "10":"Dhawal Kulakarni" , "11":"Jasprith Bumrah"}
{"1":"Shane Watson" , "2":"Ambati Rayudu" , "3":"Sursh Raina" , "4":"Faf Duplesis" , "5":"M S Dhoni (Cap)&(Wk)" , "6":"Dwayne Bravo" , "7":"Ravindra Jadeja" , "8":"Harbajan Singh" , "9":"Deepak Chahar" , "10":"Shardaul Thakur" , "11":"Josh Hazlewood"}

Mumbai Indians , Royal Challengers
{"1":"Rohith Sharma (Cap)" , "2":"Quinton DeKock (Wk)" , "3":"Chris Lynn" , "4":"Yuvaraj Singh" , "5":"Kerion Pollard" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Lasith Malinga" , "9":"Nathan Coulter-Nile" , "10":"Dhawal Kulakarni" , "11":"Jasprith Bumrah"}
{"1":"Aron Finch" , "2":"Parthiv Patel (Wk)" , "3":"Virat Kohli (Cap)" , "4":"A B Devilliers" , "5":"Shivam Dube" , "6":"Devdutt Padikkal" , "7":"Chris Morris" , "8":"Washington Sundar" , "9":"Umesh Yadav" , "10":"Yuzvendra Chahal" , "11":"Dale Steyn"}

India  , Australia
{"1":"Rohith Sharma " , "2":"Shikar Dhawan" , "3":"Virat Kohli " , "4":"Yuvaraj Singh" , "5":"M S Dhoni (Cap)&(Wk)" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Ravindra Jadeja" , "9":"Mohammad Shami" , "10":"Deepak Chahar" , "11":"Jasprith Bumrah"}
{"1":"Aron Finch (Cap)" , "2":"David warner" , "3":"Steve Smith (Cap)" , "4":"Glenn Maxwell" , "5":"Marcus Stoinis" , "6":"Aston Turner" , "7":"Nathan Coulter-Nile" , "8":"Mitchell Starc" , "9":"Adam Zampa" , "10":"Pat Cummins" , "11":"Jason Behrendorff"}

"""

