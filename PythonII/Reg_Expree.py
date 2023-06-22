import re

# split_term = "a"

# text = "This is a string with term1 and term2"

    
# match = re.search("a", text)
# print(match.start())
# print(re.split(split_term,text))

# text = re.findall("phrase", "test phrase match in the match middle")
# print(text)

import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print(f"Searching for pattern {pat}")
        print(re.findall(pat, phrase))
        print("\n")
        

test_phrase = "sdsd..sssdddd..sdddsddd...dsds...dssssss...sddddd"

test_patterns = ["sd+"] # * for 0 or more d / ? 0 or 1 d/ {3} 3 d, to specify the number/ {2,3} to or 3 d/ + for 1 or more d/ s[sd]+ for s followed by one or more s or d

# to remove symbols from a text: ["[^!.?]+"]. The symbols to be removed come after the ^ sign. The + sign stands for "more"
#["[a-z]+"] sequence of lower case chars
#["[A-Z]+"] sequence of upper case chars
#[r"\d+"]

multi_re_find(test_patterns, test_phrase)