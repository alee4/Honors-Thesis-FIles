import os
import glob
import pandas as pd

def combind_csv(directory):
	os.chdir(directory)
	print("curr dir is: " + directory)
	extension = ''

	all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

	#print("Num files collected: " + str(len(all_filenames))
	#combine all files in the list
	combined_csv = pd.concat((pd.read_csv(f) for f in all_filenames))

	csv_name = str(directory) + "_combined_csv.csv"

	#export to csv
	combined_csv.to_csv(csv_name, index=False, encoding='utf-8-sig')

	os.chdir('..')

subreddit_list = ["JoeRogan", "walkaway", "WorkReform", "ukraine", "conspiracy", 
                       "Coronavirus", "China_Flu", 
                      "HermanCainAward", "antiwork", "politics", "Conservative", "progressive", "Libertarian"]

list_of_dirs = ["csv1", "csv2"]
#for d in subreddit_list:
#	combind_csv(d)
combind_csv("antiwork")
