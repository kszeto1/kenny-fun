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


player_scores = {}
for player in roster:
    player_scores[player] = 0


roster_regex = '(' + ('|'.join(roster)) + ')'


one_point_regex = roster_regex + " makes free"
two_point_regex = roster_regex + " makes (two point|layup|driving dunk|tip|\d+\-foot jumper|\d+\-foot two point)"
three_point_regex = roster_regex + " makes \d+\-foot three point"


def get_roster_stats():
    for play in play_by_play:
        one_point_scored = (re.search(one_point_regex, play))
        two_point_scored = (re.search(two_point_regex, play))
        three_point_scored = (re.search(three_point_regex, play))
        if one_point_scored:
            print 'Match found: ', one_point_scored.group()
            extracted_player = one_point_scored.group(1)
            player_scores[extracted_player] += 1
        elif two_point_scored:
            print 'Match found: ', two_point_scored.group()
            extracted_player = two_point_scored.group(1)
            player_scores[extracted_player] += 2
        elif three_point_scored:
            print 'Match found: ', three_point_scored.group()
            extracted_player = three_point_scored.group(1)
            player_scores[extracted_player] += 3
        else:
            print 'No match', play

    pprint.pprint(player_scores)

get_roster_stats()

