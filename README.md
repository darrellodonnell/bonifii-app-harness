
# OUTCOME

Getting 


# Running Containers Locally

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