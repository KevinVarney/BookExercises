#! python3
# randomChoreEmailer.py

import smtplib, sys, random

emailAddresses = ['k.varney@pgr.reading.ac.uk', 'kevin_varney@yahoo.com', \
          'kevinvarney@bulldoghome.com', 'k.varney@student.reading.ac.uk']
myEmailAddress = 'kevin.e.varney@googlemail.com'          
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(myEmailAddress,sys.argv[1])

for address in emailAddresses:
    randomChore = random.choice(chores)
    chores.remove(randomChore)
    print('Sending chore ' + randomChore + ' to ' + address)
    body = "Subject: Chore. \n Your chore for today is " + randomChore
    sendMailStatus = smtpObj.sendmail(myEmailAddress, address, body)

    if sendMailStatus != {}:
        print('There was a problem sending email to %s, %s' % (address, body))

smtpObj.quit()
