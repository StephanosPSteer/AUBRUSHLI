import fountainplus
import sys

import csv
from collections import Counter
from argparse import ArgumentParser
from gooey import Gooey
from gooey import GooeyParser

cast=0
breakdown = 0
shotlist = 0
fountainfile = ''

@Gooey(header_show_title=True, header_show_subtitle=True, menus=True, program_name='Aubrushli', menu=[{'name': 'Help', 'items':
	 [{
		 'type': 'AboutDialog',
		 'menuTitle': 'About Aubrushli'
		 ,
		 'name': 'Aubrushli',
		 'description': 'A simple app to read and extract production information from screenplays',
		 'version': '1.0',
		 'copyright': '2022',
		 'website': 'https://github.com/StephanosPSteer/AUBRUSHLI',
		 'developer': 'Stefanos Christofi',
		 'license': 'MIT'
		 }]
		 }]
)
def main():
	# parser = ArgumentParser()
	#mac version
	parser = GooeyParser(description="By Stefanos Christofi  \nE:stefanoschristofi@yahoo.com")
	#windows version
	#parser = GooeyParser()
	parser.add_argument(
        "-i",
        "--inputfile", 
        required=True,
        help="Fountain File",
		widget='FileChooser'
    )
	parser.add_argument(
         "-castlist",
        #  "--cast",
		 action='store_true',
        # required=False,
        help="create a cast list"
    )
	parser.add_argument(
        "-breakdownsummary",
		action='store_true',
        # "--breakdown_summary",
        # required=False,
        help="create a breakdown summary"
    )
	parser.add_argument(
        "-shotlist",
		action='store_true',
        # "--shotlist",
        # required=False,
        help="create a shotlist"
    )
	args = parser.parse_args()
	


# get parameter settings

	# for idx, arg in enumerate(sys.argv):
	# 	#print(arg)
	# 	if idx == 1:
	# 		fountainfile = arg
	# 	if idx >1:
	# 		if arg =='--cast':
	# 			cast = 1
	# 		if arg =='--breakdown':
	# 			breakdown = 1
	# 		if arg =='--shotlist':
	# 			shotlist = 1



	# load fountain file

	d = open(args.inputfile, 'r')
	work_with_me = d.read()
	d.close()


	this_text = work_with_me



	# make it a fountain object
	F = fountainplus.Fountain(this_text)
	#for et in F.elements(FountainElement('Boneyard')): 
	#print(F.elements[0])
	# for ele in F.elements:
		#if 'Boneyard:' in ele:
		# print(ele)
			

	if args.castlist:
		res = list(Counter(F.characters).items())

		header = ['Cast Name', 'Dialogue Frequency']

		with open('cast.csv', 'w', encoding='UTF8', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(header)
			writer.writerows(res)
			#writer.close()
			f.close
		print('cast.csv created')



	if args.breakdownsummary:

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

	if args.shotlist:

		header = F.shotheader
		data = F.shotrow
		with open('shotlist.csv', 'w', encoding='UTF8', newline='') as s:
			writer = csv.writer(s)

			# write the header
			writer.writerow(header)

			# write multiple rows
			writer.writerows(data)

		print('shotlist.csv created')



if __name__ == "__main__":
    main()



		
