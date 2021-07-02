#pragma once
#include <iostream>

template <typename T>;
bool binary_search(vector<T>& arr, T target){
  int start = 0;
  int end = arr.size()-1;

  while (start <= end){
    int mid = (start+end)/2;

    // check if target elem is greater or less than or equal to mid
    if (target == arr[mid])
      return true;

    // exclude unusable sections
    if (target > arr[mid])
      start = mid+1;
    else
      end = mid-1;

    // continue until start is greater than end
  }

  return false;
}
