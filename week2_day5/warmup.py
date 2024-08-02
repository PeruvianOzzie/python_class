def is_palindrome(word):

    is_palindrome_flag = False

    word1 = word.lower()
    word2 = word1.replace(" ", "")
    word3 = word2.replace(",", "") 
   
    reversed_word = word3[::-1]
  
    
    if word3 == reversed_word:
        is_palindrome_flag = True

    return is_palindrome_flag
    

print(f"The workd is palindrome:  {is_palindrome("A man, a plan, a canal, Panama")}")
