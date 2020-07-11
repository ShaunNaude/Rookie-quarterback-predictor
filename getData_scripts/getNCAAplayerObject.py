from sportsreference.ncaaf.roster import Player
import pandas
     #dataframe that stores info from csv file
df = pandas.read_csv('../data/all_qb_names.csv')

for index, row in df.iterrows():
    num = 1
    name = (row['Name'])
    #string manipulation
    name = name.lower()
    name = name.replace(" ", "-")
    name = name + "-" + str(num)
    player = Player(name)
    while True:

        try:
            if (player.position == "QB"):
                #write player to csv file
                player.dataframe.to_csv("dataFolder/NCAA_player_csv/" + player.name + ".csv")
                print("wriiten")
                break
            else:
                num = num + 1
                name = (row['Name'])
                # string manipulation
                name = name.lower()
                name = name.replace(" ", "-")
                name = name + "-" + str(num)
                player = Player(name)
        except:
              print("Player does not have dataFrame")
              break


    
    
    