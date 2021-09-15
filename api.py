import os

from dotenv import load_dotenv
import mailchimp_transactional as MailchimpTransactional


load_dotenv()

MAILCHIMP_TRANSACTIONAL_API_KEY = os.getenv("MAILCHIMP_TRANSACTIONAL_API_KEY")
mailchimp_transactional_api = MailchimpTransactional.Client(MAILCHIMP_TRANSACTIONAL_API_KEY)