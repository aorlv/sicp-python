#(define (a-plus-abs-b a b)
#    ((if (> b 0) + -) a b))

def a_plus_abs_b(a, b):                 
    if b > 0:                                  #Если b больше 0
        print(a + b)                             #напечатать результат сложения а и b
    else:                                        #Иначе (если b <= 0)
        print(a - b)                             #напечатать результат вычитания а и b
    
    #print(a + b) if (b > 0) else print(a - b)    #тоже самое, только тернарным оператором

a_plus_abs_b(2, 4)
a_plus_abs_b(3, -1)
a_plus_abs_b(5, 0)
 