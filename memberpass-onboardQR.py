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

parser = argparse.ArgumentParser(description='Simple heartbeat utility to test MemberPass Identity API')
parser.add_argument("--m", default="test1234", help="memberId - do NOT use internally signficant identier.")
# parser.add_argument("--p", help="10-digit (North American) phone number that will be invited")

args = parser.parse_args()
memberId = args.m


# # Get OAuth2 token from Azure AD


# data = {'grant_type': 'client_credentials', 'client_secret': SECRET, 'client_id' : CLIENTID, 'redirect_uri': ""}

# print("requesting access token")
# access_token_response = requests.post(OAUTH_URL, data=data, verify=False, allow_redirects=False)

# # SAMPLE OUTPUT:
# # {'token_type': 'Bearer', 'expires_in': '3599', 'ext_expires_in': '3599', 'expires_on': '1577123924', 'not_before': '1577120024', 'resource': '00000002-0000-0000-c000-000000000000', 'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InBpVmxsb1FEU01LeGgxbTJ5Z3FHU1ZkZ0ZwQSIsImtpZCI6InBpVmxsb1FEU01LeGgxbTJ5Z3FHU1ZkZ0ZwQSJ9.eyJhdWQiOiIwMDAwMDAwMi0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9lN2I2YTY5MC1kMzIyLTQwODUtYjZkNi1kMGE0ZjcwZjBkN2IvIiwiaWF0IjoxNTc3MTIwMDI0LCJuYmYiOjE1NzcxMjAwMjQsImV4cCI6MTU3NzEyMzkyNCwiYWlvIjoiNDJWZ1lEQi9vVFN2VVdMend4TkhhMHVyL0RpOEFBPT0iLCJhcHBpZCI6IjMxNjBiMzBhLTczYzktNDllZS1iNGMwLWJmNTA3ZjlmZGJhNyIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2U3YjZhNjkwLWQzMjItNDA4NS1iNmQ2LWQwYTRmNzBmMGQ3Yi8iLCJvaWQiOiJjNzkzMzA4My0yNmUyLTQ1ODEtODNkYy00NjliZGY2YmM3ZjciLCJzdWIiOiJjNzkzMzA4My0yNmUyLTQ1ODEtODNkYy00NjliZGY2YmM3ZjciLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiTkEiLCJ0aWQiOiJlN2I2YTY5MC1kMzIyLTQwODUtYjZkNi1kMGE0ZjcwZjBkN2IiLCJ1dGkiOiJOeGxlQ1VZNzdFS2hrRGFxOEdueEFBIiwidmVyIjoiMS4wIn0.fDtWNRpAcznVLfbTNMW7NZ-0D435g80u7y2USdcGv3qUIBaysidhekt8ech8OKFJ17hTk8hYWUra8GUmuZ8_tMIZsqLA22dHhniJXkbEdhytzyIEQaaUlc1aP1TF9nxexLyG8jugzDJsAIHHCafvr-r6VBI_qZCr1pbylnUDtzsMafuEc2pxgrgUXylfdwlZAH8YlPFJUiukZHS14olfT61R6WjU4X1rlo_uhUWOLdEYTQhPAu_ndm0OBgJ4ciAW2JnbHm7yXEitNMFdxGHMwXCdWB8T0ycXpS0ZHAoQYRvXWy4RDvYbVvsx_zNqUSUWaif1BJs4vvnfLcQlh1IdcQ'}

# print(access_token_response)
# res = access_token_response.json() #.access_token
# print(res)
#print(access_token_response.json())

# print("DEBUG (main python): access_token " + authtokens.oauth_token)

# oauth_token = res["access_token"]

# build headers and data payload for upcoming http POST to CULedger.Identity for Onboarding.
headers = {'Content-Type': 'application/json',
           # 'Prefer':'respond-async', #remove comment for async
           'Authorization': 'Bearer ' + authtokens.oauth_token}


start_time = time.time()

# ONBOARD TEST

onboardData = {"memberId": memberId,
                                "phoneNumber": "6138668904",
                                "emailAddress": "bubba@mailnesia.com",
                                "displayTextFromFI": "Let's get connected via MemberPass!",
                                "credentialData": {
                                    "CredentialId": "--",
                                    "CredentialDescription": "--",
                                    "Institution": "--",
                                    "CredentialName": "--",
                                    "MemberNumber": memberId,
                                    "MemberSince": "--"
                                }
                             }
print(onboardData)

onboardEndpoint ="{}member/{}/createInvitation".format(MEMBERPASS_URL, memberId)
print(onboardEndpoint)
response = requests.post(onboardEndpoint, data=json.dumps(onboardData), headers=headers)
print("Invitation Response:")

print(response)
print(response.text)
print(response.json())


# # HEARTBEAT TEST...
# heartbeatEndpoint = "{}heartbeat".format(MEMBERPASS_URL)
# print(heartbeatEndpoint)
# response = requests.post(heartbeatEndpoint, data=json.dumps(onboardData), headers=headers)
# print("Heartbeat Response:")

end_time = time.time()




print("TIME in API (start to end): ")
print(end_time - start_time)


# print 'body: ' + access_token_response.text
#
# # we can now use the access_token as much as we want to access protected resources.
# tokens = json.loads(access_token_response.text)
# access_token = tokens['access_token']
# print "access token: " + access_token
#
# api_call_headers = {'Authorization': 'Bearer ' + access_token}
# api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
#
# print api_call_response.text