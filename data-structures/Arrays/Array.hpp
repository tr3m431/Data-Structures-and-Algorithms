#include <iostream>

// enables type and size to be determined at instantiation
template<typename T, size_t S>

class Array {
public:
  // returns the number of elements (includes unoccupied positions) as a constant
  size_t size() const { return S; }

  // overload [] operator to return the value corresponding to the entered index
  T& operator[](size_t index) { return array[index]; }
  const T& operator[](size_t index) const { return array[index]; }

  // returns the memory addres of the array
  T* data() { return array; }
  const T* data() const { return array; }

  // length used in the array
  // size_t lengthUsed(){
  //   int length = 0;
  //
  //   for (size_t i = 0; i < S; i++){
  //     // if the current value isn't NULL, increment length
  //     if (array[i])
  //       length++;
  //   }
  //
  //   return length;
  // }

  // insert
  void insert(T element, size_t index){
    // check if index is within the array
    if (index < 0 && index >= S)
      throw "Specified index is not available in the array";

    // check if the array is full

    // insert element and moving remaining elements

  }

  // delete
  void Delete(T* element);

  // update
  void update(T* oldElement, T newElement);

  // traverse
  void printAll();

  // search
  T search(T element);

private:
  T array[S];
};
