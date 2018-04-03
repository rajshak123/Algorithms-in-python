from linkedlist import LinkedList
LinkedList=LinkedList()
LinkedList.insertStart(12)
LinkedList.insertStart(34)
LinkedList.insertStart(50)

print('\n')
LinkedList.traverse()

LinkedList.insertEnd(90)
LinkedList.insertEnd(100)
LinkedList.insertEnd(29)
print('\n')
LinkedList.traverse()


# LinkedList.removeStart()
# print('\n')
# LinkedList.traverse()

# LinkedList.removeEnd()
# print('\n')
# LinkedList.traverse()

LinkedList.removeAny(12)

LinkedList.removeAny(90)
LinkedList.removeAny(34)
print('\n')
LinkedList.traverse()