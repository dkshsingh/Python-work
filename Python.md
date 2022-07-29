# Python Hacks

### 1.fibonacci series
#### a series of numbers in which each number (fibonacci number) is the sum of the two preceding numbers.
#### code:
      fibo = [0,1]
      [fib.append(fib[-2]+fib[-1]) for i in range(5)]
      fibo
      > [0,1,1,2,3,5,8]
      
      
 ### 2.check palindrome of string
 #### a palindrome is a number or string that looks the same when it gets reversed.
 #### code:
         text = 'level'
         ispalindrome = text == text[::-1]
         ispalindrome
         > true
 ### 3. find transpose of matrix
 #### you can transpose a matrix in just one line of code using zip function.
 ### code:
         a = [[1,2,3]
              [4,5,6]
              [7,8,9]]
          transpose = [list(i) for i in zip(*a)]
          transpose
          > [[1,4,7],[2,5,8],[3,6,9]]
### 4. type-casting whole list in one go
### code:
         list(map(int,['1','2','3']))
         >[1,2,3]
         list(map(float,[1,2,3]))
         >[1.0,2.0,3.0]
         [float(i) for i in [1,2,3]]
         >[1.0,2.0,3.0]
### 5. creating lists using for loop
### code:
        lst = list(range(0,10))
        print(lst)
         
         
         
         
