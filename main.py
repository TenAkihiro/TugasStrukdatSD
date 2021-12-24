from UnorderedList import UnorderedList

mylist = UnorderedList()
mylist.add(31) 
mylist.add(40)
mylist.add(50)
mylist.add(70)

print(mylist.isEmpty()) # False
print(mylist.size()) # 2
print(mylist.search(40)) # True

mylist.remove(40) 
print(mylist.search(40)) #False

mylist.insert(3, 100)  
print(mylist.search(100)) #True

mylist.cetak()  # 31 40 100 50 70

mylist.reverse()  
mylist.cetak() # 70 50 100 40 31

mylist.pop()
mylist.cetak() # 70 50 100 40

