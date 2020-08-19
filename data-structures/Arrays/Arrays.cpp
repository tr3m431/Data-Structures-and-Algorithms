#include <iostream>
#include "Array.hpp"

int main(){
  // fixed size array tests
  Array<int, 2> hi;

  hi[0] = 1;
  hi[1] = 2;

  for (int i = 0; i < hi.size(); i++)
    std::cout<< hi[i] << std::endl;


  std::cout<< hi.data() << std::endl;

  // dynamically sized array tests

  return 0;
}
