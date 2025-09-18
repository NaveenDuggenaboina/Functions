#Program for obtaining alphabets, symbols and digits
#FilterEx5.py
value = "P2yt$1h4#o*3n" # here value of <class,str> and is iterabel object
alpha=list(filter(lambda ch:ch.isalpha(),value))
digits=list(filter(lambda ch:ch.isdigit(),value))
symbols=list(filter(lambda ch: not ch.isalnum(),value))
print(symbols)