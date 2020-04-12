import os
import json
import jwt
from google.cloud import pubsub_v1
from google.auth import jwt


def authenticate_client(service_account_info: dict):
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
    return jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience
    )

if __name__ == "__main__":

    service_secret_path = 'service_secret.json'
    service_account_info = {}

    with open(service_secret_path) as service_account_info_file:
        service_account_info = json.load(service_account_info_file)
    service_account_id = service_account_info['client_id']
    project_id = service_account_info['project_id']
    topic = 'u{}'.format(service_account_id)
    subscription_path = 'projects/{}/subscriptions/{}'.format(project_id, topic)
    topic_path = 'projects/{}/topics/{}'.format(project_id, topic)

    publisher = pubsub_v1.PublisherClient(
        credentials=authenticate_client(service_account_info)
    )
    while(True):
        msg = input("Publish something: ")
        
        publisher.publish(topic_path, msg.encode())