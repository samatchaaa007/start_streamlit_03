def send_log_to_google_form(username, fullname, browser, page, event, ip):
    import requests
    from datetime import datetime

    url = "https://docs.google.com/forms/d/e/1FAIpQLSfp2aRm1XAGkRL0K5y87680BYcko8aGxJyhpNLsrdaxLbI65g/formResponse"
    
    form_data = {
        "entry.36918558": username,
        "entry.94384076": fullname,
        "entry.1474490753": browser,
        "entry.264051270": page,
        "entry.2013583068": event,
        "entry.543729100": ip,
        "entry.526048478": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    response = requests.post(url, data=form_data)
    return response.status_code == 200
