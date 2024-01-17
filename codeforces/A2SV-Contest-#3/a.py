a = input()
all_ = []
while a != "":
    all_.append([i for i in a.split()])
    a = input()
with open("b.csv", "w") as file:
    for i in all_:
        file.write(str(i[1].encode('utf-8'))[2:-1])
        file.write("\n")
