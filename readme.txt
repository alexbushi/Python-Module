Alex Bushinsky
Inside Sherpa Module 2

Feedback Incorporated from Module 1
-Included negative unit tests
-Included configuration file to hold list of sanctions and hit qualifier percentage
-Included input validation, including try catch when reading from config file
-Separated business logic code from other code using different files
-More detailed variable names
-Created different methods to provide input to the program
    -Command Line
    -API Endpoint


Input: string representing payee name
Output: Returns a hit or no hit message along with % match of payee string with any entity in the sanctions list

Command Line Instructions
1) python module2.py "payeeString"

API Endpoint Instructions
1) pipenv shell
2) pipenv install flask
3) python apiVersion.py
4) navigate to localhost5000:/screen/"payeeString"

Test Instructions
1) python test.py