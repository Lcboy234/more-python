# names = ["dfsadwe", "dqwed", "fwerf", "cwewdcwe", "fwfwe", "bmktlk", "vnerjvn"]

# import random
# new_dict = {student:random.randint(1, 100) for student in names}

# passed_students = {student:score for (student, score) in new_dict.items() if score >= 70}
# print(passed_students)

student_dict = {
    "student": ["Kai", "Kai2", "Kai3"],
    "score": [58, 77, 95]
}

# for (key, value) in student_dict.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Kai2":
        print(row.score)