import typing as t
from datetime import datetime
from enums.ContactEnums import LINKED_PRECEDENCE_ENUMS
class Contact:
    id : int
    phoneNumber: t.Optional[str]
    email: t.Optional[str]
    linkedId: t.Optional[int]
    linkPrecedence: LINKED_PRECEDENCE_ENUMS
    createdAt: datetime
    updatedAt: datetime
    deletedAt: t.Optional[int]

    @classmethod
    def from_response(cls, response):
        d = response
        print("d",d)
        obj =  cls()
        obj.id = d['id']
        obj.phoneNumber=d['phonenumber'] if d['phonenumber'] else None
        obj.email=d['email'] if d['email'] else None
        obj.linkedId=d['linkedid'] if d['linkedid'] else None
        obj.linkPrecedence=d['linkprecedence']
        obj.createdAt=d['createdat']
        obj.updatedAt=d['updatedat']
        obj.deletedAt=d['deletedat'] if d['deletedat'] else None
        return obj

    @classmethod
    def from_responses(cls, responses):
        obj_list =[]
        for response in responses:
            obj_list.append(cls.from_response(response))
        return obj_list


