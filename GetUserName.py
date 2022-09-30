print("Get username")

import requests
import json

from GetToken import get_auth0_token

URL = ""

TEAMNAME = 'CLS'

access_token = get_auth0_token()




f = open('data.json')
inputData = json.load(f)

outputObject = []

for loan in inputData:
    print(loan['loanNumber'])
    PARAMS = {'address':TEAMNAME, 'loanNumber':loan['loanNumber']}
    HEADERS = {
        'Authorization'
    : 'Bearer ' + access_token }

    r = requests.get(url = URL, params = PARAMS, headers=HEADERS)

    if (r.status_code == 200):
        data= r.json()

        print(data[0])

        outputObject.append(data[0])
    else:
        data = {
            "loanNumber" : loan['loanNumber'],
            "StatusCode" : r.status_code
        }
        outputObject.append(data)

    # # Serializing json
    json_object = json.dumps(outputObject, indent=4)

    # Writing to sample.json
    with open("output.json", "w") as outfile:
        outfile.write(json_object)

