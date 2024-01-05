##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import os
import smtplib 


# 1. Update the birthdays.csv
new_birthday = input("Please enter a new birthday in csv format (name,email,year,month,day) or answer N to continue")
birthdays_file = "birthdays.csv"
if new_birthday == "N" or new_birthday == "n":
    pass
else:
    with open(birthdays_file, "a") as file:
        file.write(f"\n{new_birthday}")
    
birthdays_data = pandas.read_csv(birthdays_file)


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now().date()  # Get the current date without time

for index, row in birthdays_data.iterrows():
    if (
        row['month'] == now.month
        and row['day'] == now.day
    ):
        print(f"It's {row['name']}'s birthday!")
        BIRTHDAY = True
        NAME = row["name"]
        
        
        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if BIRTHDAY:
    # Your name variable
    name = NAME
    # Path to the folder containing text files
    folder_path = "letter_templates"

    # List all text files in the folder
    text_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

    if text_files:
        # Select a random text file from the list
        random_file = random.choice(text_files)

        # Read the contents of the selected text file
        file_path = os.path.join(folder_path, random_file)
        with open(file_path, "r") as file:
            file_contents = file.read()

        # Replace [Name] with the name variable
        modified_contents = file_contents.replace("Angela", "Anen")
        modified_contents = str(modified_contents.replace("[NAME]", NAME))
        print(modified_contents)
        
        
    # 4. Send the letter generated in step 3 to that person's email address.
    MY_EMAIL = "kelvinisshayo@gmail.com"
    PASSWORD = "macmuykehevhutvh"
    with smtplib.SMTP("smtp.gmail.com", port=587,) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, to_addrs=row['email'], msg=f"Subject: Happy Birthday!\n\n{modified_contents}")



