#include <iostream>

std::string is_palindrome(int test_num){
  /* The function checks if the number is palindrome or not.*/
  int temp_num = test_num;
  int digit;
  int index=0;
  int arr[20] = {};
  
  while (temp_num >= 1) {
    digit = temp_num % 10;
    arr[index] = digit;
    index = index + 1;
    temp_num = temp_num / 10;
  }
  for (int i=0; i<index; i++) {
    //std::cout << arr[i] << " " << arr[index-1-i] << std::endl;
    if (arr[i] != arr[index-1-i])
      return "non-palindrome number";
  }
  return "palindrome number";
}


int main() {
  
  int test_num = 1221;

  std::cout << "The number " << test_num << " is a " << is_palindrome(test_num) << std::endl;
  
  return 0;
}
