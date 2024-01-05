#TODO: Create a letter using starting_letter.txt 
  
with open("Input/Names/invited_names.txt", "rt") as file:
    global name 
    names = file.readlines()
    print(names)
    
for name in names:
    with open("Input\Letters\starting_letter.txt", "rt") as file:
        letter = file.read()
        letter.replace("[name]", f"{name.strip()}")
        with open(f"Output\ReadyToSend\letter_for_{name.strip()}.txt", "w") as file_1:
            file_1.write(letter.replace("[name]", f"{name.strip()}"))
        
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp