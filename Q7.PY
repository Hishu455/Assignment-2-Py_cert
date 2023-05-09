Regex_Pattern = r"^[0-9]{1}[a-zA-Z0-9]{4}[.]{1}$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())