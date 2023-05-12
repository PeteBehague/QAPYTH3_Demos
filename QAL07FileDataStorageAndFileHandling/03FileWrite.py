# Program : 03FileWrite
# Purpose : Example to open and write to file

file = open("03FileWrite.txt","w")
#                              ^ Write
for n in range(1,11):
    newline = "This is line " + str(n) + "\n"
    file.write(newline)
file.close()


file = open("03FileWrite.txt","a")
#                              ^ Append
for n in range(12,21):
    newline = "This is line " + str(n) + "\n"
    #                                      ^ new line char
    file.write(newline)
file.close()


file = open("03FileWrite.txt","w")
#                              ^ Write
for n in range(21,31):
    newline = "This is line " + str(n) + "\n"
    file.write(newline)
file.close()

