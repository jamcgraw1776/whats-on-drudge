# drudge data 

import urllib.request
import urllib.parse
import re

link_list = []

raw_data = (urllib.request.urlopen('http://www.drudgereport.com'))
raw_text = raw_data.read() #raw_data is unmanipulated raw feed from website
links = re.findall(r'A HREF="(.*?)">',str(raw_text))

count = 0
for lnk in links:
	link_list.append(str(lnk)) #link_list is pull data in a list format 
	count += 1

output_string = '' #output_string is link_list with each element on seperate line
output_string = '\n'.join(link_list)

''
saveFile = open('testsearch.txt','w')
saveFile.write(str(output_string))
saveFile.close()
