'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually 
spelled out with letters: one, two, three, four, five, six, seven, eight, and nine 
also count as valid "digits".

Equipped with this new information, you now need to find the real first and last 
digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
'''

inputfile = open('input.txt', 'r')
Lines = inputfile.readlines()

#numlist = ["0","1","2","3","4","5","6","7","8","9"]
stringnumlist = ("zero","one","two","three","four","five","six","seven","eight","nine")



def scanline(line):
    numstore = {}  # Temp dictionary

    # Go through each tuple of string number and search for it in the line. Grab the start index as well as numeric value.
    # First if statement is left to right search, second if statement is right to left search.  Assign index and value to numstore dict 
    for i in stringnumlist:
        if i in line:
            if line.index(i) not in numstore:
                numstore[line.index(i)] = str(stringnumlist.index(i))
            if line.rindex(i) not in numstore:
                numstore[line.rindex(i)] = str(stringnumlist.index(i))

        numeric = str(stringnumlist.index(i))
        if numeric in line:
            if line.index(numeric) not in numstore:
                numstore[line.index(numeric)] = numeric
            if line.rindex(numeric) not in numstore:
                numstore[line.rindex(numeric)] = (numeric)

    # Grab the min index and assign value to first digit, grab the max index and assign value to last digit
    firstDigit = numstore[min(numstore,key=int)]
    lastDigit = numstore[max(numstore,key=int)]

    return firstDigit,lastDigit

def main():
    calibrationValue = 0  # Variable to hold accumlated calibration value
    for line in Lines:
        firstdigit,lastdigit = scanline(line)
        digits = str(firstdigit) + str(lastdigit) 
        #print("digits = ",digits)
        intdigits = int(digits)  # Convert string digits to integer
        calibrationValue += intdigits  # Add int value to calibrationValue
    print("Calibration Values = ",calibrationValue)

if __name__ == '__main__':
    main()

