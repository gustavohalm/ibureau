def my_binary(n):
    str_binary = ''
    while n > 0:
        str_binary += str( n % 2 )   
        n = n // 2
    return str_binary[::-1]

def max_sequence(n):
    binary = my_binary(n)
    m = 0
    new_max = 0

    for b in binary:
        if b == '0':
            new_max += 1
            if new_max > m:
                m = new_max
        else:
            new_max = 0
    return str( m ) 

print( max_sequence(3))
 
print( max_sequence(89) )  # 
print( max_sequence(20) )  
print( max_sequence(4353) )  
print( max_sequence(100000) ) 
print( max_sequence(2065) ) 
