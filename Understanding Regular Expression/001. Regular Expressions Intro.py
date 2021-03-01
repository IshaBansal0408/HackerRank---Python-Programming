# Importing re module
import re

"""
            STUDYING re.search()
re.search() is used to match a pattern against a string
re.search(<pattern>,<string>)
    span=(a,b) indicates where the match was found.
    match=___ indicates which characters are matched.
"""

# Simple Search
print("SIMPLE SEARCH")
string="Isha123Dabbu"
pattern="123"
print(re.search(pattern,string))

print("""
INFORMATION :
span=(a,b) indicates where the match was found.
match=___ indicates which characters are matched.""")

print("""
OTHER INFO ABOUT re PATTERNS:
[] --> class of characters
    [0-9]-Matches any single decimal digit character btw 0 and 9
    [a-z]-Any btw a and z
    [A-Z]-Any btw A and Z
    [abc]-Matches any of the characters mentioned 'a','b' or 'c'
. --> dot character
    a.b-Matches a and then one character except \n and then b
^ or \A--> Matches starting of string or complement a [] class
$ or \Z--> Matches end of the string
+ --> a+ matches one or more occurence of a
* --> a* matches 0 or more occurence of a
? --> a? matches 0 or 1 occurence of a
\w --> Matches any word character
            uppercase
            lowercase
            digits
            underscore
\W --> Matches any non-word character
\d --> Any decimal digit
\D --> non-decimal digit
\s --> Any whitespace character
            space
            tab
\S --> not whitespace character
<char>{<no>} --> matches exactly 'no' amount of char
<char>{a,b} --> matches exactly btw a and b amount of char
""")

