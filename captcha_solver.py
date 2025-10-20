# https://github.com/2captcha/2captcha-python

import sys
import os
from twocaptcha import TwoCaptcha
import base64

password = "89f9dd097ee56e5784be091863ac0589"

def solveRecaptcha(sitekey, url):

    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    api_key = os.getenv('APIKEY_2CAPTCHA', password)
    solver = TwoCaptcha(api_key)

    try:
        result = solver.rotate()

    except Exception as e:
        sys.exit(e)

    else:
        sys.exit('solved: ' + str(result))
