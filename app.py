class App:

    def pack(self):
        print("item1 \n" "item2 \n" "item3 \n")

remove = input("which item do you want to replace: ")
new1 = input("kindly insert your new item: ")
if remove == "item1":

    item[0] = item[0].replace(first_num, new1)
    gate = open('list.txt', 'w')
    gate.write('{}\n'.format(item))
    gate.close()
elif remove == "item2":

    item[1] = item[1].replace(sec_num, new1)
    gate = open('list.txt', 'w')
    gate.write('{}\n'.format(item))
    gate.close()
elif remove == "item3":

    item[2] = item[2].replace(third_num, new1)
    gate = open('list.txt', 'w')
    gate.write('{}\n'.format(item))
    gate.close()

elif remove != "item1,item2, item3":
    print("invalid item selected ")

else:
    print("thanks")

items = open('list.txt', 'r')
print(items.read())
items.close()


