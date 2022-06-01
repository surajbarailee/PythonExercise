# Hard Keywords and Soft Keywords
# The difference between hard and soft keywords is that hard keywords are always reserved words, even in positions
# where they make no sense (e.g. x = class + 1), while soft keywords only get a special meaning in context.
# Some identifiers are only reserved under specific contexts. These are known as soft keywords. The identifiers match, case and _ can syntactically act as keywords in contexts related to the pattern matching statement, but this distinction is done at the parser level, not when tokenizing.


import keyword

print(keyword.kwlist)
print(keyword.iskeyword("for"))
print(keyword.softkwlist)


# Case and match are soft keyword


# Soft keywords are, IIUC, a side effect of the PEG parser being a backtracking parser.
# A token can be identifier in attempt at parsing, but a keyword in another.
# PEP-622 provides the example match [x,y]:. match would first be parsed as an identifier, until the : is encountered, at which point the parse would fail.
# It then backtracks and tries the alternative of parsing match as a keyword. – chepner.

# You can use soft keywords as normal variables.
# That said, just because you can doesn't mean you should.
# Using something that could be a keyword but isn't in based on context is likely to be confusing to whoever has to look at the code later
