#! python3
# autoUnsubscriber.py - check through emails and open unsuscribe links.

import imapclient, imaplib, bs4, pyzmail, sys, webbrowser
imaplib._MAXLINE = 10000000

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('kevin.e.varney@googlemail.com',sys.argv[1])
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE', '12-Oct-2017'])
rawMessages = imapObj.fetch(UIDs,['BODY[]'])

for UID in UIDs:
    message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
    if message.html_part != None:
        try:
            payload = message.html_part.get_payload().decode(message.html_part.charset)
            soup = bs4.BeautifulSoup(payload,'lxml')
            elems = soup.select('p')
            for elem in elems:
                text = elem.getText()
                if text.find('unsubscribe') > 0:
                    link = elem.find('a')
                    webbrowser.open(link.get('href'))
        except:
            print('Exception occurred')

imapObj.logout()
