import fountainplus
import csv
from collections import Counter
from gooey import Gooey
from gooey import GooeyParser


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
	
	#mac version
	parser = GooeyParser(description="By Stefanos Christofi  \nE:stefanoschristofi@yahoo.com")
	#windows version
	#parser = GooeyParser()
	parser.add_argument(
        "-i",
        "--inputfile",
	metavar='Fountain Screenplay', 
        required=True,
        help="Fountain File",
	widget='FileChooser'
    )
	parser.add_argument(
         "-castlist",
	 metavar='Cast List',
         action='store_true',
         help="create a cast list"
    )
	parser.add_argument(
        "-breakdownsummary",
	metavar='Breakdown Summary',
	action='store_true',
        help="create a breakdown summary"
    )
	parser.add_argument(
        "-shotlist",
	metavar='Shot List',
	action='store_true',
        help="create a shotlist"
    )
	args = parser.parse_args()
	
	# load fountain file

	d = open(args.inputfile, 'r')
	work_with_me = d.read()
	d.close()

	this_text = work_with_me



	# make it a fountain object
	F = fountainplus.Fountain(this_text)

			

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



		
