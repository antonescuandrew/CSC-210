import HammingUtilities
choice = 1
while choice == 1 or 2:
    print("1. Send a transmission")
    print("2. Recieve a transmission")
    print("3. Quit")
    choice = int(input("Choose an option by typing the number without the period."))
    if choice == 1:
        inputfile = open(input("Enter the name of the input file. "),'r')
        outputfile = open(input("Enter the name of the output file. "),'w')
        errorfile = open(input("Enter the name of the error file. "), 'w')
        for line in inputfile:
            if int(line) >= 0 and int(line) <= 255:
                numbinwithprefix = format(int(line),'#010b')
                numbin = numbinwithprefix[2:]
                binlist = [int(char) for char in str(numbin)]
                bintohamming = HammingUtilities.dataToHamming(binlist)
                hammingstring = HammingUtilities.HammingToString(bintohamming)
                outputfile.write(hammingstring)
                outputfile.write('\n')
            else:
                errorfile.write(line)
    if choice == 2:
        inputfile = open(input("Enter the name of the input file with one Hamming code per line. "), 'r')
        outputfile = open(input("Enter the name of the output file. "),'w')
        errorfile = open(input("Enter the name of the error file. "), 'w')
        for line in inputfile:
            strippedline = line.strip()
            hamminglist = [int(char) for char in (str(strippedline))]
            if HammingUtilities.isHammingCorrect(hamminglist) == True:
                hammingindata = HammingUtilities.HammingToData(hamminglist)
                datainstring = (HammingUtilities.dataToString(hammingindata))
                datanum = str(int(datainstring,2))
                outputfile.write(str(datanum))
                outputfile.write('\n')
            else:
                errorbits = HammingUtilities.checkHammingGroups(hamminglist)
                if len(errorbits) == 1:
                    correctedhamminglist = HammingUtilities.makeCorrectedHamming(hamminglist)
                    correctedhammingdata = HammingUtilities.HammingToData(correctedhamminglist)
                    correctedhammingstring = HammingUtilities.HammingToString(correctedhammingdata)
                    correctedhammingint = int(correctedhammingstring,2)
                    outputfile.write(str(correctedhammingint))
                    outputfile.write('\n')
                else:
                    hammingerrorstring = HammingUtilities.HammingToString(hamminglist)
                    errorfile.write(hammingerrorstring)
                    errorfile.write('\n')
    if choice == 3:
        break
    inputfile.close()
    outputfile.close()
    errorfile.close()
