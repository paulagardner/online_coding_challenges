#now is as good a time as any to learn regex:
import re
import argparse
parser = argparse.ArgumentParser(description = "takes an input file and makes 
it a variable to use so things aren't hardcoded")
parser.add_argument('filename')
args = parser.parse_args()


list = [line.rstrip() for line in open(args.filename)]
#reference: 
#for list comprehension: https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
#for argparser help: https://stackoverflow.com/questions/18862836/how-to-open-file-using-argparse
print(list)

#the r'<regularexpression' syntax comes from this suggestion: https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python    
regx_pattern = r'(\d)'

calibration_values = []
for line in list:
        firstmatch = re.findall(regx_pattern, line)[0]
        lastmatch = re.findall(regx_pattern, line)[-1] #this is from a comment in https://stackoverflow.com/questions/33232729/how-to-search-for-the-last-occurrence-of-a-regular-expression-in-a-string-in-pyt
        calibration_values.append(int(f'{firstmatch}{lastmatch}'))
        
print(calibration_values)

print(sum(calibration_values))
