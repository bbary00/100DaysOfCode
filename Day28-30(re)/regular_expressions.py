import re

"""
text = 'Awesome, I am doing the #100DaysOfCode challenge'

re.search(r'I am', text)
<_sre.SRE_Match at 0x7f18b0b0c100>

re.match(r'I am', text)
nothing because from start to end

re.match(r'Awesome.*challenge', text)
<_sre.SRE_Match at 0x7f18b0b0c098>

hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

m = re.match(r'.*(#\d+DaysOfCode).*', hundred)
m.groups()[0]
"""