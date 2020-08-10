#! python3
# ChoreAssignment.py - Assigns chores that need to be done randomly to people,
#                   and sents them the email with task.

import random, smtplib
import shelve, pprint

chores = ['dishes', 'bathroom', 'bedroom', 'vaccum', 'cleaning', 'walk dog']
names = {'Joe':'example@example.pl', 'Betty':'example@example.pl',
         'Franc':'example@example.pl', 'Beatriz':'example@example.pl'}

shelfFile = shelve.open('duties', writeback=True)
duties = []
for people in names:
    while True:
        randomChore = random.choice(chores)
        if (randomChore not in ' '.join(shelfFile['duty'][people])):
            break
    chores.remove(randomChore)
    duties.append([people,[names[people],randomChore]])
pprint.pprint(duties)

smtpObj = smtplib.SMTP_SSL('smtp.poczta.example.pl', 465)
smtpObj.ehlo()
smtpObj.login('example@example.pl', 'somepassword')

for name, data in duties:
    shelfFile['duty'].setdefault(name, []).append(data[1])
    body = '''Subject: Duties for this week.\n
Dear %s,\n In this week you are responsable for %s.
Best Regards.''' % (name, data[1])
    print('Sending message to %s...' % (name))
    sendmailStatus = smtpObj.sendmail('example@example.pl',data[0], body)

    if sendmailStatus != {}:
        print('There was a problem with sending email to %s: %s' %
              (name, sendmailStatus))
smtpObj.quit()
print(shelfFile['duty'])
shelfFile.close()
