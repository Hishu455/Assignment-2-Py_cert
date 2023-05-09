Regex_Pattern = r'^[1-3]{1}[0-2]{1}[0,x,s]{1}[0,3,A,a]{1}[x,s,u]{1}[.,,]{1}$'


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())