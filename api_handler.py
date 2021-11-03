import requests
import ast


def get_request(url='https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta'):
    '''
    Makes a GET request to the url and returns the received json
    '''
    r = requests.get(url)
    return r.json()


def get_tosses(url='https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta'):
    '''
    Gets the list of tosses from the body and converts it to a list
    '''
    request_json = get_request(url)
    return ast.literal_eval(request_json["body"])
