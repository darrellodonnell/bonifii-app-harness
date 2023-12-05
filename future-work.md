

Pyramid

The overall ACA-Py solution has been proven out at a very high-level. There are three types of remaining work:

- Underway - efforts that we must complete before end-December.
- Critical - efforts that we SHOULD complete before end-December.
- Deferrable - efforts that can wait until the project is picked up again.


## Activities Underway 
- complete Finivation back-end efforts to replace Verity2 with ACA-Py
- developer testbed scripts 
- Deploying Mediator 
- 

## CONFIGURATIONS - Test Harness

- DID
- Cred Def
- Host Address
- 


## CRITICAL/Recommended Activities

- DONE: Separate Endorser/Issuer and Mediator 
- multi-tenant mode


## Deferrable Activities

- Backup & Recovery
- Production-Readiness tests of `/qa` protocol
- 


---

## Deferrable Activities

# Full Endorser-Issuer-Mediator Chain

## Dev Sandbox/Testbed - Local

Currently a single docker container agent is acting in all three critical roles (Endorser, Issuer, Mediator) 

Missing - device testing locally...


## Dev Sandbox/Testbed - Azure




## ACA-Py configs

--invite-label 
--webhook-url
--trace-label Label (agent name) used logging events. [env var: ACAPY_TRACE_LABEL]

# QA Protocol

The QA protocol that is used, based on the Indicio plugin (TODO: add reference) is not production grade, at least not necessarily. The following should be done:
* Documentation of Plug-In including Swagger/OAS.
* Code inspection, including test coverage, and AIP test creation.
* Remove dangling API Calls (E.g. are the `HEAD /qa/get-questions` and `GET /qa/questions` required?)


# Backup & Recovery

The overall wallet infrastructure is well known and the ACA-Py community 
