student_dict = {"student": ["Angela", "James", "Lilly"], "score": [56, 76, 98]}

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# #loop through dataframe
# for (key, value) in student_dataframe.items():
#     print(value)

# Loop through rows of a data frame
for index, row in student_dataframe.iterrows():
    print(row)
