import qrcode
import json
import time
import requests
import sys

# TODO:

# test OOB invitation object(JSON object)
# test OOV invitation_url object


# DO NOT ALLOW re-use (spam; security risk; etc.)

# get connectionId from input

# if "--connectionId" not in sys.argv:
#   connection_id = "unknown"
#   connection_id = input("Enter connection id: ")
# else:
#   connection_id_index = sys.argv.index("--connectionId")
#   connection_id = sys.argv[connection_id_index + 1]

# payload = {
#     "handshake_protocols": [
#       "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0"
#     ],
#     "metadata": {},
#     "my_label": "Bubbaz CU",
#     "use_public_did": "true"
# }

payload = {
    "handshake_protocols": [
      "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0"
    ],
    "metadata": {},
    "my_label": "Bubbaz CU"
}


# {
#     "question_detail": "Do you love MemberPass?",
#     "question_text": "Question from MemberPass.",
#     "valid_responses": [{
#         "text": "yes"
#     }, {
#         "text": "no"
#     }]
# }

import json

json_payload = json.dumps(payload)


print(json_payload)
# https://c8b7fb092ffa.ngrok.app - DARRELL LOCAL
# http://4.157.130.159:11000

# host = "https://f331a436996c.ngrok.app"
host = "http://4.157.130.159:11000"

url = host + f"/out-of-band/create-invitation"
#url = host + f"/connections/create-invitation"

print("\nHitting URL: " + url)

response = requests.post(url, json=payload)

print("RESPONSE:")
print(response.text)
print("\n")



# invitation = {
#     "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/out-of-band/1.1/invitation",
#     "@id": "d6a87261-ef87-4ad4-9124-16c62b18de0b",
#     "label": "Bubbaz CU",
#     "handshake_protocols": [
#       "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0"
#     ],
#     "services": [
#       "did:sov:Enn9uVvmfXTnSGWpk19Tju"
#     ]
#   }


# img = qrcode.make(invitation)
# type(img)  # qrcode.image.pil.PilImage
# img.save("/Users/darrellodonnell/tmp/qr-oob-invitation.png")