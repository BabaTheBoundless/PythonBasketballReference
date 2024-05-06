#teams imports
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
#players imports
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot

#player has 31 total parameters

GSW_roster = get_roster("GSW", 2016)
Steph_Curry = get_stats('Stephen Curry', 'PER_GAME', False, False)
first_player = GSW_roster.iloc[0]
#print(GSW_roster)
#print(Steph_Curry)
Steph_Curry_Points = Steph_Curry[['SEASON','PTS', 'TRB', 'AST']]
print(Steph_Curry_Points)

