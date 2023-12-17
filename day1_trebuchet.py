print("Hello world")

string = '1abc2'
print(string)
#now is as good a time as any to learn regex
import re
#the r'<regularexpression' syntax comes from this suggestion: https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
regx_pattern = r'(\d)'
firstmatch = re.findall(regx_pattern, string)[0]
print(firstmatch)
lastmatch = re.findall(regx_pattern, string)[-1] #this is from a comment in https://stackoverflow.com/questions/33232729/how-to-search-for-the-last-occurrence-of-a-regular-expression-in-a-string-in-pyt
print(lastmatch)
