"""
Array characteristics:
    size: defined at declaration (fixed)
    type: any (all elements must have the same type)
    random access: allowed
    operations: insert, delete, search, print, update, append
"""

class Array:
    def __init__(self, size, defaultVal = None):
        # declare size at instantiation
        self.size = size
        self.items = []

        # fill array with null values if no default value is set
        if(defaultVal == None):
            self.items = [defaultVal for i in range(size)]
        else:
            # otherwise fill items arrya with default values
            if len(defaultVal) <= size:
                for j in range(len(defaultVal)):
                    if(defaultVal[j] != None):
                        self.items.append(defaultVal[j])
                for i in range(len(defaultVal), size):
                    self.items.append(None)
            else:
                # throw error if there are too many elements
                raise Exception('Elements are more than the size specified')

    # return length of the array
    length = lambda self : sum([1 for elem in self.items if elem != None])

    # print all elements in the array
    def printAll(self):
        print(self.items)

# tests
if __name__ == "__main__":
    # declare new array with proper number of elements
    newArr = Array(5, [i for i in range(5)])

    # declare new array with improper number of elements
    # newArr = Array(5, [i for i in range(6)])

    # should return 5 (or number of elements)
    print(newArr.length())

    # print all elements in the array
    newArr.printAll()


    print("\nCode executed successfully\n")
