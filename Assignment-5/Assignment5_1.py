# Write a recursive program which display below pattern.
i=1
def Pattern():
    global i
    if(i<=5):
        print("*")
        i = i+1
        Pattern()

Pattern()