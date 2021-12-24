from node import Node
# List yang datanya tidak terurut
# Urutan insert data
# A -> B -> Z -> Y

# Unorderlist
# Ketika di cetak 
# A -> B -> Z -> Y

# Orderlist
# Ketika di cetak 
# A -> B -> Y -> Z

# List function di python:
# append
# extend
# insert
# remove
# pop
# clear
# index
# count
# sort
# reverse
# copy


class UnorderedList:
      def __init__ (self): 
            self.head = None
      
      def isEmpty(self):
            return self.head == None
      
      # ###########           ###########
      # # "item 2"  #         # "item 1"  #
      # ###########           ###########
      # Prev# Next  -->       Prev# Next
      # |
      # |
      # Head
      
      def add(self,item): # append
            temp = Node(item) 
            temp.setNext(self.head) 
            self.head = temp

      # PR ====
      # def cetak():
      # def insert(self, index, item):
      # def reverse(self):
      # def pop(self):
      
      def size(self): #count
            current = self.head 
            count = 0 
            while current != None:       
                  count = count + 1
                  current = current.getNext()
            return count

      def search(self,item):
            current = self.head 
            found = False
            while current != None and not found:
                  if current.getData() == item:
                        found = True 
                  else:
                        current = current.getNext()
            return found

      def remove(self,item):
            current = self.head 
            previous = None 
            found = False 
            while not found:
                  if current.getData() == item:
                        found = True
                  else:
                        previous = current 
                        current = current.getNext()
            
            if previous == None:
                  self.head = current.getNext() 
            else:
                  previous.setNext(current.getNext())
      
      