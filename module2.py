# Alex Bushinsky
# InsideSherpa Module 2

# Command line implementation

from stringFromCL import getStringFromCL as getPayeeInfo
from configData import getConfigData
from businessLogic import getHitMessage


def main():
    # Read in user input from command line
    payeeString = getPayeeInfo()
    # Read in config input
    sanctionsList, matchPercentageQualifier = getConfigData('config.ini')
    # Perform logic, deterimine if there's a hit
    print(getHitMessage(payeeString, sanctionsList, matchPercentageQualifier))


if __name__ == "__main__":
    main()
