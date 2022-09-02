import fountainplus
import sys

import csv
from collections import Counter

breakdown = 0
shotlist = 0
fountainfile = ''

# get parameter settings

for idx, arg in enumerate(sys.argv):
	#print(arg)
	if idx == 1:
		fountainfile = arg
	if idx >1:
		if arg =='--breakdown':
			breakdown = 1
		if arg =='--shotlist':
			shotlist = 1



# load fountain file

d = open(fountainfile, 'r')
work_with_me = d.read()
d.close()


this_text = work_with_me



# make it a fountain object
F = fountainplus.Fountain(this_text)



res = list(Counter(F.characters).items())



header = ['CAST', 'Dialogue Frequency']

with open('cast.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerows(res)
	#writer.close()
	f.close
print('cast.csv created')



if breakdown ==1:

	header = F.csvheader
	data = F.csvrow

	data.sort(key=lambda x: (x[5], x[6], x[7]))

	with open('breakdownsummary.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(header)
		writer.writerows(data)
		#writer.close()
		f.close

	print('breakdownsummary.csv created')

if shotlist == 1:

	header = F.shotheader
	data = F.shotrow
	with open('shotlist.csv', 'w', encoding='UTF8', newline='') as s:
		writer = csv.writer(s)

		# write the header
		writer.writerow(header)

		# write multiple rows
		writer.writerows(data)

	print('shotlist.csv created')



		
