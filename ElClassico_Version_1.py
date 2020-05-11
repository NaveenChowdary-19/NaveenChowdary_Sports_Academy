import random

Real_Madrid_Squad_List = []

Barcelona_Squad_List = []

Match_Squad = []



Required_Minutes_Real = []
for minute in range(0, 5):
    x = random.randint(0, 90)
    Required_Minutes_Real.append(x)

Required_Minutes_Real = sorted(Required_Minutes_Real, reverse=True)

Required_Minutes_Barca = []
for minute in range(0, 5):
    x = random.randint(0, 90)
    Required_Minutes_Barca.append(x)

Required_Minutes_Barca = sorted(Required_Minutes_Barca, reverse=True)

print(Required_Minutes_Real)
print(Required_Minutes_Barca)


#=================================================================================================================================

class Football:

    def __init__(self, Squad, Minutes, Squad_List):

        self.Goal = random.choice(Squad_List)  # Squad["7"]

        print(self.Goal)

        self.Yellow_Card = random.choice(Squad_List)  # Squad["4"]

        self.Red_Card = random.choice(Squad_List)  # Squad["2"]

        self.Assist = random.choice(Squad_List)  # Squad["5"]

        self.Minutes = Minutes

        self.Goals = random.randint(2, 4)

        self.Passes = self.Minutes * 2

        self.Real_Madrid_Team_Passes = self.Minutes * 9

        self.Barcelona_Team_Passes = self.Minutes * 8

        self.Fouls = self.Minutes // 8

        self.Free_Kicks = random.randint(5, 8)

        self.Corner_Kicks = random.randint(4, 6)

        self.Shots_On_Target = random.randint(5, 8)

        self.Total_Shots = random.randint(11, 14)

        self.Real_Madrid_Goals = random.randint(3, 5)

        self.Barcelona_Goals = random.randint(2, 4)

        try:
            self.Minutes <= 0 and self.Minutes >= 90

        except ValueError:
            print("Arey Burra Thakkuva Yadava... Given Minutes Are Out Of Game Time.. So Please Give The  Time Which Is In Between  Game Time Ra Gutle ga")




    def Real_Madrid_Stats(self):

        for stat_minute in range(self.Minutes):
            if stat_minute == Required_Minutes_Real[0]:
                print(" ", end="\n\n")
                print("{:>45}{}'".format(" ", Required_Minutes_Real[0]))
                print("{:>45} ".format(" ") + Real_Madrid.Goal, end="\n" + "{:>45}".format(" ") + Real_Madrid.Assist)

            if stat_minute == Required_Minutes_Real[1]:
                print(" ", end="\n\n")
                print("{:>45}{}'".format(" ", Required_Minutes_Real[1]))
                print("{:>45}".format(" ") + Real_Madrid.Yellow_Card)

            if stat_minute == Required_Minutes_Real[2]:
                print(" ", end="\n\n")
                print("{:>45}{}'".format(" ", Required_Minutes_Real[2]))
                print("{:>45}".format(" ") + Real_Madrid.Red_Card)

            if stat_minute == Required_Minutes_Real[3]:
                print(" ", end="\n\n")
                print("{:>45}{}'".format(" ", Required_Minutes_Real[3]))
                print("{:>45} ".format(" ") + Real_Madrid.Goal, end="\n" + "{:>45}".format(" ") + Real_Madrid.Assist)

            if stat_minute == Required_Minutes_Real[4]:
                print(" ", end="\n\n")
                print("{:>45}{}'".format(" ", Required_Minutes_Real[4]))
                print("{:>45}".format(" ") + "Own Goal", end="\n" + "{:>45}".format(" ") + Barcelona.Yellow_Card)

            # def Barcelona_Stats(self):

            # for stat_minute in range(self.Minutes):
            if stat_minute == Required_Minutes_Barca[0]:
                print(" ", end="\n\n")
                print("{:>72}{}'".format(" ", Required_Minutes_Barca[0]))
                print("{:>72}".format(" ") + Barcelona.Goal, end="\n" + "{:72}".format(" ") + Barcelona.Assist)

            if stat_minute == Required_Minutes_Barca[1]:
                print(" ", end="\n\n")
                print("{:>72}{}'".format(" ", Required_Minutes_Barca[1]))
                print("{:>72}".format(" ") + Barcelona.Yellow_Card, end="\n")

            if stat_minute == Required_Minutes_Barca[2]:
                print(" ", end="\n\n")
                print("{:>72}{}'".format(" ", Required_Minutes_Barca[2]))
                print("{:>72}".format(" ") + Barcelona.Red_Card, end="\n")

            if stat_minute == Required_Minutes_Barca[3]:
                print(" ", end="\n\n")
                print("{:>72}{}'".format(" ", Required_Minutes_Barca[3]))
                print("{:>72}".format(" ") + Barcelona.Goal, end="\n" + "{:>72}".format(" ") + Barcelona.Assist)

            if stat_minute == Required_Minutes_Barca[4]:
                print(" ", end="\n\n")
                print("{:>72}{}'".format(" ", Required_Minutes_Barca[4]))
                print("{:>72}".format(" ") + "Own Goal", end="\n" + "{:>72}".format(" ") + Real_Madrid.Yellow_Card)





    def stats_of_The_Match(self):

        # In Team Stats  1. Goals   2. Corner Kicks     3. Free kicks     4. Passes    5. Shots On target    6. Total shots    7. Fouls   8. Red Cards   9. Yellow cards

        print(" ", end="\n\n\n")

        print("{:>60} Stats Of The Match".format(" "))
        print("{:>60}".format(" ") + "=====================", end="\n\n")

        print("{:>52} :== {} :== ".format(" ", self.Real_Madrid_Goals) + "  ||  " + " :==  {}  :== ".format(
            self.Barcelona_Goals))

        print("{:>42} :== Real Madrid :== ".format(" ") + "  ||  " + " :== Barcelona :==")
        print(" ", end="\n\n")

        self.Fouls = random.randint(6, 14)

        self.Yellow_Card = random.randint(2, 4)

        self.Red_Card = random.randint(0, 1)

        print("{:>53}".format(" ") + str(Real_Madrid.Real_Madrid_Goals) +"{:<30}".format("  --*: Goals :*--  ") + str(Barcelona.Goals), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Yellow_Card) + "{:<30}".format("   --*: Yellow Cards :*--  ") + str(Barcelona.Yellow_Card), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Red_Card) + "{:<30}".format("   --*: Red Cards :*--  ") + str(Barcelona.Red_Card), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Fouls) + "{:<30}".format("   --*: Fouls :*--  ") + str(Barcelona.Fouls), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Corner_Kicks) + "{:<30}".format("  --*: Corner_Kicks :*--  ") + str(Barcelona.Corner_Kicks), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Free_Kicks) + "{:<30}".format("  --*: Free_Kicks :*--  ") + str(Barcelona.Free_Kicks), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Shots_On_Target) + "{:<30}".format("  --*: Shots_On_Target :*--  ") + str(Barcelona.Shots_On_Target), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Total_Shots) + "{:<30}".format("  --*: Total_Shots :*--  ") + str(Barcelona.Total_Shots), end="\n\n")

        print("{:>53}".format(" ") + str(Real_Madrid.Real_Madrid_Team_Passes) + "{:<30}".format("  --*: Team_Passes :*--  ") + str(Barcelona.Barcelona_Team_Passes), end="\n\n")





    def Result_Of_Match(self):

        print("{:>53} Result Of The Match BY 'Heineken'".format(" "))
        print("{:>55}".format(" ") + "===============================", end="\n\n")

        print("{:>51} :== {} :== ".format(" ", self.Real_Madrid_Goals) + "  ||  " + " :==  {}  :== ".format(
            self.Barcelona_Goals), end="\n\n")

        print("{:>40}  :== Real Madrid :== ".format(" ") + "  ||  " + " :== Barcelona :==")

        Real_Madrid.Real_Madrid_Stats()

        # Barcelona.Barcelona_Stats()

        Real_Madrid.stats_of_The_Match()

        # Barcelona.stats_of_The_Match()


#===============================================================================================================================================================

class Striker:
    def __init__(self):
        self.Goals = random.randint(1, 2)

        self.shots_on_target = random.randint(4, 6)  # shots_on_target

        self.dribbles = random.randint(6, 8)  # dribbles

        self.total_shots = random.randint(6, 9)  # total_shots

        self.penalty_kicks = random.randint(0, 2)  # penalty_kicks


class Mid_Fielder(Striker):
    def __init__(self):
        super().__init__()

        self.Assists = random.randint(0, 2)  # Assists

        self.Corner_kicks = random.randint(2, 5)  # corner_kicks

        self.free_kicks = random.randint(2, 4)  # free_kicks

        self.crosses = random.randint(1, 4)  # crosses

        self.retrives = random.randint(5, 10)  # retrives


class Deffender(Mid_Fielder):
    def __init__(self):
        super().__init__()

        self.Tackles = random.randint(4, 6)  # stats["Tackles"]

        self.Interceptions = random.randint(7, 10)  # stats["Interceptions"]

        self.Fouls = random.randint(3, 5)  # stats["Fouls"]

        self.Blocks = random.randint(3, 6)  # stats["Blocks"]


class Goal_Keeper(Deffender):
    def __init__(self):
        super().__init__()

        self.Saves = random.randint(1, 4)  # stats["Saves"]

        self.Goals_Awarded = random.randint(0, 3)  # stats["Goals_Awarded"]

        self.clean_sheets = random.randint(0, 1)  # stats["clean_sheets"]

        self.penalty_kicks_saved = random.randint(0, 1)  # stats["penalty_kicks_saved"]


class Player_stats(Goal_Keeper):
    def __init__(self):

        super().__init__()



    def Print_Player_Stats(self):

        if Fav_Player_is not in Match_Squad:
            print("Arey Thuppals Yadava Your Favourite Player -{}- Not In Squad Ra Gutle. He Got Injured Give Another Player Ra Houle ".format(Fav_Player_is))

        else:

            print(" ", end="\n\n\n")

            print("Your Favourite Player -{}- Stats Are ::".format(Fav_Player_is))
            print("====================================================", end="\n\n")

            print("{:<19} {:<25} ".format(" " , "Goals  :--  ") + str(self.Goals), end="\n\n")

            print("{:<19} {:<25}".format(" " , "shots_on_target :--  ") + str(self.shots_on_target), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Dribbles  :--  ") + str(self.dribbles), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Total Shots  :--  ") + str(self.total_shots), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Penalty Kicks  :--  ") + str(self.penalty_kicks), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Assists  :--  ") + str(self.Assists), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Corner_kicks  :--  ") + str(self.Corner_kicks), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Free Kicks  :--  ") + str(self.free_kicks), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Crosses  :--  ") + str(self.crosses), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Retrives  :--  ") + str(self.retrives), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Fouls  :--  ") + str(self.Fouls), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Blocks  :--  ") + str(self.Blocks), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Interceptions  :--  ") + str(self.Interceptions), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Tackles  :--  ") + str(self.Tackles), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Saves  :--  ") + str(self.Saves), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Clean_sheets  :--  ") + str(self.clean_sheets), end="\n\n")

            print("{:<19} {:<25}".format(" " , "Goals_Awarded  :--  ") + str(self.Goals_Awarded), end="\n\n")

            print("{:<19} {:<24}".format(" " , "Penalty_kicks_saved  :--  ") + str(self.penalty_kicks_saved), end="\n\n")


#=================================================================================================================================================================


if __name__ == "__main__":
    import json

    Real_Madrid_Squad = json.loads(input())

    Barcelona_Squad = json.loads(input())

    # {"7":"Cristiano Ronaldo" , "1":"Keylor Navas" , "2":"Sergio Ramos" , "3":"Marcelo" , "4":"Varane" , "5":"Toni Kroos" , "6":"Aaron Ramsey" , "8":"Casemiro" , "9":"Karim Benzma" , "10":"Jamie Vardy" , "11":"Gerath Bale"}
    # {"10":"Lionel Messi" , "1":"Cluadio Bravo" , "3":"Gerard Pique" , "4":"Virgil Vandijk" , "5":"Sergio Roberto" , "2":"David Luiz" , "6":"Robert Levendowski" , "7":"James Rodrguize" , "8":"Paulo Dybala" , "9":"Masuet Ozil" , "11":"Mohammad Salah"}

    Minutes = int(input())

    Fav_Player_is = str(input())

    print(Minutes)
    # print(Fav_Player)

for Keys in Real_Madrid_Squad:
    Real_Madrid_Squad_List.append(Real_Madrid_Squad[Keys])

for Keys in Barcelona_Squad:
    Barcelona_Squad_List.append(Barcelona_Squad[Keys])

Match_Squad = Real_Madrid_Squad_List + Barcelona_Squad_List



# print(" ",end = "\n\n\n")


playing_XI = len(Real_Madrid_Squad_List)

print(" ", end="\n\n\n")

print("{:>10}Real Madrid Playing XI are :".format(" ") + "{:>70}".format(" ") + "Barcelona Playing XI are :")

print("{:>10}===========================".format(" ") + "{:>70}".format(" ") + "===========================",end="\n\n")

for player in range(playing_XI):
    Barca = "{}. {:<30}".format(str(player + 1), str(Barcelona_Squad_List[player]))

    Real = "{}. {:<30} {:<63}".format(str(player + 1), str(Real_Madrid_Squad_List[player]), " ")

    print("{:>11}{}. {:<30} {:<63}".format(" ", str(player + 1), str(Real_Madrid_Squad_List[player]), " "),"{}. {:<30}".format(str(player + 1), str(Barcelona_Squad_List[player])) , end = "\n\n")

    # print(Real, Barca)

print(" ", end="\n\n\n")



Real_Madrid = Football(Real_Madrid_Squad, Minutes, Real_Madrid_Squad_List)

Barcelona = Football(Barcelona_Squad, Minutes, Barcelona_Squad_List)

print(Real_Madrid.Result_Of_Match())



Fav_Player = Player_stats()

print(Fav_Player.Print_Player_Stats())
print(Match_Squad)






'''

{"7":"Cristiano Ronaldo" , "1":"Keylor Navas" , "2":"Sergio Ramos" , "3":"Marcelo" , "4":"Varane" , "8":"Toni Kroos" , "6":"Aaron Ramsey" , "5":"Casemiro" , "9":"Karim Benzma" , "10":"Jamie Vardy" , "11":"Gerath Bale"}
{"10":"Lionel Messi" , "1":"Cluadio Bravo" , "3":"Gerard Pique" , "4":"Virgil Vandijk" , "5":"Sergio Roberto" , "2":"David Luiz" , "9":"Robert Levendowski" , "7":"James Rodrguize" , "8":"Paulo Dybala" , "6":"Masuet Ozil" , "11":"Mohammad Salah"}
90
Cristiano Ronaldo



---How Will You Represents The No Of Goals In Result Of The Match By Players 

---If I Give You a Input Player You Should Print If He is Striker Or Mid Fielder Or Goal Keeper Or Defender And Stats Should COme According to the Payer type And Should 
Match Result Of The Match Stats 
---In Player Stats If He Shot Goals And If He Give Assists And Yellow Cards And All STats Have To Come In Proper Way

---The Substitute Players Should Also Come in Out put As in International Match..
--- And Substitute Players Stats Should Also Come in Out put If User Wants
 
'''
