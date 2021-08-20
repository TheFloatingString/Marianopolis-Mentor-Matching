import csv
import codecs

with codecs.open("static/Mentee_Sign_Up_Form_Peer_Mentor_Program.csv", "r") as csvfile:

	csvreader = csv.reader(csvfile, delimiter=';')

	for row in csvreader:
		print(row)

