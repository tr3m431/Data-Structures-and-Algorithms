"""
Array characteristics:
    size: defined at declaration (fixed)
    type: any (all elements must have the same type)
    random access: allowed
    operations: insert, delete, search, print, update
"""

class Array:
    def __init__(self, dataType, size = None, defaultVal = None):
        # declare size at instantiation
        self.size = size
        self.items = []
        self.dataType = dataType

        # check that size and defaultVal aren't None
        if size == None and defaultVal == None:
            raise Exception('Array instance must contain either size or default values')

        # set size to number of elements in defaultVal if not specified in the constructor
        if self.size == None:
            self.size = sum([1 for elem in defaultVal])

        # fill array with null values if no default value is set
        if(defaultVal == None):
            self.items = [defaultVal for i in range(self.size)]

        else:
            # otherwise fill items array with default values
            if len(defaultVal) <= self.size:
                for j in range(len(defaultVal)):
                    if(defaultVal[j] != None):
                        self.items.append(defaultVal[j])

                for i in range(len(defaultVal), self.size):
                    self.items.append(None)

                if not all(isinstance(elem, self.dataType) for elem in self.items):
                    raise Exception('Array contains elements not of the specified data type')

            else:
                # throw error if there are too many elements
                raise Exception('Elements are more than the size specified')

    def insert(self, index, element):
        # check if index is within array size (between 0 and size - 1)
        #
        return None

    # return length of the array
    lengthUsed = lambda self : sum([1 for elem in self.items if elem != None])

    # print all elements in the array
    # printAll = lambda self : print(self.items)

    def printAll(self):
        print(self.items)

# tests
if __name__ == "__main__":
    # test array
    newArr = Array(int, 5, [num for num in range(5)])

    # declare new array with proper number of elements using all parameters
    # newArr = Array(int, 5, [i for i in range(5)]) -> GOOD

    # declare an array of size 5 and data type int
    # newArr = Array(int, 5) -> GOOD

    # declare an int array of numbers in range(5)
    # newArr = Array(int, None, [num for num in range(5)]) -> GOOD

    # declare a mixed type array as an int array
    # newArr = Array(int, None, ['yes', 4]) -> GOOD (throws custom error)

    # declare a int array with no size or default values
    # newArr = Array(int, None, None) -> GOOD (throws custom error)

    # should return 5 (or number of elements)
    print(newArr.lengthUsed())

    # print all elements in the array
    newArr.printAll()


    print("\nCode executed successfully\n")