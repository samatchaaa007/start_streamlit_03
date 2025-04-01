def send_log_to_google_form(username, fullname, browser, page, event, ip):
    import requests
    from datetime import datetime

    url = "https://docs.google.com/forms/d/e/xxxxxxxxxx/formResponse"
    form_data = {
        "entry.1234567890": username,
        "entry.2345678901": fullname,
        "entry.3456789012": browser,
        "entry.4567890123": page,
        "entry.5678901234": event,
        "entry.6789012345": ip,
        "entry.7890123456": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    response = requests.post(url, data=form_data)
    return response.status_code == 200
