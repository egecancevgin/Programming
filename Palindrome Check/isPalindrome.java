class Main {
  public static void main(String[] args) {
    System.out.println(isPalindrome(52125));
  }
  static boolean isPalindrome(int num) {
    /* 
      Checks if a number is in Palindrome form.
      Complexity: O(n), S(n).
    */
    int temp_num = num;
    int digit, index=0;
    int[] arr = new int[10];
    
    while (temp_num >= 1) {
      digit = temp_num % 10;
      arr[index] = digit;
      index = index + 1;
      temp_num = temp_num / 10;
    }

    for (int i=0; i<index; i++) {
      if (arr[i] != arr[index-i]) {
        return false;
      }
    }    
    return true;
  }
}
