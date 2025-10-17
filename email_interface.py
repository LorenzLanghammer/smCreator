from abc import ABC, abstractmethod
import json
import requests
import random
import string
import zendriver as zd
import asyncio
from country_values import *
from smsactivate.api import SMSActivateAPI
from helper import *
import imaplib
import re
from email import policy
from email.parser import BytesParser
from email.header import decode_header, make_header
from imapclient import IMAPClient
from datetime import timezone, datetime
from email import policy
import base64
import time
import email
from database.dbInterface import *

class EmailInterface(ABC):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @abstractmethod
    async def getCode(self):
        pass


class GmailImapInterface(EmailInterface):
    async def getCode(self):
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        try:
            mail.login(self.email, self.password)
            mail.select("INBOX")
            status, message_numbers = mail.search(None, 'FROM', '"instagram"')

            if status != 'OK' or not message_numbers[0]:
                return None
            
            msg_nums = message_numbers[0].split()
            for num in reversed(msg_nums):
                status, msg_data = mail.fetch(num, '(RFC822)')
                if status != 'OK':
                    continue

                msg = BytesParser(policy=policy.default).parsebytes(msg_data[0][1])
                raw_subject = msg['subject']
                if not raw_subject:
                    continue

                subject = str(make_header(decode_header(raw_subject)))
                m = re.search(r'\b(\d{4,8})\b', subject)  # e.g., 6 digits, allow 4–8 just in case
                if m:
                    code = m.group(1)
                    print(f"Instagram code: {code}")
                    return code
            return None
        finally:
            try:
                mail.logout()
            except Exception as e:
                print(f"Error logging out: {e}")


class OutlookImapInterface(EmailInterface):
    def __init__(self, email, password, client_id):
        super().__init__(email, password)
        self.client_id = client_id

    async def getCode(self):
        access_token = self.get_access_token(self.password, "00000000402b2c1f")
        auth_string = f"user={self.email}\x01auth=Bearer {access_token}\x01\x01"
        auth_b64 = base64.b64encode(auth_string.encode()).decode()
        
        mail = imaplib.IMAP4_SSL("imap-mail.outlook.com") 
        typ, data = mail.authenticate("XOAUTH2", lambda x: auth_b64)
        if typ != 'OK':
            raise Exception(f"XOAUTH2 auth failed: {typ} {data}")
        
        mail.select("INBOX")
        status, message_numbers = mail.search(None, 'FROM', '"instagram"')
        if status != 'OK' or not message_numbers[0]:
            return None
        msg_nums = message_numbers[0].split()


        for num in reversed(msg_nums):
            status, msg_data = mail.fetch(num, '(RFC822)')
            if status != 'OK':
                continue
            msg = BytesParser(policy=policy.default).parsebytes(msg_data[0][1])
            raw_subject = msg['subject']
            if not raw_subject:
                continue

            subject = str(make_header(decode_header(raw_subject)))
            m = re.search(r'\b(\d{4,8})\b', subject)  # e.g., 6 digits, allow 4–8 just in case
            if m:
                code = m.group(1)
                print(f"Instagram code: {code}")
                return code
            return None
        return mail 

    
    def get_access_token(self, refresh_token, client_id, client_secret=None):
        token_url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
        data = {
            "client_id": client_id,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": "https://outlook.office.com/IMAP.AccessAsUser.All offline_access openid profile email"
        }

        if client_secret:
            data["client_secret"] = client_secret

        resp = requests.post(token_url, data=data)
    
        try:
            resp.raise_for_status()
        except requests.HTTPError:
            # show the error details for debugging
            print("Token endpoint error:", resp.status_code, resp.text)
            raise
        return resp.json()["access_token"]



class GmxInstaImapInterface(EmailInterface):
    async def getCode(self):
        EMAIL = self.email
        PASSWORD = self.password

        try:
            mail = imaplib.IMAP4_SSL("imap.gmx.com")
            mail.login(EMAIL, PASSWORD)
            mail.select("INBOX")
            status, message_numbers = mail.search(None, 'FROM', '"instagram"')
            msg_nums = message_numbers[0].split()

            for num in reversed(msg_nums):
                
                status, msg_data = mail.fetch(num, '(RFC822)')
                if status != 'OK':
                    print(f"Error fetching message {num}: {status}")
                    continue
                msg = BytesParser(policy=policy.default).parsebytes(msg_data[0][1])
                raw_subject = msg['subject']
                if not raw_subject:
                    print(f"No subject found in message {num}")
                    continue
                subject = str(make_header(decode_header(raw_subject)))
                m = re.search(r'\b(\d{4,8})\b', subject)
                if m:
                    code = m.group(1)
                    print(f"Instagram code: {code}")
                    return code
                print(f"No code found in subject: {subject}")
            return None
        except Exception as e:
            print(f"IMAP error: {e}")
        finally:
            try:
                mail.logout()
            except:
                pass


class GmxTiktokImapInterface(EmailInterface):
    async def getCode(self, email, password):
        #EMAIL = self.email
        #PASSWORD = self.password

        try:
            mail = imaplib.IMAP4_SSL("imap.gmx.com")
            mail.login(email, password)
            mail.select("INBOX")
            status, message_numbers = mail.search(None, 'FROM', '"noreply@account.tiktok.com"')
            msg_nums = message_numbers[0].split()

            for num in reversed(msg_nums):
                
                status, msg_data = mail.fetch(num, '(RFC822)')
                if status != 'OK':
                    print(f"Error fetching message {num}: {status}")
                    continue
                msg = BytesParser(policy=policy.default).parsebytes(msg_data[0][1])
                raw_subject = msg['subject']
                if not raw_subject:
                    print(f"No subject found in message {num}")
                    continue
                subject = str(make_header(decode_header(raw_subject)))
                m = re.search(r'\b\d{6}\b', subject)
                if m:
                    code = m.group(0)
                    print(f"Tiktok code: {code}")
                    return code
                print(f"No code found in subject: {subject}")
            return None
        except Exception as e:
            print(f"IMAP error: {e}")
        finally:
            try:
                mail.logout()
            except:
                pass

    async def getCodeById(self, id):
        row = get_gmx_by_id(id)
        email = row[1]
        password = row[2]
        code = await self.getCode(email, password)
        return code


gmxtiktok = GmxTiktokImapInterface("robertktd-brickles@gmx.com", "m7q1S84dg2x")
asyncio.run(gmxtiktok.getCodeById(578))

def get_content():

    IMAP_SERVER = "imap.gmx.com"
    EMAIL_ACCOUNT = "dunnkevin1572@gmx.com"
    PASSWORD = "cqayrm0MX"

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")
    if status != "OK":
        print("No messages found!")
        exit()

    email_ids = messages[0].split()

    for eid in email_ids:
        status, msg_data = mail.fetch(eid, "(RFC822)")
        if status != "OK":
            print("Failed to fetch", eid)
            continue

        raw_msg = msg_data[0][1]
        msg = email.message_from_bytes(raw_msg)

        print("=" * 80)
        print("From:", msg.get("From"))
        print("To:", msg.get("To"))
        print("Date:", msg.get("Date"))
        print("Subject:", msg.get("Subject"))

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_dispo = str(part.get("Content-Disposition"))
                if content_type == "text/plain" and "attachment" not in content_dispo:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    print("Body:\n", body)
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")
            print("Body:\n", body)

    mail.logout()


def filter_working_imap():
    rows = get_all_gmx()
    for row in rows:

        mail = imaplib.IMAP4_SSL("imap.gmx.com")
        try:
            mail.login(row[1], row[2])
            print("could log in")
        except Exception as e:
            print("login failed for" + str(row[0]))
        #mail.select("INBOX")
        

#filter_working_imap()
#get_content()