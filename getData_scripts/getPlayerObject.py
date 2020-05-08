from sportsreference.nfl.roster import Player
import pandas
    # dataframe that stores info from csv file
df = pandas.read_csv('../data/QB_names/all_qb_names.csv')

    #loop to write player dataframe to csv
for index, row in df.iterrows():
    name = (row['player_id'])
    player = Player(name)
    playerdf = player.dataframe
    playerdf.to_csv('../data/QB_data' + name+'.csv')












