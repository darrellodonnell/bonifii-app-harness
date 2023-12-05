Tom has created two tools for us to use –

* Database with all of the client information, this replaces the spreadsheet that we were using – here is the link to the Database - https://securememberpass.azurewebsites.net/EditInfo
  * There is column that contains the Client secret expiration date which can be sorted on
  * When a new Client secret is created because the old one is expiring, the new secret should be placed in the Client secret field and the old secret should be moved to the Notes column
  * The credit union should then be notified and requested to update their secret to the new one
* Tool to test current credit union status – here is the link - https://securememberpass.azurewebsites.net/Test2
  * From this tool, you can pick the Credit union, dev or prod and test if their environment is working
  * This tool pulls data from the Database listed above
* Adding security - adminMP/Adm1nMP (needed to get into the sites)