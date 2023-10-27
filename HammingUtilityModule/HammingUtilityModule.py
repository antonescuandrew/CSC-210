#Hamming code utility module
#complete all the function stubs.  You can add other functions if you wish,
#  but they will not be tested or graded separately from the functions
#  already in this template.  You may NOT change the names, parameters,
#  parameter types, or return types of any of these functions.
#A data byte will be represented as a list of 8 integers, each integer will be
#either 1 or 0
#A Hamming code will be represented as a list of 12 integers, each integer will be
#either 1 or 0
#NOTE: Be aware that the bits of Hamming codes are numbered two ways, by their
#    position in the list (0-11) and by their Hamming position (1-12).  Make sure
#you
#    know which you are suppposed to be using in each situation
##debugging and other useful functions
def inputData(): #get input from the user to create a data byte
    listdata = []
    inputstring = input("Input an 8 digit data byte:")
    for character in inputstring:
        listdata.append(int(character))
    return listdata
def inputHamming(): #get input from the user to create a Hamming code
    listhamming = []
    inputhamming = input("Input a 12 digit Hamming code:")
    for character in inputhamming:
        listhamming.append(int(character))
    return listhamming
def dataToString(d8): #d8 example: [0,0,0,0,0,0,0,0]
    stringdata = ''
    for number in d8:
        stringdata = stringdata + str(number)
    return stringdata
def HammingToString(HC): #HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    stringhamming = ''
    for number in HC:
        stringhamming = stringhamming + str(number)
    return stringhamming
def printData(d8): #d8 example: [0,0,0,0,0,0,0,0]
    print(*d8,sep='',end='')
    return #no return value; the 8 digits of d8 are printed with no other
#characters, no blanks, no newline ...
def printHamming(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    print(*HC,sep='', end='')
    return #no return value; the 12 digits of HC are printed with no other
#characters, no blanks, no newline ...
##important Hamming functions
def dataToHamming(d8):#d8 example: [0,0,0,0,0,0,0,0]
    dth = [0,0,0,0,0,0,0,0,0,0,0,0]
    dth[2] = d8[0]

    dth[4] = d8[1]
    dth[5] = d8[2]
    dth[6] = d8[3]
    dth[8] = d8[4]
    dth[9] = d8[5]
    dth[10] = d8[6]
    dth[11] = d8[7]
    if (dth[0] + dth[2] + dth[4] + dth[6] + dth[8] + dth[10]) % 2 != 0:
        dth[0] = 1
    if (dth[1] + dth[2] + dth[5] + dth[6] + dth[9] + dth[10]) % 2 != 0:
        dth[1] = 1
    if (dth[3] + dth[4] + dth[5] + dth[6] + dth[11]) % 2 != 0:
        dth[3] = 1
    if (dth[7] + dth[8] + dth[9] + dth[10] + dth[11]) % 2 != 0:
        dth[7] = 1
    return dth #The Hamming code corresponding to d8
def HammingToData(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0] [10010011]
    HCtodata = HC.copy()
    del HCtodata[0]
    del HCtodata[0]
    del HCtodata[1]
    del HCtodata[4]
    return HCtodata #The data byte corresponding to HC
def isHammingCorrect(HC):#HC example:[0,0,0,0,0,0,0,0,0,0,0,0]
    if (HC[0]+ HC[2] + HC[4] + HC[6] + HC[8]+ HC[10] ) % 2 == 0:
        if (HC[1] + HC[2] + HC[5] + HC[6] + HC[9] + HC[10]) % 2 ==0:
            if (HC[3] + HC[4] + HC[5] + HC[6] + HC[11]) % 2 == 0:
                if (HC[7] + HC[8] + HC[9] + HC[10] + HC[11]) % 2 == 0:
                    return True
    else:
        return False #True if HC is a valid Hamming code and False if it is not
def checkHammingGroups(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    errorgroups = []
    if (HC[0]+ HC[2] + HC[4] + HC[6] + HC[8]+ HC[10] ) % 2 != 0:
        errorgroups.append(1)
    if (HC[1] + HC[2] + HC[5] + HC[6] + HC[9] + HC[10]) % 2 !=0:
        errorgroups.append(2)
    if (HC[3] + HC[4] + HC[5] + HC[6] + HC[11]) % 2 != 0:
        errorgroups.append(4)
    if (HC[7] + HC[8] + HC[9] + HC[10] + HC[11]) % 2 != 0:
        errorgroups.append(8)
    return errorgroups #The return value is a list containing all the parity bits
#that show an error -
                 #  [1,2] would mean that parity groups 1 and 2 each had an odd
#number of 1's but that
                 #  groups 4 and 8 were correct.
                 #If the Hamming code is correct, the return value would be []
def makeCorrectedHamming(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    correctedhamming = HC.copy()
    eg = checkHammingGroups(HC)
    if len(eg) == 1:
        if 1 in eg:
            correctedhamming[0] = 1
        if 2 in eg:
            correctedhamming[1] = 1

    if 4 in eg:
        correctedhamming[3] = 1
    if 8 in eg:
        correctedhamming[7] = 1
    return correctedhamming
#else: #If HC can be corrected by changing one of its bits, the return value is
#return HC
#are more errors
#the return value is the same
#  the corrected Hamming Code.
# If HC is already a vaild code or if there
#  than can be corrected with a 1-bit change,
#  as the original HC
if __name__ == "__main__":
    #Here is a sample driver, add to it or replace it as you need
    dByte = inputData()
    print("testing inputData",dByte)
    HCIn = inputHamming()
    print("testing inputHamming",HCIn)
    dString = dataToString(dByte)
    print("testing dataToString",dString)
    HString = HammingToString(HCIn)
    print("testing HammingToString",HString)
    print(".",end='')
    printData(dByte)
    print(".")
    print(".",end='')
    printHamming(HCIn)
    print(".")
    HConverted = dataToHamming(dByte)
    DataConverted = HammingToData(HCIn)
    print("testing dataToHamming",HConverted)
    print("testing HammingToData",DataConverted)
    if isHammingCorrect(HCIn):
        print("isHammingCorrect reports correct")
    else:
        print("isHammingCorrect reports not correct")
    print("testing checkHammingGroups",checkHammingGroups(HCIn))
    print("testing makeCorrectedHamming",makeCorrectedHamming(HCIn))
