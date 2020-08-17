#include <iostream>
#include <array>

// enables type and size to be determined at instantiation
template<typename T, size_t S>

class Array {
public:
  // returns the number of elements (includes unoccupied positions) as a constant 
  size_t Size() const { return S; }

  T& operator[](size_t index) { return m_Data[index]; }
  const T& operator[](size_t index) const { return m_Data[index]; }

  T* Data() { return m_Data; }
  const T* Data() const { return m_Data; }

  // insert
  void insert(T element);
  // delete
  void Delete(T element);
  // update
  void update(T oldElement, T newElement);
  // traverse
  void printAll();
  // search
  T search(T element);

private:
  T m_Data[S];
};

// int main(void){
//   Array<std::string, 2> message;
//
//   message[0] = "Hello";
//   message[1] = "world!";
//
//   memset(&message[0], 0, message.Size() * sizeof(int));
//
//   for (int i = 0; i < message.Size(); i++){
//     std::cout<< message[i] << std::endl;
//   }
//
//   return 0;
// }
