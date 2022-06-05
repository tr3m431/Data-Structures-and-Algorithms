#include "LinkedList.hpp"

int main(){
  Node<int>* list(0);
  list->next = Node<int>(1);
  std::cout << list->val << std::endl;
  std::cout << list->val << std::endl;
}
