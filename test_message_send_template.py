import os

from mailchimp_transactional.api_client import ApiClientError

from api import mailchimp_transactional_api

recipient_username = "swagtastic"
template_content = [
    {"username": recipient_username},
]

subject = "Grasshopperfund Development Test Email"
grasshopperfund_dev_email = os.getenv("GRASSHOPPERFUND_DEV_EMAIL")
recipient_email = os.getenv("RECIPIENT_EMAIL")
message = {
    "subject": subject,
    "from_email": grasshopperfund_dev_email,
    "to": [
            {
            "email": recipient_email,
        },
    ],
}

template_name = "test1"
send_template_data = {
    "template_name": template_name,
    "template_content": template_content,
    "message": message,
}


def send_template_test():
    try:
        mailchimp_transactional_api.messages.send_template(
            send_template_data
        )
    except ApiClientError as error:
        print(error.text)


if __name__ == '__main__':
    send_template_test()