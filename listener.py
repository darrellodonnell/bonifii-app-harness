import time
import webhook_listener
from datetime import datetime

def process_post_request(request, *args, **kwargs):
    print(
        "\nReceived request:\n"
        # + "Method: {}\n".format(request.method)
        # + "Headers: {}\n".format(request.headers)
        + "Args (url path): {}\n".format(args)
        # + "Keyword Args (url parameters): {}\n".format(kwargs)
        + "Body: {}".format(
            request.body.read(int(request.headers["Content-Length"]))
            if int(request.headers.get("Content-Length", 0)) > 0
            else ""
        )
    )

    # Process the request!
    # ...

    return


webhooks = webhook_listener.Listener(handlers={"POST": process_post_request}, port = 5000)
webhooks.start()

while True:
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date_time + ": Still alive...")
    time.sleep(3000)