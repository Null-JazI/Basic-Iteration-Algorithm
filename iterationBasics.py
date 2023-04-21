import random

# Function takes input values which is fed to randNum.
def userInp():
    while(1):
        lotNum = input("Enter a whole number from range 1-999: ")
        if isInt(lotNum)==False:
            print("")
            print("Please print a whole number!")
            print("")
        elif isInt(lotNum)==True:
            if int(lotNum) > 1000 or int(lotNum) < 0:
                print("")
                print("Please enter a number in the range 1-999!")
                print("")
            else:
                break
    return int(lotNum)

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# randNum generates random numbers until your number is chosen
def randNum(y):
    count = 0
    while(1):
        generator = random.randint(1,999)
        count += 1
        if generator == y:
            print("Your number has been found after " + str(count) + " iterations.")
            break

def main():
    lottoNum = userInp()
    randNum(lottoNum)
main()
