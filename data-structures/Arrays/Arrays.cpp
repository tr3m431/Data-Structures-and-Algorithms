#include <iostream>
#include "Array.hpp"

int main(){
  // fixed size array tests
  Array<std::string, 2> hi;

  hi[0] = "Hello, ";
  hi[1] = "world!";

  for (int i = 0; i < hi.Size(); i++){
    std::cout<< hi[i];
  }

  std::cout<< std::endl;

  // dynamically sized array tests

  return 0;
}
