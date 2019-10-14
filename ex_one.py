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

print( max_sequence(3) ) # return 0 
print( max_sequence(4) )  # 

print( max_sequence(88) )  

print( max_sequence(100) )  

print( 'binario:' + bin(100))
print( max_sequence(100000) ) 
