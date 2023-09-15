# Bonus 1 :
char = "Bonjour1a1tous21je1suis1Albert1Nestor21le1castor31En1janvier1de1l4année1dernière21plus1de1dix5mille1personnes1m4ont1voués1un1culte31C4était1marrant21mais1un1peu1bizarre31En1tout1cas1plus1que1de1s4appeler1Albert1Nestor1en1étant1un1castor."
char2 = char.replace("1", " ")
char3 = char2.replace("2", ",")
char4 = char3.replace("3", ".")
char5 = char4.replace("4", "'")
char6 = char5.replace("5", "-")
char7 = char6.replace("castor", "Castor")
print(char7)

# Bonus 2 :
charPal = "racecarbananaappleleveldeifiedcivicnoonradarrotorreferkayakmadamtenetwowbobpoppeepredderrepaperrotatorlevelerreviverredividerdetartratedmalayalam"

def find_palindromic_substring(x):
    print()