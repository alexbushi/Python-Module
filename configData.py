# Library to read config file
import configparser

# Initialize config library
configPars = configparser.ConfigParser()


def getConfigData(configFileName):
    '''Takes in nothing, returns a list of strings that are the sanctioned names and match percentage parameter as tuple'''

    # List of strings
    sanctionsList = []
    matchPercentageQualifier = 75

    try:
        configPars.read(configFileName)

        try:
            sanctionsList = configPars['default']['sanctionList'].split(",")
        except:
            print('Could not load sanctions list, defaulting to empty list')

        try:
            matchPercentageQualifier = int(
                configPars['default']['matchPercentageQualifier'])
        except:
            print('Could not load match percentage, defaulting to 75%')
    except FileNotFoundError as e:
        print(e)
    return sanctionsList, matchPercentageQualifier
