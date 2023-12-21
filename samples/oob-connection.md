
# Summary of OOB Invitation

## Two Different State Flows

There are state flows for both `connection` and `out_of_band` (using webhook labels not API labels) that come in via the webhook `topic` channel.

### connections

state flow:

`invitation` -> `request` -> `response` -> `active`

> **NOTE:** if user does not hit Connect (e.g. ignores or presses Deny) NO RESPONSE will be received, leaving us in `invitation` state
 

### out_of_band

state flow:

`await-response` -> `done`
> **NOTE:** if user does not hit Connect (e.g. ignores or presses Deny) NO RESPONSE will be received - leaving us in `await-response` state

# QR Code Generated in www

FROM SERVER (to generate QR)
> **NOTE:** There is a ***mismatch*** in fields. `invi_msg_id` is returned from the /out-of-band/create-invitation POST, but it is returned in webhooks under the `connections` topic as `invitation_msg_id`.
>
> FROM API:
> * `'invi_msg_id': 'c509a7a9-7911-4d55-90b9-8f3903d06d83'`
> 
> FROM WEBHOOKS:
> * `/topic/out_of_band` - `"invi_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83"`
> * `/topic/connections` - `"invitation_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83"`

POST:

```
{"handshake_protocols": ["did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0"], "metadata": {}, "my_label": "Bonifii Demo CU"}
```
RETURNS:
```
{'state': 'initial', 'trace': False, 'invi_msg_id': 'c509a7a9-7911-4d55-90b9-8f3903d06d83', 'oob_id': '67c814a2-cc2b-409b-bf4a-68c3ebde7212', 'invitation': {'@type': 'did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/out-of-band/1.1/invitation', '@id': 'c509a7a9-7911-4d55-90b9-8f3903d06d83', 'label': 'Bonifii Demo CU', 'imageUrl': 'https://culedger.s3.amazonaws.com/MemberPass512x512.png', 'handshake_protocols': ['did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0'], 'services': [{'id': '#inline', 'type': 'did-communication', 'recipientKeys': ['did:key:z6MkfhJgdVLVJjVfyPuasrJqRyrX1mVKyVsSszw1kkeLEdvA'], 'serviceEndpoint': 'https://4a0a09025a0e.ngrok.app'}]}, 'invitation_url': 'https://4a0a09025a0e.ngrok.app?oob=eyJAdHlwZSI6ICJkaWQ6c292OkJ6Q2JzTlloTXJqSGlxWkRUVUFTSGc7c3BlYy9vdXQtb2YtYmFuZC8xLjEvaW52aXRhdGlvbiIsICJAaWQiOiAiYzUwOWE3YTktNzkxMS00ZDU1LTkwYjktOGYzOTAzZDA2ZDgzIiwgImxhYmVsIjogIkJvbmlmaWkgRGVtbyBDVSIsICJpbWFnZVVybCI6ICJodHRwczovL2N1bGVkZ2VyLnMzLmFtYXpvbmF3cy5jb20vTWVtYmVyUGFzczUxMng1MTIucG5nIiwgImhhbmRzaGFrZV9wcm90b2NvbHMiOiBbImRpZDpzb3Y6QnpDYnNOWWhNcmpIaXFaRFRVQVNIZztzcGVjL2Nvbm5lY3Rpb25zLzEuMCJdLCAic2VydmljZXMiOiBbeyJpZCI6ICIjaW5saW5lIiwgInR5cGUiOiAiZGlkLWNvbW11bmljYXRpb24iLCAicmVjaXBpZW50S2V5cyI6IFsiZGlkOmtleTp6Nk1rZmhKZ2RWTFZKalZmeVB1YXNySnFSeXJYMW1WS3lWc1Nzencxa2tlTEVkdkEiXSwgInNlcnZpY2VFbmRwb2ludCI6ICJodHRwczovLzRhMGEwOTAyNWEwZS5uZ3Jvay5hcHAifV19'}
```

# webhook activity follows:

> NOTE: the following text (repeated on every event) is from the `listener.py` webhook harness:
```
Received request:
Args (url path): ('webhook', 'topic', 'out_of_band')
Body: b'
```

ON SERVER (webhook) - written in order received.

* 18:20:29.448660Z `/topic/out_of_band` - `state` of `await-response`
* 18:20:29.416692Z `/topic/connections` - `state` of `invitation`

```
Received request:
Args (url path): ('webhook', 'topic', 'out_of_band')
Body: b'{"state": "await-response", "created_at": "2023-12-18T18:20:29.448660Z", "updated_at": "2023-12-18T18:20:29.448660Z", "trace": false, "oob_id": "67c814a2-cc2b-409b-bf4a-68c3ebde7212", "invi_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "invitation": {"@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/out-of-band/1.1/invitation", "@id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "label": "Bonifii Demo CU", "imageUrl": "https://culedger.s3.amazonaws.com/MemberPass512x512.png", "handshake_protocols": ["did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0"], "services": [{"id": "#inline", "type": "did-communication", "recipientKeys": ["did:key:z6MkfhJgdVLVJjVfyPuasrJqRyrX1mVKyVsSszw1kkeLEdvA"], "serviceEndpoint": "https://4a0a09025a0e.ngrok.app"}]}, "connection_id": "a19d3461-dba2-47db-b9bc-de9a002b5fc4", "our_recipient_key": "2F3e3F63yC1Cru4tCHLzatJXCCDUZcd6Bz25vUgKKR8n", "role": "sender"}'
```
This `out_of_band` response contains:
* `connection_id` - but we don't have enough context to do anything with that yet as we need the `connections` topic data


```
Received request:
Args (url path): ('webhook', 'topic', 'connections')
Body: b'{"state": "invitation", "created_at": "2023-12-18T18:20:29.416692Z", "updated_at": "2023-12-18T18:20:29.416692Z", "connection_id": "a19d3461-dba2-47db-b9bc-de9a002b5fc4", "their_role": "invitee", "connection_protocol": "connections/1.0", "rfc23_state": "invitation-sent", "invitation_key": "2F3e3F63yC1Cru4tCHLzatJXCCDUZcd6Bz25vUgKKR8n", "invitation_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "routing_state": "none", "accept": "auto", "invitation_mode": "once"}'
```

This `connections` event contains:
* connection_id - this links to the `out_of_band` message previous
* invitation_msg_id - this can be correlated to the `invi_msg_id` received from the API

The `updated_at` timestamp is OLDER than the timestamp for the `out_of_band` data received.



> [!NOTE]
> At this point we MUST await input from the Member.
> On the Member's device a prompt to "Connect/Deny" is presented.
> There is NO activity on the server until `Connect` is pressed. Reiterating a point above when a Member ignores or hits Deny, no messages are received.



We get 4 events (written in order received)
* 18:21:40.685860Z `/topic/connections` - `state` of `request`
* 18:20:29.448660Z `/topic/out_of_band` - `state` of `done` 
  - oob invitation is "done" BUT `updated_at` **IS NOT UPDATED**
* 18:21:40.708380Z `/topic/connections` - `state` of `response`
* 18:21:43.825507Z `/topic/connections` - `state` of `active` 
  - connection is active

```
Received request:
Args (url path): ('webhook', 'topic', 'connections')
Body: b'{"state": "request", "created_at": "2023-12-18T18:20:29.416692Z", "updated_at": "2023-12-18T18:21:40.685860Z", "connection_id": "a19d3461-dba2-47db-b9bc-de9a002b5fc4", "their_did": "ABALLmQDZA8JJS9nFZXmnE", "their_label": "iPhone", "their_role": "invitee", "connection_protocol": "connections/1.0", "rfc23_state": "request-received", "invitation_key": "2F3e3F63yC1Cru4tCHLzatJXCCDUZcd6Bz25vUgKKR8n", "invitation_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "routing_state": "none", "accept": "auto", "invitation_mode": "once"}'

Received request:
Args (url path): ('webhook', 'topic', 'out_of_band')
Body: b'{"state": "done", "created_at": "2023-12-18T18:20:29.448660Z", "updated_at": "2023-12-18T18:20:29.448660Z", "trace": false, "oob_id": "67c814a2-cc2b-409b-bf4a-68c3ebde7212", "invi_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "invitation": {"@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/out-of-band/1.1/invitation", "@id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "label": "Bonifii Demo CU", "imageUrl": "https://culedger.s3.amazonaws.com/MemberPass512x512.png", "handshake_protocols": ["did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0"], "services": [{"id": "#inline", "type": "did-communication", "recipientKeys": ["did:key:z6MkfhJgdVLVJjVfyPuasrJqRyrX1mVKyVsSszw1kkeLEdvA"], "serviceEndpoint": "https://4a0a09025a0e.ngrok.app"}]}, "connection_id": "a19d3461-dba2-47db-b9bc-de9a002b5fc4", "our_recipient_key": "2F3e3F63yC1Cru4tCHLzatJXCCDUZcd6Bz25vUgKKR8n", "role": "sender"}'

Received request:
Args (url path): ('webhook', 'topic', 'connections')
Body: b'{"state": "response", "created_at": "2023-12-18T18:20:29.416692Z", "updated_at": "2023-12-18T18:21:40.708380Z", "connection_id": "a19d3461-dba2-47db-b9bc-de9a002b5fc4", "my_did": "Jky5dQ86cS72TgaY695uy4", "their_did": "ABALLmQDZA8JJS9nFZXmnE", "their_label": "iPhone", "their_role": "invitee", "connection_protocol": "connections/1.0", "rfc23_state": "response-sent", "invitation_key": "2F3e3F63yC1Cru4tCHLzatJXCCDUZcd6Bz25vUgKKR8n", "invitation_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "routing_state": "none", "accept": "auto", "invitation_mode": "once"}'

Received request:
Args (url path): ('webhook', 'topic', 'connections')
Body: b'{"state": "active", "created_at": "2023-12-18T18:20:29.416692Z", "updated_at": "2023-12-18T18:21:43.825507Z", "connection_id": "a19d3461-dba2-47db-b9bc-de9a002b5fc4", "my_did": "Jky5dQ86cS72TgaY695uy4", "their_did": "ABALLmQDZA8JJS9nFZXmnE", "their_label": "iPhone", "their_role": "invitee", "connection_protocol": "connections/1.0", "rfc23_state": "completed", "invitation_key": "2F3e3F63yC1Cru4tCHLzatJXCCDUZcd6Bz25vUgKKR8n", "invitation_msg_id": "c509a7a9-7911-4d55-90b9-8f3903d06d83", "routing_state": "none", "accept": "auto", "invitation_mode": "once"}'
```