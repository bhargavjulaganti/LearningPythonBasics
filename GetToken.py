import requests


def get_auth0_token():

    requestBody = {
        "client_id": "",
        "client_secret": "",
        "audience": "",
        "grant_type": "client_credentials"
    }

    # Making a POST request
    r = requests.post('', requestBody)

    if (r.status_code == 200):
        responseBody = r.json()
        return responseBody['access_token']
    else:
        raise Exception("Error while retrieving access token with status code :" + str(r.status_code))