import os
import pprint
import re

# Parse the file and create a dictionary of all the players mapped to how much they score.
# Note that you'll have to handle several cases to do this correctly. I won't specify what those cases are.
# Part of the exercise is to figure out those cases yourself.
# Your function should return something like
# {'Kevin Durant': 15, 'Andre Iguodala': 0}. 
# I didn't include all the players but you get the idea. You should include any player who didn't score as having zero points.
# A good strategy would be create a starting dictionary where every player has 0 points, then loop through the play by play string and
# add points accordingly. 

roster = ('Kevin Durant', 'Klay Thompson', 'David West', 'Damian Jones', 'JaVale McGee',
          'Matt Barnes', 'Ian Clark', 'Stephen Curry', 'Draymond Green', 'Andre Iguodala', 'Shaun Livingston',
          'Kevon Looney', 'James Michael McAdoo', 'Patrick McCaw', 'Zaza Pachulia')

filename = 'lal-vs-gsw-412-quarter1.txt'

os.chdir('D:\\Users\\Kenny\\Desktop\\kenny-fun\\nba_fun')
print os.getcwd()
lines = open(filename, 'r').readlines()
# lines = '\n'.join(lines)
# print lines

players_stats = {}
for key in range(len(roster)):
    players_stats[roster[key]] = 0
dwest = str(roster[2])
for key in players_stats:
    if key == dwest:
        players_stats[key] = 67
        if players_stats[key] == 67:
            players_stats[key] += 33
    if key == roster[0]:
        players_stats[key] += 2
    if 'a' in key[1].lower():
        players_stats[key] += 3
    if 'curry' in key.lower():
        players_stats[key] += 30

thirty = []
for e in lines:
    digits = re.findall(r'\d+-', e)
    print digits
# for e in digits:
#     numbers = re.findall(r'\d+', digits)
# print digits

# results = map(int, numbers)

# for numberz in results:
#     if numberz > 25: #need to find what length three point line is
#         thirty.append(numberz)

# pprint.pprint(thirty)
    # if "makes" in e:
    #     print e



# dict[] = 2
# pprint.pprint(players_stats)

def get_roster_stats():
    # Your code here
    pass

pprint.pprint(get_roster_stats())
