from sportsreference.nfl.roster import Player
import pandas
    # dataframe that stores info from csv file
df = pandas.read_csv('test.csv')

    #loop to write player dataframe to csv
for index, row in df.iterrows():
    name = (row['Names'])
    player = Player(name)
    playerdf = player.dataframe
    playerdf.to_csv(name+'.csv')












