import imaplib
import cred
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(cred.username, cred.password)
mail.list()
# Out: list of "folders" aka labels in gmail.
print(mail.select("inbox")) # connect to inbox.