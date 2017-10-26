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
play_by_play = open(filename, 'r').readlines()
# lines = '\n'.join(lines)
print play_by_play


dict = {}
for player in roster:
    dict[player] = 0
print dict

roster_regex = '(' + ('|'.join(roster)) + ')'
# pattern_players = re.compile(roster_regex)
print roster_regex

def get_roster_stats():
    for play in play_by_play:
        p = re.search(roster_regex + ' makes free ', play)
        if p:
            print 'Match found: ', p.group()
        else:
            print 'No match', play

    # if p and m:
        # dict[e] = 3
        # if dict[e] > 0:
        # dict[p] += 3

get_roster_stats()

# pprint.pprint(get_roster_stats)
