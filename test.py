from module2 import getHitMessage
from configData import getConfigData
from stringFromCL import getStringFromCL

sanctionsList, matchPercentageQualifier = getConfigData('config.ini')

# Test suite


def main():
    testBusinessLogic()
    testConfigData()
    print('All tests passed!')


def testConfigData():
    assert getConfigData(
        'config.ini') == (['Kristopher Doe', 'Iceland', 'Royal Arctic Line'], 75)
    # Pass in wrong file name, defaults to original list
    assert getConfigData(
        'config.txt') == (['Kristopher Doe', 'Iceland', 'Royal Arctic Line'], 75)


def testBusinessLogic():
    # Test that all get 100% hit
    assert getHitMessage('Iceland', sanctionsList,
                         matchPercentageQualifier) == 'Hit with 100% match'
    assert getHitMessage('Kristopher Doe', sanctionsList,
                         matchPercentageQualifier) == 'Hit with 100% match'
    assert getHitMessage('Royal Arctic Line', sanctionsList,
                         matchPercentageQualifier) == 'Hit with 100% match'
    # Test with different characters to get a less than 100% hit
    assert getHitMessage('Icelaxd', sanctionsList,
                         matchPercentageQualifier) == 'Hit with 85% match'
    assert getHitMessage('Kristophre Doe', sanctionsList,
                         matchPercentageQualifier) == 'Hit with 92% match'
    assert getHitMessage('Royal Arctiz linz', sanctionsList,
                         matchPercentageQualifier) == 'Hit with 82% match'
    # Test less characters
    assert getHitMessage('KoistophreDoe', sanctionsList,
                         matchPercentageQualifier) == 'Hit with 81% match'
    # Test no hits
    assert getHitMessage('Izecadk', sanctionsList,
                         matchPercentageQualifier) == 'No Hit with 57% greatest match'
    assert getHitMessage('Icelxnz', sanctionsList,
                         matchPercentageQualifier) == 'No Hit with 71% greatest match'
    assert getHitMessage('alex', sanctionsList,
                         matchPercentageQualifier) == 'No Hit with 28% greatest match'
    assert getHitMessage('', sanctionsList,
                         matchPercentageQualifier) == 'No Hit with 0% greatest match'
    assert getHitMessage('!225', sanctionsList,
                         matchPercentageQualifier) == 'No Hit with 0% greatest match'
    # buffer overflow to consider, SQL injection attack


if __name__ == "__main__":
    main()
