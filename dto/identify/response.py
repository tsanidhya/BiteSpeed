
class Contact:
    primaryContatctId: int
    emails: list
    phoneNumbers: list
    secondaryContactIds: list

    def ret_json(self):
        return {
            'primaryContatctId': self.primaryContatctId,
            'emails': self.emails,
           'phoneNumbers' : self.phoneNumbers,
            'secondaryContactIds': self.secondaryContactIds
        }


class IdentifyResponse:
    contact: Contact

    def __init__(self, primaryContatctId =-1, emails=[],phoneNumbers=[],secondaryContactIds=[]):
        contactObj = Contact()
        contactObj.primaryContatctId = primaryContatctId
        contactObj.emails = emails
        contactObj.phoneNumbers = phoneNumbers
        contactObj.secondaryContactIds = secondaryContactIds
        self.contact = contactObj

    def ret_json(self):
        return {
            'contact' : self.contact.ret_json()
        }



