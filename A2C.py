i=0
output = open("cowascii.cow","w")
txt = input("Enter your text: ") 
for char in txt:
    c= ord(char)
    while (True):
        if(i<c):
            output.write("MoO ")
            i += 1
        else:
            output.write("Moo OOO ")
            i=0
            break