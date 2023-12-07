import json


'''
# Spara en inmatning & läs in den när man startar programmet
with open("intro.txt", "r") as txt: 
    contents = txt.read() 
    print(contents,end="")
    
    # There is also readlines - returns an array of each newline,
    # and readline, which returns new line from the file each time it is called. 
    # You can also set the number of characters to read.
'''


'''
# Gör så programmet matar ut “Inget sparat” om filen inte existerar
try:
    with open("none.txt", "r") as txt: 
        contents = txt.read()
        print(contents)
except FileNotFoundError: 
    print("No such file found !")
'''


'''
# Skapa ett program som sparar flera saker med bibliotek och JSON-format
info = {
    "Subject":"Freeman",
    "Status":"Observation Terminated",
    "Postmortem": "Subject declined offer of employment"
}

with open("status.json", "w") as file:
    json.dump(info, file) 

    file.flush() # apply the changes without ending the file stream.

    with open("status.json", "r") as file: 
        content = json.load(file)
        print(content["Subject"])
'''
