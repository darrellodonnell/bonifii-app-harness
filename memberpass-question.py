# source based on https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code
#
__author__ = "Darrell O'Donnell"
__copyright__ = "Copyright 2023, CULedger, LLC (dba Bonifii)"
__credits__ = ["BYU-bdm4"]
__license__ = "BSD-3-Clause"
__version__ = "1.0.1"
__maintainer__ = ""
__status__ = "beta"



# /heartbeat

import requests, json
import memberpassoauth as authtokens
import urllib3
import time
import argparse
import config as cfg #config.py



# READ CONFIG
CLIENTID = cfg.API['CLIENTID']
SECRET = cfg.API['SECRET']
TENANTID = cfg.API['TENANTID']
MEMBERPASS_URL = cfg.API['MEMBERPASS_URL']
OAUTH_URL = cfg.API['OAUTH_URL']

parser = argparse.ArgumentParser(description='Sends SimpleAuthenticate challange via MemberPass Identity API')
parser.add_argument("--m", default="test1234", help="memberId - do NOT use internally signficant identier.")
# parser.add_argument("--p", help="10-digit (North American) phone number that will be invited")

args = parser.parse_args()
memberId = args.m

# build headers (and get OAuth token) and data payload for upcoming http POST to CULedger.Identity for Onboarding.
headers = {'Content-Type': 'application/json',
           # 'Prefer':'respond-async', #remove comment for async
           'Authorization': 'Bearer ' + authtokens.oauth_token}


start_time = time.time()

# ONBOARD TEST

question = {
  "messageId": "42",
  "messageQuestion": "Are you on the phone with _______?",
  "messageTitle": "CU is asking you a question",
  "messageText": "Our system needs to make sure that you are on the phone with one of our operators. We do this to protect you and your accounts at the credit union.",
  "positiveOptionText": "Yes, it is me.",
  "negativeOptionText": "No. I am NOT. That is not me.",
  "expires": "2023-12-21T02:50:13.334Z"
}
print(question)

onboardEndpoint ="{}member/{}/authenticateSimple".format(MEMBERPASS_URL, memberId)
print(onboardEndpoint)
response = requests.post(onboardEndpoint, data=json.dumps(question), headers=headers)
print("Invitation Response:")

print(response)
print(response.text)
print(response.json())


end_time = time.time()




print("TIME in API (start to end): ")
print(end_time - start_time)
