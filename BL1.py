
f_in = open("BL1.INP", "r")
f_o = open("BL1.OUT", "w", encoding = "UTF-8" )

n = f_in.readlines()
lst = []

for i in n:
    if i == " ":
        continue
    n = i
data = int(n)

f_o.write(f"Các ước của {data}: ")

for uoc in range(1,data+1):
    if data%uoc != 0:
        continue
    f_o.write(f"{uoc} ")
    lst.append(uoc) 
f_o.write(f"\nCác số nguyên tố: ")
dem = 0 
for nguyento in lst:
    if nguyento == 2:
        f_o.write("2 ")
    for i in range(2,nguyento):
        if nguyento%i == 0:
            dem += 1
        if dem == 0:
            f_o.write(f"{nguyento}")
        else:
            None







