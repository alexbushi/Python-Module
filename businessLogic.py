import sys
from difflib import SequenceMatcher

# Wrapper that can be used regardless of input source


def getHitMessage(payeeString, sanctionsList, matchPercentageQualifier):
    '''takes in a string, list of strings, and an int, returns a message as a string'''

    gotAHit, matchPercentage = checkIfHit(payeeString,
                                          sanctionsList, matchPercentageQualifier)
    if gotAHit:
        return 'Hit with {}% match'.format(matchPercentage)
    else:
        return 'No Hit with {}% greatest match'.format(matchPercentage)


def checkIfHit(payeeString, sanctionsList, matchPercentageQualifier):
    '''Helper function, takes in a string, and list of strings, returns hit or no hit'''

    matchPercentage = 0
    # Used for printing only, no logic
    greatestmatchPercentage = 0

    for index in range(len(sanctionsList)):
        # Convert to integer
        matchPercentage = int(
            (SequenceMatcher(None, payeeString, sanctionsList[index]).ratio()) * 100)
        # Only used for printing, no logic
        if (matchPercentage > greatestmatchPercentage):
            greatestmatchPercentage = matchPercentage

        # determined if % of match qualifies as sanctioned or not
        if (matchPercentage >= matchPercentageQualifier):
            return True, matchPercentage
        else:
            continue

    return False, greatestmatchPercentage
