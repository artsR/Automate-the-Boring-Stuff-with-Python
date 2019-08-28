import re

text = 'VERB '
changeRegex = re.compile(r'VERB(\.)?')
mo = changeRegex.sub(r'fucks\1', text)
print(mo)

agentNameRegex = re.compile(r'Agent (\w)\w*')
mo = agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)

data = ['Agent Alice', 'Agent Carol', 'Agent Eve', 'Agent Bob']
dataRegex = re.compile(r' \w*')
mo = dataRegex.search(data)
print(mo)
