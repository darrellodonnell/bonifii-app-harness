
# ngrok LIMITS

NOTE: When restarting ngrok, the domains all change (they are ephemeral). This impacts:

* Docker image for Agent (endorser-issuer)
* API endpoint (can hit that locally though with port passthrough)
* webhook


## HL-Indy CLI

Was updated in October 2023

https://github.com/hyperledger/indy-cli-rs

- see Releases


## Indicio DemoNet

Indicio DemonNet 




# ACA-Py Deployment

NOTE: `Endorser` capability will be done using Indy CLI. In future if required an Endorser (Bonifii as Endorser) pattern can be built and deployed using ACA-Py. [for detail see: https://github.com/hyperledger/aries-cloudagent-python/blob/main/Endorser.md]

Key Decisions and notes follow.





# Ledger and Transactions

Ledger Choice: 

* Sovrin:
  * TestNet ($500/6-months and subject to "periodic resets" - what does that even mean?
  * MainNet - $5000/year
* Indicio:
  * DemoNet - https://indicio.tech/indicio-demonet/ - was the initial choice but it has random network resets.
  * **TestNet** as choice - https://indicio.tech/indicio-testnet/ - resets annually 

NOTE: Indicio Transaction Author agreement: https://github.com/Indicio-tech/indicio-network/blob/main/TAA/TAA.md


# ~~CLI Commands~~
- not using CLI - using API

## Sending Credential (automated)

/issue-credential-2.0/send

WORKING??? example:
```

{
  "auto_issue": true,
  "comment": "Some comment",
  "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "credential_preview": {
    "@type": "issue-credential/2.0/credential-preview",
    "attributes": [
      {
        "name": "Institution",
        "value": "Bubbaz CU"
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
        "value": "schmoopy-1234"
      },
      {
        "name": "CertificateID",
        "value": "cert:4567"
      }
    ] 
  },
  "filter": {
    "indy": {
      "cred_def_id": "Enn9uVvmfXTnSGWpk19Tju:3:CL:178678:tag1"
    }
  } 
}

```



EXAMPLE payload
```
{
  "auto_remove": true,
  "comment": "string",
  "connection_id": "ef887afa-90c9-448a-9ac6-5de7955bfca3",
  "credential_preview": {
    "@type": "issue-credential/2.0/credential-preview",
    "attributes": [
      {
        "mime-type": "image/jpeg",
        "name": "favourite_drink",
        "value": "martini"
      }
    ]
  },
  "filter": {
    "indy": {
      "cred_def_id": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
      "issuer_did": "WgWxqztrNooG92RXvxSTWv",
      "schema_id": "WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0",
      "schema_issuer_did": "WgWxqztrNooG92RXvxSTWv",
      "schema_name": "preferences",
      "schema_version": "1.0"
    },
    "ld_proof": {
      "credential": {
        "@context": [
          "https://www.w3.org/2018/credentials/v1",
          "https://w3id.org/citizenship/v1"
        ],
        "credentialSubject": {
          "familyName": "SMITH",
          "gender": "Male",
          "givenName": "JOHN",
          "type": [
            "PermanentResident",
            "Person"
          ]
        },
        "description": "Government of Example Permanent Resident Card.",
        "identifier": "83627465",
        "issuanceDate": "2019-12-03T12:19:52Z",
        "issuer": "did:key:z6MkmjY8GnV5i9YTDtPETC2uUAW6ejw3nk5mXF5yci5ab7th",
        "name": "Permanent Resident Card",
        "type": [
          "VerifiableCredential",
          "PermanentResidentCard"
        ]
      },
      "options": {
        "proofType": "Ed25519Signature2018"
      }
    }
  },
  "replacement_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "trace": true,
  "verification_method": "string"
}
```

# OLD `/issue-credential/send`
```
{
  "auto_remove": true,
  "comment": "Bubbaz CU",
  "connection_id": "ef887afa-90c9-448a-9ac6-5de7955bfca3",
  "cred_def_id": "Enn9uVvmfXTnSGWpk19Tju:3:CL:178678:tag1",
  "credential_proposal": {
    "@type": "issue-credential/1.0/credential-preview",
    "attributes": [
      {
        "name": "Institution",
        "value": "Bubbaz CU"
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
        "value": "schmoopy-1234"
      },
      {
        "name": "CertificateID",
        "value": "cert:4567"
      }
    ]
  },
  "issuer_did": "Enn9uVvmfXTnSGWpk19Tju",
  "schema_id": "Enn9uVvmfXTnSGWpk19Tju:2:MemberPass:1.0",
  "schema_issuer_did": "Enn9uVvmfXTnSGWpk19Tju",
  "schema_name": "MemberPass",
  "schema_version": "1.0",
  "trace": true
}
```

EXAMPLE (from ACA-Py Swagger):
```
{
  "auto_remove": true,
  "comment": "string",
  "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "credential_preview": {
    "@type": "issue-credential/2.0/credential-preview",
    "attributes": [
      {
        "mime-type": "image/jpeg",
        "name": "favourite_drink",
        "value": "martini"
      }
    ]
  },
  "filter": {
    "indy": {
      "cred_def_id": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
      "issuer_did": "WgWxqztrNooG92RXvxSTWv",
      "schema_id": "WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0",
      "schema_issuer_did": "WgWxqztrNooG92RXvxSTWv",
      "schema_name": "preferences",
      "schema_version": "1.0"
    },
    "ld_proof": {
      "credential": {
        "@context": [
          "https://www.w3.org/2018/credentials/v1",
          "https://w3id.org/citizenship/v1"
        ],
        "credentialSubject": {
          "familyName": "SMITH",
          "gender": "Male",
          "givenName": "JOHN",
          "type": [
            "PermanentResident",
            "Person"
          ]
        },
        "description": "Government of Example Permanent Resident Card.",
        "identifier": "83627465",
        "issuanceDate": "2019-12-03T12:19:52Z",
        "issuer": "did:key:z6MkmjY8GnV5i9YTDtPETC2uUAW6ejw3nk5mXF5yci5ab7th",
        "name": "Permanent Resident Card",
        "type": [
          "VerifiableCredential",
          "PermanentResidentCard"
        ]
      },
      "options": {
        "proofType": "Ed25519Signature2018"
      }
    }
  },
  "replacement_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "trace": true,
  "verification_method": "string"
}
Parameter content type


```

## `/out-of-band/send-invitation`


```
{
  "@type": "did:sov:Enn9uVvmfXTnSGWpk19Tju;spec/out-of-band/1.0/invitation",
  "@id": "c927b4a7-1901-433e-ac3f-16158431fd0a",
  "handshake_protocols": [
    "did:sov:Enn9uVvmfXTnSGWpk19Tju;spec/didexchange/1.0"
  ],
  "label": "Alice",
  "service": [
    "did:sov:UpFt248WuA5djSFThNjBhq"
  ]
}
```

source (below): https://ldej.nl/post/becoming-a-hyperledger-aries-developer-part-3-connecting-using-didcomm-exchange/
```
{
  "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/out-of-band/1.0/invitation",
  "@id": "c927b4a7-1901-433e-ac3f-16158431fd0a",
  "handshake_protocols": [
    "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0"
  ],
  "label": "Alice",
  "service": [
    "did:sov:UpFt248WuA5djSFThNjBhq"
  ]
}
```



### /issue-credential/send-offer


test:
```
{
  "auto_issue": true,
  "auto_remove": true,
  "comment": "string",
  "connection_id": "ef887afa-90c9-448a-9ac6-5de7955bfca3",
  "cred_def_id": "Enn9uVvmfXTnSGWpk19Tju:3:CL:178678:tag1",
  "credential_preview": {
    "@type": "issue-credential/1.0/credential-preview",
    "attributes": [
      {
        "Institution": "Bubbaz CU", 
        "CredentialName": "MemberPass",
        "CredentialDescription": "description",
        "MemberSince": "1989",
        "InstitutionID": "schmoopy-1234",
        "CertificateID": "cert:4567"
      }
    ]
  },
  "trace": true
}
```

example:
```
{
  "auto_issue": true,
  "auto_remove": true,
  "comment": "string",
  "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "cred_def_id": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
  "credential_preview": {
    "@type": "issue-credential/1.0/credential-preview",
    "attributes": [
      {
        "mime-type": "image/jpeg",
        "name": "favourite_drink",
        "value": "martini"
      }
    ]
  },
  "trace": true
}
```


/question/{conn_id}/send-question


```
{
 "@type": "https://didcomm.org/questionanswer/1.0/question",
 "question_text": "MemberPass CU has a question.",
 "question_detail": "Do you love MemberPass?",
 "valid_responses": [
 {"text": "YES"},
 {"text": "no"}
 ]
}
```