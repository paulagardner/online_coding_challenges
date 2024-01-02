#now is as good a time as any to learn regex:
#now is as good a time as any to learn regex:
#reference:
#for list comprehension: https://stackoverflow.com/questions/15233340/getting-rid-
of-n-when-using-readlines
#for argparser help: https://stackoverflow.com/questions/18862836/how-to-open-file
-using-argparse
print(list)
#the r'<regularexpression' syntax comes from this suggestion: https://stackoverflo
w.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
regx_pattern = '(\d|one|two|three|four|five|six|seven|eight|nine)'
def text_to_integer():
        number_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five
': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10'} #make a
dictionary that contains all the maps
        test = 'two'
        if test in number_mapping:
                converted_integer = number_mapping[test]
                return converted_integer
        else:
                return match #else case for if the match is already an integer
print(text_to_integer())
calibration_values = []
#for line in list:
        #firstmatch = re.findall(regx_pattern, line)[0]
        #lastmatch = re.findall(regx_pattern, line[-1] #this is from a comment in
https://stackoverflow.com/questions/33232729/how-to-search-for-the-last-occurrence
-of-a-regular-expression-in-a-string-in-pyt
        #re.sub( #https://flexiple.com/python/python-regex-replace
        #calibration_values.append((f'{firstmatch}{lastmatch}'))
        #print(text_to_integer(firstmatch))
#print(calibration_values)
#this works correctly, perhaps regex replace https://learn.microsoft.com/en-us/dot
net/api/system.text.regularexpressions.regex.replace?view=net-8.0
#print(sum(calibration_values))
~
"day1_trebuchet.py" 44L, 1912C written                          30,1          Bot
