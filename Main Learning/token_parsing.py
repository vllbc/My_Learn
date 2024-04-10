import re
from collections import namedtuple
text = "foo = 23+42*10"

Token = namedtuple('Token', ['type', 'value'])

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# scanner = master_pat.scanner(text)

# for t in iter(scanner.match, None):
#     tok = Token(t.lastgroup, t.group())
#     print(tok)
# print(master_pat.findall(text))
import string
trans = string.maketrans()
print(trans)