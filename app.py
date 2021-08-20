from flask import Flask, render_template, request, send_file
from src import match, file_reading

import csv

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/post_file_upload", methods=["GET", "POST"])
def post_file_upload():
	if request.method == "POST":
		print(request.files)
		file_mentee = request.files["mentee-csv-file"]
		file_mentor = request.files["mentor-csv-file"]

		file_mentee.save("static/uploads/mentee.csv")
		file_mentor.save("static/uploads/mentor.csv")

		match_obj = match.Match()
		match_obj.upload_mentor_csv_content(file_reading.convert_file_to_matrix("static/uploads/mentor.csv"))
		match_obj.upload_mentee_csv_content(file_reading.convert_file_to_matrix("static/uploads/mentee.csv"))

		result = match_obj.generate()

		with open("static/output/final_matching.csv", "w") as outputfile:
			write = csv.writer(outputfile)
			write.writerows(result)

		return send_file("static/output/final_matching.csv")

if __name__ == '__main__':
	app.run(debug=True)