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
    index = []
    for string in lines:
        if "makes" in string:
            for e in roster:
                if e in string:
                    if e not in index:
                        index.append(e)
                    if e in index:
                        break
    print 'In the first quarter, the following players made a basket for Golden State: ' + str(index)

GSW_who_scored()

















