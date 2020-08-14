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
        self.notInArrayMSG = 'Element not contained in array'

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
            if self.lengthUsed() <= self.size:
                for j in range(len(defaultVal)):
                    if(defaultVal[j] != None):
                        self.items.append(defaultVal[j])

                for i in range(len(defaultVal), self.size):
                    self.items.append(None)

                for elem in self.items:
                    if type(elem) != self.dataType and elem != None:
                        raise Exception('Array contains elements not of the specified data type')

                # if not all(isinstance(elem, self.dataType or None) for elem in self.items):
                #     raise Exception('Array contains elements not of the specified data type')

            else:
                # throw error if there are too many elements
                raise Exception('Elements are more than the size specified')

    # insert an element and increment the index of each element by 1
    def insert(self, index, element):
        # check if index is within array size (between 0 and size - 1)
        if index not in range(self.size):
            raise IndexError('Specified index is not available in the array')

        # check for empty space within the array
        if None not in self.items:
            raise Exception('Array is currently full')

        # check if new element is of the correct data type
        if type(element) != self.dataType:
            raise Exception('Array cannot contain elements not of the specified data type')

        # iterate through the array, insert, and move remaining elements
        if (self.lengthUsed() < self.size):
            for i in range(self.lengthUsed(), index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = element

        else:
            raise IndexError('Element index is out of range')

    # check if element is in the array, set to null if so, raise error if not
    # looks for first instance of the original element
    def delete(self, element):
        # check if element is in the array raise error if not...
        if element not in self.items:
            raise Exception(self.notInArrayMSG)

        # set to null if so
        for index in range(self.lengthUsed()):
            if self.items[index] == element:
                self.items[index] = None
            else:
                continue

    # search specified element using a linear search algorithm and return the index
    # raise an error if the element isn't in the array
    # looks for first instance of the original element
    def search(self, element):
        # check if the element is in the array
        if element not in self.items:
            raise Exception(self.notInArrayMSG)

        # use a linear sech to find the element and return the index
        for index in range(self.lengthUsed()):
            if self.items[index] == element:
                return index
            else:
                continue

    # check if element is in the array and if the new element is of the correct data type
    # locate and replace the original element with the new element
    # looks for first instance of the original element
    def update(self, oldElement, newElement):
        # check if new element is of the correct data data type
        if not isinstance(newElement, self.dataType):
            raise Exception('New element is not of the specified data type')

        # check if the element to be replaced is in the array
        if oldElement not in self.items:
            raise Exception(self.notInArrayMSG)

        # use a linear search to find and replace the original element
        for index in range(self.lengthUsed()):
            if self.items[index] == oldElement:
                self.items[index] = newElement
            else:
                continue

    # return length of the array
    lengthUsed = lambda self : sum([1 for elem in self.items if elem != None])

    # print all elements in the array
    # printAll = lambda self : print(self.items)

    def printAll(self):
        print(self.items)

# tests
if __name__ == "__main__":
    # test array
    newArr = Array(int, 5, [num for num in range(4)])

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

    # insert 4 as the final element of the array
    newArr.insert(4, 4)

    # delete the newly inserted element: 4
    newArr.delete(4)

    # update the first element of the array, 0, to 5
    newArr.update(0, 5)

    # should return 4 (or number of elements)
    print(newArr.lengthUsed())

    # print all elements in the array
    newArr.printAll()

    # search and print the fourth elemnt in the newArr array
    print('Index of searched element 3: {0}'.format(newArr.search(3)))

    print("\nCode executed successfully\n")
