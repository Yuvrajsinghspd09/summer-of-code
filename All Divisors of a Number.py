'''
 Time Complexity: O(sqrt(N))
 Space Complexity: O(sqrt(N))
'''

def find_divisors(N):
    divisors=[]
    for i in range(1,int(N**0.5)+1):
        if N%i==0:
            divisors.append(i)

            if i!=N//i: # for e.g 18//2= 9, to get 9 in list, we did this step
                divisors.append(N//i)
        
        divisors.sort()
        print(" ".join(map(str, divisors)))
        
    #The line print(" ".join(map(str, divisors))) is a compact and efficient way to convert a list of integers into a single string 
    # where each integer is separated by a space, and then print that string. 
 # practice attempt 1
 def find_all_div(num):
     divisors=[]
     for i in range (1,int(num**0.5)+1):
          if num%i ==0:
           divisors.append(i)

           if i!=num//i:
            divisors.append(num//i)
          divisors.sort()
          print(" ".join(map(str, divisors)))
      
