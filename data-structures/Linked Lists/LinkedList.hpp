#include <iostream>

template<typename T>
struct Node {
    T val;
    Node* next;

    Node(T head){
      val = head;
    }
};

// insert
template<typename T>
void insert(Node<T>* head, T newNode, size_t position);
// append
template<typename T>
void append(Node<T>* head, T newNode);
// remove
template<typename T>
void remove(Node<T>* head, size_t position);
// length
template<typename T>
size_t length(Node<T>* head);
