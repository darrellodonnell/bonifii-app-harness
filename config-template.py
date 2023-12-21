# COPY this file to config.py and fill out required parameters (all under API)
# config.py is in .gitignore and should not be checked in.
#
# main API parameters
#
#
API = {
    "CLIENTID": "-----",
    "SECRET": "-----",
    "TENANTID": "-----",
    "MEMBERPASS_URL": "-----",
    "OAUTH_URL": "-----"
}



local = dict(
  acapyhost = "https://SAMPLE.ngrok.app",
  agentDID = "DID-GOES-HERE",
  creddef = "DID-GOES-HERE:3:CL:178678:tag1",
  finame = "LOCAL Demo CU"
)

azure = dict(
  acapyhost = "http://ACAPYSERVER.COM:11000",
  agentDID = "Enn9uVvmfXTnSGWpk19Tju",
  creddef = "Enn9uVvmfXTnSGWpk19Tju:3:CL:178678:tag1",
  finame = "_____ Demo CU"
)

