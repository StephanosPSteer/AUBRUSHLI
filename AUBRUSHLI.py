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
	g= parser.add_argument_group()
	g.add_argument(
        "-i",
        "--inputfile",
	metavar='Load Fountain File',
        required=True,
        help="Fountain File",
	widget='FileChooser'
    )
	# parser.add_argument(
    #      "--castlist",
	#  metavar='Cast List',
    #      action='store_true',
    #      help="create a cast list"
    # )
	# parser.add_argument('--cast_out_file',
	# 					metavar='Save Cast List',
	# 					#action='store_true',
	# 					widget='FileSaver')
	# parser.add_argument(
    #     "--breakdownsummary",
	# metavar='Breakdown Summary',
	# action='store_true',
    #     help="create a breakdown summary"
    # )
	# parser.add_argument('--break_out_file',
	# 					metavar='Save Breakdown Summary',
	# 					#action='store_true',
	# 					widget='FileSaver')
	# parser.add_argument(
    #     "--shotlist",
	# metavar='Shot List',
	# action='store_true',
    #     help="create a shotlist"
    # )
	# parser.add_argument('--shot_out_file',
	# 					metavar='Save Shot List',
	# 					#action='store_true',
	# 					widget='FileSaver')
	cast = g.add_mutually_exclusive_group(gooey_options={
            'title': "Cast List"
        })
	cast.add_argument('--cast_out', metavar='Save Cast List',
					  help='Select where to save Cast List',
					  widget='FileSaver',
					  gooey_options=dict(
						  wildcard="CSV (.csv)|*.csv", full_width=True
					  ))
	breakd = g.add_mutually_exclusive_group(gooey_options={
		'title': "Breakdown Summary"
	})
	breakd.add_argument('--break_out', metavar='Save Breakdown Summary',
					  help='Select where to save Breakdown Summary', widget='FileSaver',
					  gooey_options=dict(
						  wildcard="CSV (.csv)|*.csv", full_width=True))
	shot = g.add_mutually_exclusive_group(gooey_options={
		'title': "Shot List"
	})
	shot.add_argument('--shot_out', metavar='Save Shot List',
					  help='Select where to save Shot List', widget='FileSaver',
					  gooey_options=dict(
						  wildcard="CSV (.csv)|*.csv", full_width=True,))

	args = parser.parse_args()
	
	# load fountain file

	d = open(args.inputfile, 'r')
	work_with_me = d.read()
	d.close()

	this_text = work_with_me

	# make it a fountain object
	F = fountainplus.Fountain(this_text)
	
	#if args.castlist:
	if args.cast_out:
		res = list(Counter(F.characters).items())

		header = ['Cast Name', 'Dialogue Frequency']
		output_cast = args.cast_out

		#with open('cast.csv', 'w', encoding='UTF8', newline='') as f:
		with open(output_cast, 'w', encoding='UTF8', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(header)
			writer.writerows(res)
			#writer.close()
			f.close
		print('castlist created')



	if args.break_out:

		header = F.csvheader
		data = F.csvrow

		data.sort(key=lambda x: (x[5], x[6], x[7]))
		output_break = args.break_out

		with open(output_break, 'w', encoding='UTF8', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(header)
			writer.writerows(data)
			f.close

		print('breakdown summary created')

	if args.shot_out:

		header = F.shotheader
		data = F.shotrow
		output_shot = args.shot_out
		with open(output_shot, 'w', encoding='UTF8', newline='') as s:
			writer = csv.writer(s)

			# write the header
			writer.writerow(header)

			# write multiple rows
			writer.writerows(data)

		print('shotlist created')



if __name__ == "__main__":
    main()



		




		



		
