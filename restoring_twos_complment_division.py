#algorithm for restoring twos complement division 
"""
Algorithm to implement the two's complement restoring divsion 
Assuming that dividend and remainder always have same sign 
Algorithm complie to the following relation :
Dividend = Divisor * Quotient + Remainder
"""
# function to convery a decimal number to binary 
def decimal_to_binary(number):
    if(number < 0):                                                                 #when number is negative
        return format (twos_complement(number, 8), "08b")                           #calculate two's complement and convert to binary
    elif(number > 255):                                                             #overflow condition 
        return format(number,"08b")[1:]                                             #discard the overflow bit
    else:               
        return format(number, "08b")
# # ===============================================================================================================

#function to calculate 2's complement 
def twos_complement(number, bits):
    if(number & (1 << (bits - 1))) !=0:
        number = number - (1 << bits)                                                #perform division 
    return number  & ((2 ** bits) - 1)                                               #convert the number in integer form 
# # ===============================================================================================================

#function to perform binary shift
def binary_shift(regA, regQ):
    regA =decimal_to_binary(int(regA, 2) << 1)                                        #left shift 
    regQ = decimal_to_binary(int(regQ, 2) << 1)                                       
    
    return regA, regQ

# # ===============================================================================================================
#function to calculate division 
def restoring_division (dividend, divisor, bits):

    if((dividend < 0 and divisor < 0) or (dividend >0 and divisor > 0)):               #ceck if both the dividend and divisor are of same sign 
        flag = False                                                                   #set flag false
    else:                                                                              #else tehy of opposite sign 
        flag = True                                                                    #set flag true                            
        
    div = decimal_to_binary(abs(divisor))
    complement = twos_complement(-int(div,2), number_bits) 
    twosCdiv = decimal_to_binary(complement)
    regM_init = twosCdiv                                                               # load two's complement of divisor in register M
    regQ_init = decimal_to_binary(abs(dividend))
    regQ = regQ_init

    regA_init = decimal_to_binary(0)
    regA = regA_init

    i=0
    while i <len(regQ):                                                                 #perform deivsion as many times as there are bit positions in Q
        shiftedbit = regQ[0]                                                            #store left shifted bit
        regA, regQ = binary_shift(regA, regQ)                                           #shift the bits of A and Q to left
        regA = regA[:7] + shiftedbit                                                    
        res_regA = regA
        regAMsb = res_regA[0]  
                                    
        regA = int(regA,2) + int(twosCdiv,2)                                            #do A<-- A-M by adding two's complement of divisor 

        regA = decimal_to_binary(regA)
        regQ = decimal_to_binary(int(regQ,2))

        if(regAMsb == regA[0]):                                                         #check if reg A has same sign 
            regQ = regQ[:7] + "1"                                                       # Q0 <-- 1
        else:
            regQ = regQ[:7] + "0"                                                       # Q0 <-- 0
            regA = res_regA                                                             # restore
        i+=1

    remainder = regA                                                                    #store remainder
    quotient = regQ                                                                     #store quotient
    magRemainder = int(remainder, 2)                                                    # calculate signed magnitude
    magQuotient = int (quotient, 2)

    if (flag == True):                                                                  #check if fag is true
        magRemainder = -int(remainder[1:], 2)                                           
        magQuotient = -int (quotient[1:], 2)
        quotient = decimal_to_binary(twos_complement(-int(quotient,2), bits))           #negate the quotient            
        remainder = decimal_to_binary(twos_complement(-int(remainder,2), bits))         #negate teh remainder    
    
    return quotient, remainder, regA_init, regM_init, regQ_init, magRemainder, magQuotient
# # ===============================================================================================================

# variable intialization and function call
decDividend = -9
decDivisor =  3
number_bits = 8
quotient, remainder, regA_init, regM_init, regQ_init, magRemainder, magQuotient = restoring_division(decDividend, decDivisor, number_bits)

#print the results 
print("\n" + "Input decimal values are : {} and {} \n".format(decDividend, decDivisor))
print("Initial values in register A, Q amd M are : A = {}, Q = {}, M = {} \n".format(regA_init, regQ_init, regM_init))
print("Values after final cycle in Register A = {} and Register Q = {} \n".format(remainder, quotient))
print("Final values : Quotient = {}, Remainder = {} \n".format(quotient, remainder))
print("Values in decimal yRx form : {} R {} , where y = quotient and x = remainder".format(magQuotient, magRemainder))
# # ====================================================================================================================
        


