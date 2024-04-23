import re

re.findall("ab*c", "ac")
# ['ac']

re.findall("ab*c", "abcd")
# ['abc']

re.findall("ab*c", "acc")
# ['abc', 'ac']

re.findall("ab*c", "abcac")
# ["abc", "ac"]

re.findall("ab*c", "abdc")
# []

re.findall("ab*c", "ABC", re.IGNORECASE)
# ['ABC']

re.findall("a.c", "abc")
["abc"]

re.findall("a.c", "abbc")
[]

re.findall("a.c", "ac")
[]

re.findall("a.c", "acc")
["acc"]


# re.sub(), which is short for substitute, allows you to replace text in a string that matches a regular expression with new text.
string = "Everything is <replaced> if its in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
string
#'Everything is ELEPHANTS.'


# The arguments passed to re.sub() are the regular expression, followed by the replacement text, followed by the string.
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
string
"Everything is ELEPHANTS."


# Alternatively, you can use the non-greedy matching pattern *?
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
string
"Everything is ELEPHANTS if it's in ELEPHANTS."
