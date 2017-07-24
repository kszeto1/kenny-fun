import os
import pprint

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

def get_roster_stats():
    # Your code here
    pass

pprint.pprint(get_roster_stats())
