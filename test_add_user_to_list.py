import json

from api import (
    mailchimp_marketing_api
)



def get_all_lists():
    return mailchimp_marketing_api.lists.get_all_lists()


if __name__ == '__main__':
    response =  get_all_lists()


    print(json.dumps(response, indent=4, sort_keys=True))