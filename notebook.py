# Import time and pickle modules

import time
import pickle


# Load existing notebook data or create a new notebook

notebook_name = "notebook.dat"

try:

    file = open(notebook_name, "rb")
    notes = pickle.load(file)
    file.close()

except FileNotFoundError:
    print("File not found, creating a new notebook.")
    notes = []


# Create the main program loop

while True:


    print("""
          (1) Read notes
          (2) Add note
          (3) Edit note
          (4) Delete note
          (5) Save and exit""")
    
    choice = input("What would you like to do?: ")


    if choice == "1":
        for i in notes:
            print(i)

    elif choice == "2":
        entry = input("Write a new note: ")
        timestamp = time.strftime("%X %x")
        notes.append(entry + ":::" + timestamp)

    elif choice == "3":
        print("There are", len(notes), "notes.")
        number = int(input("Which note would you like to edit?: "))
        print(notes[number-1])
        new_text = input("Enter new text: ")
        timestamp = time.strftime("%X %x")
        notes[number -1] = new_text + ":::" + timestamp

    elif choice == "4":
        print("There are", len(notes), "notes.")
        number = int(input("Which note would you like to delete?: "))
        deleted = notes.pop(number-1)
        print("Deleted note:", deleted)

    elif choice == "5":
        file = open(notebook_name, "wb")
        pickle.dump(notes, file)
        file.close()
        print("Saving notebook and exiting.")
        break

    else:
        print("Invalid choice.")
