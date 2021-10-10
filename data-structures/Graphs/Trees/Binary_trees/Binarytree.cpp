#include "Binarytree.hpp"
#include <queue>

void depth_first_traversal(Node<int>* root){
  if (!root){
    std:: cout << "empty" << std::endl;
    return;
  }

  std::cout << root->value << std::endl;

  if (root->left)
    depth_first_traversal(root->left);

  if (root->right)
    depth_first_traversal(root->right);
}

void breadth_first_traversal(Node<int>* root){
  if (!root){
    std:: cout << "empty" << std::endl;
    return;
  }
  
  std::queue<Node<int>*> q;

  for (q.push(root); !q.empty(); q.pop()){
    Node<int>* current = q.front();
    std::cout << current->value << std::endl;

    if (current->left)
      q.push(current->left);

    if (current->right)
      q.push(current->right);
  }
}

int main(){
  Node<int>* root = new Node<int>(1);
  root->left = new Node<int>(3);
  root->right = new Node<int>(2);
  root->right->left = new Node<int>(4);
  root->right->right = new Node<int>(5);
  root->right->left->right = new Node<int>(7);
  root->left->left = new Node<int>(6);

  depth_first_traversal(root);
  std::cout << "---------------------" << std::endl;
  breadth_first_traversal(root);

  std::cout<<"done"<<std::endl;

  free(root);
  return 0;
}
