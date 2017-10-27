import re

a = 'Roger Federer is the greatest'
b = 'Rafael Nadal is the greatest'
c = 'Piyush Gupta is the greatest'

# Clearly, I'm not he greatest and I want the regular expression to account for that
regex_search = '(Roger Federer|Rafael Nadal) is the greatest'

# Using only re.search
print(re.search(regex_search, a) != None) # True
print(re.search(regex_search, b) != None) # True
print(re.search(regex_search, c) != None) # False

#However the above way is messy. You could also do it this way

pre_compiled_regex = re.compile(regex_search)
print(pre_compiled_regex.search(a) != None) # True
print(pre_compiled_regex.search(b) != None) # True
print(pre_compiled_regex.search(c) != None) # False
