def my_binary(n):
    str_binary = ''
    while n > 0:
        str_binary += n % 2    

    return reverse(str_binary)

def max_sequence(n):
    binary = bin(n).split('b')[1]
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
