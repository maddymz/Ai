#program to calculate booth multiplication 
#It takes input in decimal numbers and returns binary multiplaiction 

#function for decimal to binary conversion 
def decimal_to_binary(number):
    if(number < 0):
        return format (twosComplement(number, 8), "08b")

    elif(number > 255):
        return format(number,"08b")[1:]    
    
    else:
        return format(number, "08b")

#function to add the binary numbers
def binaryAddition (num1, num2):
    num3 = int(num1,2) + int(num2, 2)
    return decimal_to_binary(num3)

#function to carry out the multiplication
def boothMultiplication (multiplier, multiplicand, twosComplementM) :
    valueRegisterA = decimal_to_binary(0)
    valueRegisterQ = multiplier
    valuerRegisterM = multiplicand
    
    lastShiftedBit = '0'

    for i in range(len(multiplier)):
      
        multiplierLSB = valueRegisterQ[7]
        if (multiplierLSB == lastShiftedBit):
            valueRegisterA, valueRegisterQ, lastShiftedBit = binaryShift(valueRegisterA, valueRegisterQ, lastShiftedBit)

        elif (multiplierLSB == '0' and lastShiftedBit == '1'):
            valueRegisterA = binaryAddition(valueRegisterA , valuerRegisterM)
            valueRegisterA, valueRegisterQ, lastShiftedBit = binaryShift(valueRegisterA, valueRegisterQ, lastShiftedBit)

        elif (multiplierLSB == '1' and lastShiftedBit == '0'):
            valueRegisterA = binaryAddition(valueRegisterA , twosComplementM)
            valueRegisterA, valueRegisterQ, lastShiftedBit = binaryShift(valueRegisterA, valueRegisterQ, lastShiftedBit)
    i = i -1
    product = int((valueRegisterA + valueRegisterQ),2)
    print("Final value is  : " + str(product))

#function to calculate 2's complement 
def twosComplement(multiplicand, bits):
    if(multiplicand & (1 << (bits - 1))) !=0:
        multiplicand = multiplicand - (1 << bits)
    return multiplicand  & ((2 ** bits) - 1)

#function to perform binary shift
def binaryShift(valueRegisterA, valueRegisterQ, lastShiftedBit):
    lastShiftedBit = valueRegisterQ[-1]
    registerALSB = valueRegisterA[-1]

    if(valueRegisterA[0] == '1'):                                                      # chaeck the MSB 
        valueRegisterA = decimal_to_binary(int(valueRegisterA, 2) >> 1)                # retain it 
        valueRegisterA = '1'+valueRegisterA[1:]
    else:
        valueRegisterA = decimal_to_binary(int(valueRegisterA, 2) >> 1)
    
    valueRegisterQ = decimal_to_binary(int(valueRegisterQ, 2) >> 1)
    valueRegisterQ = registerALSB + valueRegisterQ[1:]
    return valueRegisterA, valueRegisterQ, lastShiftedBit


decimalMultiplier = -29
decimalMultiplicand = -105
multiplier = decimal_to_binary(decimalMultiplier)
multiplicand = decimal_to_binary(decimalMultiplicand)

if(decimalMultiplicand < 0 ):                                                           #check for negative number 
    twosComplementM = decimal_to_binary(-decimalMultiplicand)                           # then calculate teh 2's complement
else:
    twosComplementM = decimal_to_binary(twosComplement(decimalMultiplicand, 8))

boothMultiplication(multiplier, multiplicand, twosComplementM)                          # function call for multiplaication 

