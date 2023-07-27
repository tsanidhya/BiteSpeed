from db_repository.ContactRepository import ContactRepository
from dto.identify.response import IdentifyResponse
from dto.identify.request import IdentifyRequest
class ContactService:
    contactRepository: ContactRepository

    def __init__(self, contactRepository):
        self.contactRepository = contactRepository


    def execute(self, request:IdentifyRequest):
        # print(email)
        # print(phoneNumber)
        # print("Done----------->")
        responses = []
        if request.email and not request.phoneNumber:
            linkedid = self.contactRepository.insert_when_phone_number_null(request.email)
            if not linkedid:
                responses = self.contactRepository.get_contacts_with_email(request.email)
            else:
                responses = self.contactRepository.get_contacts_with_linked_id(linkedid)
        if request.phoneNumber and not request.email:
            linkedid = self.contactRepository.insert_when_email_null(request.phoneNumber)
            if not linkedid:
                responses = self.contactRepository.get_contacts_with_phone(request.phoneNumber)
            else:
                responses = self.contactRepository.get_contacts_with_linked_id(linkedid)
        if request.phoneNumber and request.email:
            print("HERE phoneNumber and email")
            linkedid = self.contactRepository.insert_when_email_phone_present(request.email,request.phoneNumber)
            if not linkedid:
                responses,dummy = self.contactRepository.get_contacts_with_phone_email(request.email,request.phoneNumber)
            else:
                responses = self.contactRepository.get_contacts_with_linked_id(linkedid)

        # process responses
        print(responses)
        emails = [response.email for response in responses if response.email is not None]
        phoneNumbers = [response.phoneNumber for response in responses if response.phoneNumber is not None]
        secondaryContactIds = []
        if len(responses) > 1:
            secondaryContactIds = [response.id for response in responses[1:]]
        return IdentifyResponse(
            primaryContatctId=responses[0].id,
            emails=list(set(emails)),
            phoneNumbers=list(set(phoneNumbers)),
            secondaryContactIds=secondaryContactIds
        ).ret_json()



