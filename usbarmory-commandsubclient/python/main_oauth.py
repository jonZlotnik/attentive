import os
import json
import jwt
from google.cloud import pubsub_v1
from google_auth_oauthlib import flow, helpers


def authenticate_user(client_secret_path: str, scopes: [str]):
    appflow = flow.InstalledAppFlow.from_client_secrets_file(
        client_secret_path,
        scopes=scopes
    )
    appflow.run_console()
    return appflow.credentials

def callback(message):
    print("Received message: {}".format(message))
    message.ack()



if __name__ == "__main__":

    client_secret_path = 'client_secret.json'
    client_creds = {}
    with open(client_secret_path) as client_creds_file:
        client_creds = json.load(client_creds_file)
    
    
    user_creds = authenticate_user(client_secret_path, ["openid", "https://www.googleapis.com/auth/userinfo.email"])
    subscriber = pubsub_v1.SubscriberClient(credentials=user_creds)

    uid:str = 'u' + jwt.decode(user_creds.id_token, verify=False)['sub']
    project_id = client_creds['installed']['project_id']

    subscription_path = 'projects/{}/subscriptions/{}'.format(project_id, uid)

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
