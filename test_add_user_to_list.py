import json

from mailchimp_marketing.api_client import ApiClientError

from api import (
    mailchimp_marketing_api,
    MAILCHIMP_LIST_ID,
    RECIPIENT_EMAIL,
)



def get_all_lists():
    return mailchimp_marketing_api.lists.get_all_lists()

def get_list():
    return mailchimp_marketing_api.lists.get_list(MAILCHIMP_LIST_ID)

def add_user_to_list():
    subscriber_data = {
        "email_address": RECIPIENT_EMAIL,
        "status": "subscribed"
    }
    return mailchimp_marketing_api.lists.add_list_member(MAILCHIMP_LIST_ID, subscriber_data)

if __name__ == '__main__':

    try:
        response =  add_user_to_list()
        print(json.dumps(response, indent=4, sort_keys=True))
    except ApiClientError as error:
        print(error.text)