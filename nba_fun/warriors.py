
roster = ('Kevin Durant', 'Klay Thompson', 'David West', 'Damian Jones', 'Javale McGee',
          'Matt Barnes', 'Ian Clark', 'Stephen Curry', 'Draymond Green', 'Andre Iguodala', 'Shaun Livingston',
          'Kevon Looney', 'James Michael McAdoo', 'Patrick McCaw', 'Zaza Pachulia')

filename = 'kenny-fun/nba_fun/lal-vs-gsw-412-quarter1.txt'

# Parse the file and figure out who scored in the first quarter from the golden state team

lines = open(filename, 'r').readlines()

for line in lines:
    print(line)
