#! python3
# rxEmail2Bittorrent.py

import imapclient, imaplib, pyzmail, pprint, sys

imaplib._MAXLINE = 10000000
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('kevin.e.varney@gmail.com',sys.argv[1])
imapObj.select_folder('INBOX',readonly=True)
UIDs = imapObj.search(['ON', '13-Oct-2017'])
rawMessages = imapObj.fetch(UIDs, [b'BODY[]'])

#for UID in UIDs:
message = pyzmail.PyzMessage.factory(rawMessages[44224][b'BODY[]'])
for mailpart in message.mailparts:
    payload = mailpart.get_payload()
    pprint.pprint(payload)
    #if message.html_part != None:
    #    try:
    #        payload = message.html_part.get_payload().decode(message.html_part.charset)
    #        if payload.find('password') > 0:
    #            attachments = message.preamble

    #            print('')
    #    except:
    #        print('Exception')

imapObj.logout()


