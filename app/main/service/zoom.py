import time
import jwt
import json
import requests

# Enter your API key and your API secret
API_KEY = 'your_zoom_api_key'
API_SEC = 'your_api_secret'


def generateToken():
    token = jwt.encode(

        {"iss": API_KEY, "exp": time.time() + 5000},
        API_SEC,
        # Specify the hashing alg
        algorithm='HS256'
        # Convert token to utf-8
    ).decode('utf-8')

    return token


# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
                  "type": 2,
                  "start_time": "2019-06-14T10: 21: 57",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "agenda": "test",

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }


# send a request with headers including
def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))

    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]

    return join_URL, meetingPassword
