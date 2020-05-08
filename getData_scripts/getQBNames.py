from sportsreference.nfl.teams import Teams
from datetime import datetime
import pandas as pd
import os

start = datetime.now()

for i in range(2017,2020):
    year = str(i)
    teams = Teams(year)
    qbs = [[(player._name,player._player_id,player._position,) for player in team.roster.players] for team in teams._teams]
    allQbs = pd.DataFrame(columns = ['Name', 'player_id', 'position'])
    for i in qbs:
        players_df = pd.DataFrame(i, columns = ['Name', 'player_id', 'position'])
        players_df = players_df.dropna()
        mask = players_df['position'].apply(lambda x: 'qb' in x or 'QB' in x)
        qb_df = players_df[mask]
        allQbs = allQbs.append(qb_df)
        allQbs.to_csv("../data/QB_names/qbs_" + year + ".csv")
        


allqb_df = pd.DataFrame(columns = ['Name', 'player_id', 'position'])
lis = []
for i in range(1999,2020):
    current = pd.read_csv('qbs_'+str(i)+'.csv')
    allqb_df= allqb_df.append(current)

allqb_df_unique = allqb_df.drop_duplicates(subset='player_id')

allqb_names = allqb_df_unique.drop(columns=['Unnamed: 0','position'])

allqb_names.to_csv('../data/QB_names/all_qb_names.csv')
