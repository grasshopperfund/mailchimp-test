import os

from dotenv import load_dotenv
import mailchimp_transactional as MailchimpTransactional
from mailchimp3 import MailChimp
import mailchimp_marketing as MailchimpMarketing

load_dotenv()

MAILCHIMP_TRANSACTIONAL_API_KEY = os.getenv("MAILCHIMP_TRANSACTIONAL_API_KEY")
mailchimp_transactional_api = MailchimpTransactional.Client(MAILCHIMP_TRANSACTIONAL_API_KEY)

MAILCHIMP_MARKETING_API_KEY = os.getenv("MAILCHIMP_MARKETING_API_KEY")
MAILCHIMP_USERNAME = os.getenv("MAILCHIMP_USERNAME")
mailchimp_marketing_vingt_cinq_api = MailChimp(mc_api=MAILCHIMP_MARKETING_API_KEY, mc_user=MAILCHIMP_USERNAME)

MAILCHIMP_SERVER_PREFIX = os.getenv("MAILCHIMP_SERVER_PREFIX")
mailchimp_marketing_api = MailchimpMarketing.Client()
mailchimp_marketing_api.set_config({
    "api_key": MAILCHIMP_MARKETING_API_KEY,
    "server": MAILCHIMP_SERVER_PREFIX
})

MAILCHIMP_LIST_ID = os.getenv("MAILCHIMP_LIST_ID")