class Match():

	def __init__(self):
		self.raw_mentor_csv_content = []
		self.raw_mentee_csv_content = []

		self.mentor_names = []
		self.mentee_names = []
		
		self.mentor_ids = []
		self.mentee_ids = []

		self.score_matrix = []

	def upload_mentor_csv_content(self, mentor_csv_content):
		self.raw_mentor_csv_content = mentor_csv_content


		# extract list of mentor names
		for row in self.raw_mentor_csv_content[1:]:
			self.mentor_names.append(row[5])
			self.mentor_ids.append(row[6])


	def upload_mentee_csv_content(self, mentee_csv_content):
		self.raw_mentee_csv_content = mentee_csv_content

		# extract list of mentee names
		for row in self.raw_mentee_csv_content[1:]:
			self.mentee_names.append(row[5])
			self.mentee_ids.append(row[6])


	def generate(self):
		for mentor_row in self.raw_mentor_csv_content[1:]:

			list_for_mentor = []


			for mentee_row in self.raw_mentee_csv_content[1:]:

				score = 0


				# check programs (more weight)
				if mentor_row[7].lower() == mentee_row[7].lower():
					score += 1

				# check language
				if mentor_row[31]==mentee_row[35] or mentor_row[32]==mentee_row[36] or mentor_row[34]==mentee_row[38]:
					score += 1
				else:
					score += 1

				# check gender (give score of 0 if there is a preference)
				if mentor_row[36]=="1" or mentee_row[39]=="1":
					if mentor_row[16]==mentee_row[17] and mentor_row[17]==mentee_row[18] and mentor_row[19]==mentee_row[20]:
						score += 1
				else:
					score += 1

				# check activities outside of Marianopolis
				for word in mentor_row[38].lower().split():
					if word in mentee_row[41].lower():
						score += 1
						break

				# check activities at Marianopolis
				for word in mentor_row[40].lower().split():
					if word in mentee_row[43].lower():
						score += 1
						break

				# check hobbies (42)
				for word in mentor_row[42].lower().split():
					if word in mentee_row[45].lower():
						score += 1
						break

				# check if also international student [skipped]

				# add to list for mentor
				list_for_mentor.append(round(score/6, 3))

			self.score_matrix.append(list_for_mentor)

		new_return_matrix = []

		# seting up the first row
		first_row = ["",""]
		for name in self.mentee_names:
			first_row.append(name)
		new_return_matrix.append(first_row)

		# setting up the second row
		second_row = ["", ""]
		for mentee_id in self.mentee_ids:
			second_row.append(mentee_id)
		new_return_matrix.append(second_row)

		print(len(self.score_matrix))

		# setting up the following rows
		for index in range(len(self.score_matrix)):
			temp_row = self.score_matrix[index]
			temp_row.insert(0,self.mentor_names[index])
			temp_row.insert(1, self.mentor_ids[index])
			new_return_matrix.append(temp_row)


		return new_return_matrix


	def return_indices_of_top(self, target_list, top_n):
		return sorted(range(len(target_list)), key=lambda i: target_list[i])[-top_n:]


	def return_top_mentors_for_mentees(self, n=5):

		return_dict = {"results":[]}


		# print(len(self.score_matrix))
		# print(len(self.mentor_names))

		# print(len(self.score_matrix[0]))
		# print(len(self.mentee_names))

		# for row in self.score_matrix:
		# 	print(row)

		# print("Done!")

		# raise KeyError

		for index in range(len(self.score_matrix[0])-2):

			mentor_values_list = [x[index+2] for x in self.score_matrix]
			top_indices = self.return_indices_of_top(mentor_values_list, n)

			# print(self.mentor_ids)

			top_mentors = [self.mentor_names[top_index] + " " + self.mentor_ids[top_index] for top_index in top_indices]

			# print(top_mentors)
			# print(index)

			# print(len(self.score_matrix))
			# print(len(self.score_matrix[0]))
			# print(len(self.mentee_names))

			return_dict["results"].append({self.mentee_names[index]+" "+self.mentee_ids[index]: top_mentors})

		return return_dict

