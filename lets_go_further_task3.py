meetings = [["Monday", "3:30 PM", "Joe", "Samantha"], ["Monday", "4 PM", "Arnold", "Schwarzenegger"], 
            ["Tuesday", "2 PM", "Joe", "Samantha"], ["Tuesday", "5.30 PM", "Bruce", "Willis"], 
            ["Wednesday", "3 PM", "Bruce", "Willis"], ["Wednesday", "2 PM", "Joe", "Samantha"]]

name = input("Entrer un nom : ")

name_meetings = ""
for i in range(len(meetings)):
    current = meetings[i]
    if name == current[3]:
        name_meetings += current[0] + " " + current[1] + "\n"
print(name_meetings)