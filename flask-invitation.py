from flask import Flask, request, send_file, render_template, redirect, url_for, g, jsonify 
import requests
import qrcode
from io import BytesIO
import json
from flask_moment import Moment
from jinja2 import Environment

jinja_env = Environment(extensions=['jinja2_iso8601.ISO8601Extension'])


app = Flask(__name__)
moment = Moment(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.config["status"] = "LOCAL"
app.config["memberpasshost"] = "unknown"
# app.config["status"] = "AZURE"

if app.config["status"] == "LOCAL":
  app.config["acapyhost"] = "https://f331a436996c.ngrok.app"
  app.config["agentDID"] = "X4eo8b2NLAvoFfgyuKKQzF"
  app.config["creddef"] = "X4eo8b2NLAvoFfgyuKKQzF:3:CL:178678:tag1"
  app.config["fi-name"] = "D-Local CU"
else:
  app.config["acapyhost"] = "http://4.157.130.159:11000"
  app.config["agentDID"] = "Enn9uVvmfXTnSGWpk19Tju"
  app.config["creddef"] = "Enn9uVvmfXTnSGWpk19Tju:3:CL:178678:tag1"
  app.config["fi-name"] = "Bonifii Demo CU"

 
# 







# X4eo8b2NLAvoFfgyuKKQzF:3:CL:178678:tag1

# app.config["acapyhost"] = "http://4.157.130.159:11000"
# app.config["connectionlogo"] = "https://culedger.s3.amazonaws.com/MemberPass512x512.png"

#TODO: Move to use config file with LOCAL/REMOTE API endpoints

@app.context_processor
def inject_host_and_more():
    return dict(acapyhost=app.config["acapyhost"], status=app.config["status"])


@app.route('/')
def index():
   return render_template("index.html")

@app.route('/invite-memberpass')
def invite_memberpass():
  return render_template("invite-memberpass.html")

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
          "value": app.config["fi-name"]
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
   # get the URL from the server for an invite.
  payload = {
    "my_label": app.config["fi-name"]
  }
  
  json_payload = json.dumps(payload)

  #= "https://f331a436996c.ngrok.app"
  # host = "http://4.157.130.159:11000"

  host = app.config["memberpasshost"]

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

@app.route('/invite/qr-connections.png')  # This is the homepage
def generateqrconnection():
   # get the URL from the server for an invite.
  payload = {
    "my_label": app.config["fi-name"]
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
      "my_label": app.config["fi-name"] 
  }


  # print(payload + "\n")

  json_payload = json.dumps(payload)
  print(json_payload)


  #= "https://f331a436996c.ngrok.app"
  # host = "http://4.157.130.159:11000"

  host = app.config["acapyhost"]

  url = host + f"/out-of-band/create-invitation"

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


# def index():
#     return render_template(
#         'index.html'
#     )  # The spot where it says 'index.html' is what HTML file loads.


if __name__ == '__main__':
    app.run(port=2048, debug=True)
