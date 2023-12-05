# /heartbeat

import requests, json
import urllib3
import time
import config as cfg #config.py



# READ CONFIG
CLIENTID = cfg.API['CLIENTID']
SECRET = cfg.API['SECRET']
OAUTH_URL = cfg.API['OAUTH_URL']


# disable https warnings
urllib3.disable_warnings()

# Get OAuth2 token from Azure AD
data = {'grant_type': 'client_credentials', 'client_secret': SECRET, 'client_id' : CLIENTID, 'redirect_uri': ""}

# print("requesting access token")
access_token_response = requests.post(OAUTH_URL, data=data, verify=False, allow_redirects=False)

# SAMPLE OUTPUT:
# {'token_type': 'Bearer', 'expires_in': '3599', 'ext_expires_in': '3599', 'expires_on': '1577123924', 'not_before': '1577120024', 'resource': '00000002-0000-0000-c000-000000000000', 'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InBpVmxsb1FEU01LeGgxbTJ5Z3FHU1ZkZ0ZwQSIsImtpZCI6InBpVmxsb1FEU01LeGgxbTJ5Z3FHU1ZkZ0ZwQSJ9.eyJhdWQiOiIwMDAwMDAwMi0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9lN2I2YTY5MC1kMzIyLTQwODUtYjZkNi1kMGE0ZjcwZjBkN2IvIiwiaWF0IjoxNTc3MTIwMDI0LCJuYmYiOjE1NzcxMjAwMjQsImV4cCI6MTU3NzEyMzkyNCwiYWlvIjoiNDJWZ1lEQi9vVFN2VVdMend4TkhhMHVyL0RpOEFBPT0iLCJhcHBpZCI6IjMxNjBiMzBhLTczYzktNDllZS1iNGMwLWJmNTA3ZjlmZGJhNyIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2U3YjZhNjkwLWQzMjItNDA4NS1iNmQ2LWQwYTRmNzBmMGQ3Yi8iLCJvaWQiOiJjNzkzMzA4My0yNmUyLTQ1ODEtODNkYy00NjliZGY2YmM3ZjciLCJzdWIiOiJjNzkzMzA4My0yNmUyLTQ1ODEtODNkYy00NjliZGY2YmM3ZjciLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiTkEiLCJ0aWQiOiJlN2I2YTY5MC1kMzIyLTQwODUtYjZkNi1kMGE0ZjcwZjBkN2IiLCJ1dGkiOiJOeGxlQ1VZNzdFS2hrRGFxOEdueEFBIiwidmVyIjoiMS4wIn0.fDtWNRpAcznVLfbTNMW7NZ-0D435g80u7y2USdcGv3qUIBaysidhekt8ech8OKFJ17hTk8hYWUra8GUmuZ8_tMIZsqLA22dHhniJXkbEdhytzyIEQaaUlc1aP1TF9nxexLyG8jugzDJsAIHHCafvr-r6VBI_qZCr1pbylnUDtzsMafuEc2pxgrgUXylfdwlZAH8YlPFJUiukZHS14olfT61R6WjU4X1rlo_uhUWOLdEYTQhPAu_ndm0OBgJ4ciAW2JnbHm7yXEitNMFdxGHMwXCdWB8T0ycXpS0ZHAoQYRvXWy4RDvYbVvsx_zNqUSUWaif1BJs4vvnfLcQlh1IdcQ'}

# print(access_token_response)
res = access_token_response.json() #.access_token
# print(res)


# print("DEBUG: access_token = " + res["access_token"])

oauth_token = res["access_token"]

