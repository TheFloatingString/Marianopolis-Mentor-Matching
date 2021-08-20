class Match():

	def __init__(self):
		self.raw_mentor_csv_content = []
		self.raw_mentee_csv_content = []

		self.mentor_names = []
		self.mentee_names = []

		self.score_matrix = []

	def upload_mentor_csv_content(self, mentor_csv_content):
		self.raw_mentor_csv_content = mentor_csv_content


		# extract list of mentor names
		for row in self.raw_mentor_csv_content[1:]:
			self.mentor_names.append(row[5])


	def upload_mentee_csv_content(self, mentee_csv_content):
		self.raw_mentee_csv_content = mentee_csv_content

		# extract list of mentee names
		for row in self.raw_mentee_csv_content[1:]:
			self.mentee_names.append(row[5])

	def generate(self):
		for mentor_row in self.raw_mentor_csv_content[1:]:

			list_for_mentor = []


			for mentee_row in self.raw_mentee_csv_content[1:]:

				score = 0


				# check programs
				if mentor_row[26].lower() == mentee_row[29].lower():
					score += 1

				# check language
				if mentor_row[31]==mentee_row[34] or mentor_row[32]==mentee_row[35] or mentor_row[34]==mentee_row[37]:
					score += 1
				else:
					score += 1

				# check gender
				if mentor_row[36]=="1" or mentee_row[38]=="1":
					if mentor_row[16]==mentee_row[16] and mentor_row[17]==mentee_row[17] and mentor_row[18]==mentee_row[18]:
						score += 1
				else:
					score += 1

				# check activities outside of Marianopolis
				for word in mentor_row[38].lower().split():
					if word in mentee_row[40].lower():
						score += 1
						break

				# check activities at Marianopolis
				for word in mentor_row[40].lower().split():
					if word in mentee_row[42].lower():
						score += 1
						break

				# check hobbies (42)
				for word in mentor_row[42].lower().split():
					if word in mentee_row[44].lower():
						score += 1
						break

				# check if also international student [skipped]

				# add to list for mentor
				list_for_mentor.append(round(score/6, 3))

			self.score_matrix.append(list_for_mentor)



		new_return_matrix = []

		# seting up the first row
		first_row = [""]
		for name in self.mentee_names:
			first_row.append(name)
		new_return_matrix.append(first_row)

		print(len(self.score_matrix))

		# setting up the following rows
		for index in range(len(self.score_matrix)):
			temp_row = self.score_matrix[index]
			temp_row.insert(0,self.mentor_names[index])
			new_return_matrix.append(temp_row)

		return new_return_matrix