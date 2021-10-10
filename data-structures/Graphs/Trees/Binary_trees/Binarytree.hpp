# pragma once
#include <iostream>

template<typename T>
struct Node {
  T value;
  Node* left;
  Node* right;

  Node(T value){
    this->value = value;
    left = NULL;
    right = NULL;
  }
};
