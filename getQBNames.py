from sportsreference.nfl.teams import Teams
from datetime import datetime
import pandas as pd

start = datetime.now()

for i in range(2000,2020):
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
        allQbs.to_csv("qbs_" + year + ".csv")
        

end = datetime.now()
totalTime = end-start
print(totalTime)
