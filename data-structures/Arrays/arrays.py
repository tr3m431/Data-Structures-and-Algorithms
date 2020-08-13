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
            if len(defaultVal) <= size:
                for j in range(len(defaultVal)):
                    if(defaultVal[j]):
                        self.items.append(defaultVal[j])
                for i in range(len(defaultVal), size):
                    self.items.append(None)
            else:
                raise Exception('Elements are more than the size specified')

# tests
if __name__ == "__main__":
    newArr = Array(5, [i for i in range(5)])

    print("\nCode executed successfully\n")
