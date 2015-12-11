# get tons of user_agent
import re
import requests

html = requests.get('http://www.useragentstring.com/pages/All/').content.decode('iso-8859-15')

ua_pattern = re.compile(r"<a href='/.+?_id_\d+\.php'>(.+?)</a>")

results = ua_pattern.findall(html)
print(results)
with open('results.py', 'w') as s:
	s.write('[\n')
	for item in results:
		s.write("'{}',\n".format(item))
	s.write(']')
