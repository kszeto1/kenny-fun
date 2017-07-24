import os

# Parse the file and figure out who scored in the first quarter from the golden state team

roster = ('Kevin Durant', 'Klay Thompson', 'David West', 'Damian Jones', 'JaVale McGee',
          'Matt Barnes', 'Ian Clark', 'Stephen Curry', 'Draymond Green', 'Andre Iguodala', 'Shaun Livingston',
          'Kevon Looney', 'James Michael McAdoo', 'Patrick McCaw', 'Zaza Pachulia')

filename = 'lal-vs-gsw-412-quarter1.txt'

os.chdir('D:\\Users\\Kenny\\Desktop\\kenny-fun\\nba_fun')
print os.getcwd()
lines = open(filename, 'r').readlines()

def GSW_who_scored():
    players_who_have_scored = []
    for play_by_play_string in lines:
        if "makes" in play_by_play_string:
            for player in roster:
                if player in play_by_play_string:
                    if player not in players_who_have_scored:
                        players_who_have_scored.append(player)
                    if player in players_who_have_scored:
                        break
    print 'In the first quarter, the following players made a basket for Golden State: ' + str(players_who_have_scored)

GSW_who_scored()
