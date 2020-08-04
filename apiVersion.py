from flask import Flask, jsonify
from configData import getConfigData
from module2 import getHitMessage

app = Flask(__name__)


@app.route('/screen/<name>', methods=['GET'])
def get_product(name):
    # Read in config input
    sanctionsList, matchPercentageQualifier = getConfigData('config.ini')
    # Perform logic, deterimine if there's a hit
    # santize input
    return jsonify(getHitMessage(name, sanctionsList, matchPercentageQualifier))


# Run server
if __name__ == '__main__':
    app.run(debug=True)
