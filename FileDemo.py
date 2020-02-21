# File object can be iterated
f_name=open("./fileDemo")
for line in f_name :
    print('line is : ',line)
f_name.close()

