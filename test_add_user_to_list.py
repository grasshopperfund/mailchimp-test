import json

from api import (
    mailchimp_marketing_api,
    MAILCHIMP_LIST_ID,
)



def get_all_lists():
    return mailchimp_marketing_api.lists.get_all_lists()

def get_list():
    return mailchimp_marketing_api.lists.get_list(MAILCHIMP_LIST_ID)

if __name__ == '__main__':
    response =  get_list()


    print(json.dumps(response, indent=4, sort_keys=True))