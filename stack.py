from collections import deque
students = deque()          #intialize students using class deque
students.append('James')    #add elements to stack 
students.append( 'John')              
students.pop()              #display and delete last element appended element 
print(students.is_empty())  #Print true if stack is empty and false if not  
print(students)    
