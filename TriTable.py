
'''
Explanation of Nested for loop 
Loop 1 - the first loop iterates to 10, this controls the total size of the pyramid 
Loop 2 - the second loop does the printing of the pyramid. the range starts at 1 to avoid the 0 being printed in the beginning of the loop, changing it to 0 will result the pyramid having a zero at top. 
Loop 2 - if you change the first number to say 3 then the pyramid starts at 3 and goes on from there, showing different results.
Loop 2 - the i + 1 controls the width of the pyramid. if we keep it at i, the pyramid still functions but misses the last digit at every loop and iteration.
Loop 2 - the printing of the i * k is the calculation of every number. With every loop the index changes. taking number 5 as an example. 
Loop 2 - i = 5, and prints out the 5. and this stage the second loop is at its second iteration and multiplies the 5 with 2. for its third iteration it multiplies the 5 with 3. and fourth iteration with 4 to give you, 10, 15, 20
print() - the last print function prints a new line, without it the entire loop will print out on one line
'''

def triTable(x,y):
    for i in range (0,x): #controls the size of the pyramid
        for k in range(1, i + y): #starting point of pyramid and controls width of pyramid, y controls the width of the pyramid
            print (i * k, end = " ") #multiplies the iterations with each other for example at the outer loop number 7, the second loop multiplies it with 2,3,4,5,6 to get the values
        print ()
        
if __name__=="__main__": 
    
    triTable(10,1) #inputs are 10 and 1 for the question but can be changed depending on what size pyramid you want