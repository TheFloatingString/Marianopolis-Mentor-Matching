import csv


def convert_file_to_matrix(filename):

	with open(filename, "rb") as csvfile:

		csv_reader = csv.reader(csvfile, delimiter=";")

		return list(csv_reader)