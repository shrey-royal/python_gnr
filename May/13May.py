'''
while loop

Syntax-: 
    intialization
    while(condition){
        //body
        //inc/dec
    }

-> if increment or decrement is not written then the loop will executes infinite times...

In Python-> 
    initialization
    while condition:
        //body
        //inc/dec
        print()
    print()
    {
        statemtn1
        stmt2
        stmt3
    }
'''

# 0 false otherwise true


# i=1
# while i<=10:
#     print(i)
#     i+=1
# print(f"i = {i}")

# i=1
# while i<=20:
#     if i%2 == 0:
#         pass #continue
#     else:
#         print(i)
#     i+=1

list = ['royal', 34, 'students', 78]
i = 1
j = len(list)
while i<=j:
    print(list[i-1])
    i+=1

