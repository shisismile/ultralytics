import time
import hmac
import hashlib
import base64
import urllib.parse
import requests


def __send_dingtalk_msg(secret, access_token, msg, at_mobiles):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    webhook = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}&timestamp={timestamp}&sign={sign}"
    data = {
        "msgtype": "text",
        "text": {"content": msg},
        "at": {
            "atMobiles": at_mobiles,
            "isAtAll": False
        }
    }
    requests.post(webhook, json=data)


def send_dingtalk_msg(msg):
    __send_dingtalk_msg("SECd8aa4520f6bd57092623920749539ffb2d73f1bab06a0459c7bc408148edec84",
                        "76f60559907f0cb704689497e4096f5b1ad3deadcdc0bdc81bacf9c5f253b3bb" ,
                        msg,
                        ['17620533287'])



if __name__ == "__main__":
    send_dingtalk_msg("训练完成")