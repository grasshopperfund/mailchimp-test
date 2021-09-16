import json

from api import (
    mailchimp_marketing_vingt_cinq_api
)




def test_add_user_to_list():
    return mailchimp_marketing_vingt_cinq_api.lists.all(get_all=True)


if __name__ == '__main__':
    json_response =  test_add_user_to_list()

    print(json.dumps(json_response, indent=4, sort_keys=True))
