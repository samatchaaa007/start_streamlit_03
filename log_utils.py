import requests
from datetime import datetime

def send_log_to_google_form(username, fullname, browser="Unknown", page="Unknown", event="visit_page", ip="Unknown", timestamp=None):
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfp2aRm1XAGkRL0K5y87680BYcko8aGJyhNLsrdaxLbl6Sg/formResponse"

    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "entry.94384076": username,
        "entry.1474490753": fullname,
        "entry.264051270": browser,
        "entry.36918558": page,
        "entry.2013583068": event,
        "entry.543729100": ip,
        "entry.526084478": timestamp
    }

    requests.post(form_url, data=data)
