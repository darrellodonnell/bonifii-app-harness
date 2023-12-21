
# OUTCOME

Getting 


# Running  Locally

There are several components that are needed to run locally:
* Enterprise ACA-Py agent - runs in Docker
* `listener.py` - provides a console-based webhook listener
* `test-harness-www.py` - web test page (uses Flask)

## STEP 1 - run ngrok to get URLs that will be needed for running locally.

From the project folder (or type path to ngrok-config.yml):

`$ ngrok start --all --config ngrok-config.yml `

Sample (note: the order of the ports may change. The subdomains WILL change every time you run ngroky): 
```
Web Interface                 http://127.0.0.1:4040                                                           
Forwarding                    https://4a0a09025a0e.ngrok.app -> http://localhost:8000                         
Forwarding                    https://5c511ac7ced3.ngrok.app -> http://localhost:11000                        
Forwarding                    https://6e62472a2eda.ngrok.app -> http://localhost:5000 
```

All three of the `*.ngrok.app` subdomains will be needed.

## STEP 2 - Update Docker `config.yml` 

Update both of the following parameters:
* `endpoint` port 8000
  e.g. 
  ```
  # Transport 
  inbound-transport:
    - [http, 0.0.0.0, 8000] 
  outbound-transport: http 
  endpoint:
    - https://4a0a09025a0e.ngrok.app #port 8000 ngrok
  
  ```
* `webhook-url` port 5000
e.g. 
  ```
  webhook-url: https://6e62472a2eda.ngrok.app/webhook
  ```
Build and deploy the image, then run it. 
```
$ docker build -t endorser-issuer-askar .
```

Now Deploy the Container and run (tying ports 11000:11000 and 8000:8000)


## STEP 3 - Update `config.py`

Update the `app.config["acapyhost"]` value.

```
local = dict(
  acapyhost = "https://5c511ac7ced3.ngrok.app",
  agentDID = "X4eo8b2NLAvoFfgyuKKQzF",
  creddef = "X4eo8b2NLAvoFfgyuKKQzF:3:CL:178678:tag1",
  finame = "Bonifii Demo CU"
)
```

## STEP 


The following addresses are critical:

###Enterprise-Agent
* API - port 11000 on server (Docker) 
* main server - port 8000 on server (Docker)
  - update config.yml with the ngrok address for port 8000
In the ngrok console you will see:
```
Forwarding                    https://19cdbf1cb1ed.ngrok.app -> http://localhost:8000   
```

```
endpoint:
  - https://19cdbf1cb1ed.ngrok.app 
```


###Webhooks
* webhook - port 5000 on server
```
Forwarding                    https://adb0b3f39b24.ngrok.app -> http://localhost:5000 
```
NOTE the `listener.py` system here uses the `/webhook` path to receive webhooks.

e.g.
```
webhook-url: https://f63f25bc2489.ngrok.app/webhook
```

ngrok is configured 

You're going to need the following:
* `localhost` bound to ports:
  * `:8000 bound to the `acapy-endorser-issuer` container port `8000`
  * port `11000`
* DB running at IP address specified in `./acapy-endorser-issuer/config.yml`

* Database - PostgreSQL is used in its own container. 
```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres:10
```

# postgre - access

command line: 

```
docker exec -it hopeful_lehmann psql -U postgres -W
```

# ngrok Usage

```
ngrok http --domain=accurately-perfect-duck.ngrok-free.app 8000
```



Mediator:


# TODO:
* get `askar` back into play (backed off to indy)
* new Dockerfile
* Mediator
* instructions to 
* update ACA-Py QA module - separating @id and clearly indicating that @threadid is returning whatever is sent (or providing an @threadid)
* Provisioning via script (.py) for Public DID, as opposed to `autoprovision=true` in Dockerfile.


DSR Requires:
* advise DSR about BCovrin - TestNet for now - GENESIS
* Mediator Agent - invitation, to be hardcoded - hardcoding what? QR Code output 
* Push/Firebase
* Dropbox - 

Finiviation:
* CONFIG - for webhook endpoint. Send payload on request (e.g. authenticate) and receive them back...
  * webhook - https://serv
* 

* ACA-y

* ACA-Py Mediator


# BCovrin Testnet

* Link: http://test.bcovrin.vonx.io



## CREATE SCHEMA

#138800


XgHi8cka1BY2TY5n9gKnBw:2:MemberPass:1.0

XgHi8cka1BY2TY5n9gKnBw:2:MemberPass:1.1


### Payload for Creating Schema (`POST /schemas`)
```
{
  "schema_name": "MemberPass",
  "schema_version": "1.0",
  "attributes":[
    "Institution", 
    "CredentialName",
    "CredentialDescription",
    "MemberSince",
    "InstitutionID",
    "CertificateID"
  ]
}
```
returns
```
Enn9uVvmfXTnSGWpk19Tju:2:MemberPass:1.0
```
seqno:  178678



### Create Cred Def Payload (`POST /credential-definitions`)
NOTE: `tag1` is present for unknown but historical reasons. 
```
{
  "schema_id": "Enn9uVvmfXTnSGWpk19Tju:2:MemberPass:1.0",
  "tag": "tag1"
}
```

#### response:
```
{
  "sent": {
    "credential_definition_id": "Enn9uVvmfXTnSGWpk19Tju:3:CL:178678:tag1"
  },
  "credential_definition_id": "Enn9uVvmfXTnSGWpk19Tju:3:CL:178678:tag1"
}
```


## Provision (`POST /wallet/did/create`):

payload: 
```
{
  "method": "sov",
  "seed": "dN!igcvKWrw6otpWy4ct8G8KfJUQsZM2"
}
```

response:
```
{
  "result": {
    "did": "Enn9uVvmfXTnSGWpk19Tju",
    "verkey": "8WuaNUkjrqmHZ8mjd1UEDrPArvDzDYi5fdKNWU46pn68",
    "posture": "wallet_only",
    "key_type": "ed25519",
    "method": "sov"
  }
}
```

## Assign Public DID for Agent (`POST /wallet/did/public/`)



`403: No ledger available`


"XgHi8cka1BY2TY5n9gKnBw:3:CL:138800:tag1"

SeqNo: #138900