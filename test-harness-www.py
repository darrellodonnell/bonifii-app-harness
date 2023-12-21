from flask import Flask, request, send_file, render_template, redirect, url_for, g, jsonify 
import requests
import qrcode
from io import BytesIO
import json
from flask_moment import Moment
from jinja2 import Environment
import memberpassoauth as authtokens # MemberPass OAuth token tooling
import config 

jinja_env = Environment(extensions=['jinja2_iso8601.ISO8601Extension'])


app = Flask(__name__)
moment = Moment(app)


# app.config["status"] = "AZURE"

run = "LOCAL"


# MemberPass API specifics
CLIENTID = config.API['CLIENTID']
SECRET = config.API['SECRET']
TENANTID = config.API['TENANTID']
MEMBERPASS_URL = config.API['MEMBERPASS_URL']
OAUTH_URL = config.API['OAUTH_URL']


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.config["status"] = "AZURE"
app.config["memberpasshost"] = "unknown"

# Merge the config.py values in...
if run == "LOCAL":
  app.config = app.config | config.local  
else:
  app.config = app.config | config.azure




print(app.config)


@app.context_processor
def inject_host_and_more():
    return dict(acapyhost=app.config["acapyhost"], status=app.config["status"])


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/invite-memberpass/<memberId>')
def invite_memberpass(memberId):
  return render_template("invite-memberpass.html", memberId=memberId)

@app.route('/invite-oob')
def invite_oob():
  return render_template("invite-oob.html")

@app.route('/invite-connections')
def invite_connections():
  return render_template("invite-connections.html")

#TODO: Move calls into another file.

@app.route('/connection/<connectionid>')
def connectiondetail(connectionid):
   return render_template("connection-detail.html", connectionid=connectionid)

@app.route('/connections')
def connections():
  host = app.config["acapyhost"]
  url = host + f"/connections" 
  print(url)
  response = requests.get(url)
  # print(response)
  connections = response.json()
  return render_template("connections.html",connections=connections)

@app.route('/memberpasstest')
def memberpasstest():
  members = ["iOS-test1"]  # test data
  return render_template("memberpasstest.html",members=members)

@app.route('/questions')
def questions():
  host = app.config["acapyhost"]
  url = host + f"/qa/get-questions" 
  print(url)
  response = requests.get(url)
  # print(response)
  questions = response.json()
  return render_template("questions.html",questions=questions)





@app.route('/question-delete/<threadid>')
def deletequestion(threadid):
  host = app.config["acapyhost"]
  url = host + f"/qa/" + threadid 
  print(url)
  response = requests.delete(url)
  print(response)
   # if successful
  return redirect(url_for('questions'))


@app.route('/connection-delete/<connectionid>')
def deleteconnection(connectionid):
  host = app.config["acapyhost"]
  url = host + f"/connections/" + connectionid 
  print(url)
  response = requests.delete(url)
  print(response)
   # if successful
  return redirect(url_for('connections'))

@app.route('/memberpass-simpleauthenticate/<memberId>')
def simpleauthenticate(memberId):
  headers = {'Content-Type': 'application/json',
           # 'Prefer':'respond-async', #remove comment for async
           'Authorization': 'Bearer ' + authtokens.oauth_token}
  
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
  json_payload = json.dumps(question)
  print(json_payload)


  
  onboardEndpoint ="{}member/{}/authenticateSimple".format(MEMBERPASS_URL, memberId)
  print(onboardEndpoint)

  response = requests.put(onboardEndpoint, data=json.dumps(question), headers=headers)
  print("Invitation Response:")
  print(response)
  print("JSON:")
  print(response.json())

  return redirect(url_for('memberpasstest'))

@app.route('/sendqa/<connectionid>')
def sendqa(connectionid):
  payload = {
    "@type": "https://didcomm.org/questionanswer/1.0/question",
    "question_text": "MemberPass CU has a question.",
    "question_detail": "Do you love MemberPass?",
    "valid_responses": [
      {"text": "YES"},
      {"text": "no"}
    ]
  }
  json_payload = json.dumps(payload)
  print(json_payload)

  host = app.config["acapyhost"]
  url = host + f"/qa/" + connectionid + f"/send-question"

  response = requests.post(url, json=payload)
  print(response)

  return redirect(url_for('connections'))

@app.route('/sendcred/<connectionid>')
def sendcred(connectionid):
  payload = {
    "auto_issue": True,
    "comment": "My MemberPass",
    "connection_id": connectionid,
    "credential_preview": {
      "@type": "issue-credential/2.0/credential-preview",
      "attributes": [
        {
          "name": "Institution",
          "value": app.config["finame"]
        },
        {
          "name": "CredentialName",
          "value": "MemberPass"
        }, 
        {
          "name": "CredentialDescription",
          "value": "description"
        },
        {
          "name": "MemberSince",
          "value": "1989"
        },
        {
          "name": "InstitutionID",
          "value": "NCUA:DEMO1234"
        },
        {
          "name": "CertificateID",
          "value": "cert:4567"
        }
      ] 
    },
    "filter": {
      "indy": {
        "cred_def_id": app.config["creddef"] 
      }
    } 
  }

  json_payload = json.dumps(payload)
  print(json_payload)

  host = app.config["acapyhost"]
  url = host + f"/issue-credential-2.0/send-offer"

  response = requests.post(url, json=payload)
  print(response)

  return redirect(url_for('connections'))

@app.route('/invite/qr-memberpass.png')
def generateqrmemberpass():

  headers = {'Content-Type': 'application/json',
           # 'Prefer':'respond-async', #remove comment for async
           'Authorization': 'Bearer ' + authtokens.oauth_token}

  # memberId passed as URL Parameter (e.g. ".../invite/qr-memberpass.png?memberId=1234")
  memberId = request.args.get('memberId')
  print("memberId passed as: " + memberId)

  payload = {"memberId": memberId,
    "phoneNumber": "5555551212",
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
  
  onboardEndpoint ="{}member/{}/createInvitation".format(MEMBERPASS_URL, memberId)
  print(onboardEndpoint)
  response = requests.post(onboardEndpoint, data=json.dumps(payload), headers=headers)
  print("Invitation Response:")
  print(response)
  print("JSON:")
  print(response.json())



  jsonresponse = response.json()
  # print(jsonresponse)

  invitation_url = jsonresponse["invitationUrl"]
  print("invitation_url = " + invitation_url)
 
  # Generate a QR code
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )

  # Set the data
  qr.add_data(invitation_url)
  qr.make(fit=True) # Generate the QR code
  img = qr.make_image(fill_color="black", back_color="white") # Get the QR code as a PNG image

  byteIO = BytesIO()
  img.save(byteIO, 'PNG')
  byteIO.seek(0)
  return send_file(byteIO, mimetype='image/png')

@app.route('/invite/qr-connections.png')  # This is the homepage
def generateqrconnection():
   # get the URL from the server for an invite.
  payload = {
    "my_label": app.config["finame"]
  }
  
  json_payload = json.dumps(payload)

  #= "https://f331a436996c.ngrok.app"
  # host = "http://4.157.130.159:11000"

  host = app.config["acapyhost"]

  url = host + f"/connections/create-invitation"

  response = requests.post(url, json=payload)
  print(response)

  jsonresponse = response.json()
  # print(jsonresponse)

  invitation_url = jsonresponse["invitation_url"]
  print("invitation_url = " + invitation_url)
  # Generate a QR code
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  # Set the data
  qr.add_data(invitation_url)
  # Generate the QR code
  qr.make(fit=True)

  # Get the QR code as a PNG image
  img = qr.make_image(fill_color="black", back_color="white")

  byteIO = BytesIO()
  img.save(byteIO, 'PNG')
  byteIO.seek(0)
  return send_file(byteIO, mimetype='image/png')
   

@app.route('/invite/qr-oob.png')  # This is the homepage
def generateqroob():
  # get the URL from the server for an invite.
  payload = {
      "handshake_protocols":
        ["did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0"],
      "metadata": {},
      "my_label": app.config["finame"] 
  }


  # print(payload + "\n")

  json_payload = json.dumps(payload)
  print("SENDING: \n" + json_payload)


  #= "https://f331a436996c.ngrok.app"
  # host = "http://4.157.130.159:11000"

  host = app.config["acapyhost"]

  url = host + f"/out-of-band/create-invitation"

  response = requests.post(url, json=payload)
  # print(response)

  jsonresponse = response.json()
  print("FULL JSON received:" )

  print(jsonresponse)
  invitation_url = jsonresponse["invitation_url"]
  print("invitation_url = " + invitation_url)
  
  # Generate a QR code
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )

  # Set the data
  qr.add_data(invitation_url)

  # Generate the QR code
  qr.make(fit=True)

  # Get the QR code as a PNG image
  img = qr.make_image(fill_color="black", back_color="white")

  byteIO = BytesIO()
  img.save(byteIO, 'PNG')
  byteIO.seek(0)
  return send_file(byteIO, mimetype='image/png')


# def index():
#     return render_template(
#         'index.html'
#     )  # The spot where it says 'index.html' is what HTML file loads.


if __name__ == '__main__':
    app.run(port=2048, debug=True)
