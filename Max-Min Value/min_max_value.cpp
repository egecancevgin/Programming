#include <iostream>


int minimum(int arr[], int size){
  /* Finds the minimum value of an array and returns it.
  Complexity: ~O(n), S(1) */
  
  // Initializing the biggest number possible
  int min_value = 9999999;
  
  // Traverse the whole array and check if there are smaller elements
  for (int i=0; i<size; i++){
    if (arr[i] < min_value)
      min_value = arr[i];
  }

  return min_value;
}


int maximum(int arr[], int size){
  /* Finds the maximum value of an array and returns it.
  Complexity: ~O(n), S(1) */
  
  // Initializing the biggest number possible
  int max_value = -9999999;
  
  // Traverse the whole array and check if there are smaller elements
  for (int i=0; i<size; i++){
    if (arr[i] > max_value)
      max_value = arr[i];
  }

  return max_value;
}


int main() {
  
  int test_arr[] = {32, 21, 174, 18, 46, 98, 13, 23, 108};

  // Calculating the array size before calling to make it easier
  int size = sizeof(test_arr) / sizeof(test_arr[0]);
  
  std::cout << "The maximum value of the test array is: " << maximum(test_arr, size) << std::endl;
  
  std::cout << "The minimum value of the test array is: " << minimum(test_arr, size) << std::endl;

  return 0;
}
