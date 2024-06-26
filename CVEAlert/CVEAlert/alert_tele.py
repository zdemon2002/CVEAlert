import requests
def reformat_tele_message(title,cvssv20,cvssv30, cvssv31,description,pk):
    message = """CVE's daily alert\nProducts u have follows have a new CVE\nName CVE:'{}'\nSeverity Score (CVSSv2.0):'{}'\nSeverity Score (CVSSv3.0):'{}'\nSeverity Score (CVSSv3.1):'{}'\nDescription:'{}'\nUrl: http://127.0.0.1:8000/detail-cve/{}/""".format(title, cvssv20, cvssv30, cvssv31, description, pk)
    return message


def send_message_telegram(message,TOKEN,chat_id):
    urls = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    return requests.get(urls).json