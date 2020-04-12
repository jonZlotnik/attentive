import os
import json
import jwt
from google.cloud import pubsub_v1
from google.auth import jwt


def authenticate_client(service_account_info: dict):
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"
    return jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience
    )

def callback(message):
    print("Received message: {}".format(message))
    message.ack()



if __name__ == "__main__":

    service_secret_path = 'service_secret.json'
    service_account_info = {}

    with open(service_secret_path) as service_account_info_file:
        service_account_info = json.load(service_account_info_file)
    service_account_id = service_account_info['client_id']
    project_id = service_account_info['project_id']

    service_creds = authenticate_client(service_account_info)
    subscriber = pubsub_v1.SubscriberClient(credentials=service_creds)

    subscription_path = 'projects/{}/subscriptions/u{}'.format(project_id, service_account_id)

    streaming_pull_future = subscriber.subscribe(
        subscription_path, callback=callback
    )
    print("Listening for messages on {}..\n".format(subscription_path))

    with subscriber:
        streaming_pull_future.result(timeout=100000)
        # try:
        #     # When `timeout` is not set, result() will block indefinitely,
        #     # unless an exception is encountered first.
        #     streaming_pull_future.result(timeout=100000)
        # except:  # noqa
        #     streaming_pull_future.cancel()


# Embedded Auth
# -------------------------------------------
# service_account_info = json.load(open("service-account-info.json"))
# audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

# credentials = jwt.Credentials.from_service_account_info(
#     service_account_info, audience=audience
# )

# subscriber = pubsub_v1.SubscriberClient(credentials=credentials) 
# -------------------------------------------


# Common Business
# -------------------------------------------
