class app:
 def __init__(self, first_num, sec_num, third_num, response):
    self.first_num = first_num
    self.sec_num = sec_num
    self.third_num = third_num
    self.response = response

print("list of things  you want to buy")
first_num = input("first: ")
sec_num = input("second: ")
third_num = input("third: ")
# listt = 'list.txt'
item = [first_num, sec_num, third_num]
listt = open('list.txt', 'w')
listt.write('{}\n'.format(item))
listt.close()
items = open('list.txt', 'r')

# for items in items:
print("your items have been stored ")
print(items.read())
items.close()

#response = input("do you want to replace any item? ")
#if response == "Yes":
   # print("hello")
#else:
   # if response == "No":
      #  return None


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









