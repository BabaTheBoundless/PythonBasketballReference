#teams imports
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
#players imports
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
#graph plotting
import matplotlib.pyplot as plt



#player has 31 total parameters
#GSW_roster = get_roster("GSW", 2016)
Steph_Curry = get_stats('Stephen Curry', 'PER_GAME', False, False)
#first_player = GSW_roster.iloc[0]
#print(GSW_roster)
#print(Steph_Curry)
Steph_Curry_Seasons = Steph_Curry['SEASON']
Steph_Curry_Points = Steph_Curry['PTS']
Steph_Curry_Rebounds = Steph_Curry['TRB']
Steph_Curry_Assists = Steph_Curry['AST']

#print(Steph_Curry_Assists)

#Plotting the stats
plt.figure(figsize=(10, 6))
plt.plot(Steph_Curry_Seasons, Steph_Curry_Points, label='Points')
plt.plot(Steph_Curry_Seasons, Steph_Curry_Rebounds, label = 'Rebounds')
plt.plot(Steph_Curry_Seasons, Steph_Curry_Assists, label = "Assists")
#labels and title
plt.xlabel('Season')
plt.ylabel('Stats')
plt.title('Steph Curry Stats')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45) #rotate x-axis
plt.tight_layout()

plt.show()




