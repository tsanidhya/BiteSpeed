import typing as t
from datetime import datetime

class Contact:
    id : int
    phoneNumber: t.Optional[str]
    email: t.Optional[str]
    linkedId: t.Optional[int]
    linkPrecedence: str
    createdAt: datetime
    updatedAt: datetime
    deletedAt: t.Optional[int]

    @classmethod
    def from_response(cls, response):
        d = response
        print("d",d)

        obj =  cls()
        obj.id = d['id']
        obj.phoneNumber=d['phonenumber']
        obj.email=d['email']
        obj.linkedId=d['linkedid']
        obj.linkPrecedence=d['linkprecedence']
        obj.createdAt=d['createdat']
        obj.updatedAt=d['updatedat']
        obj.deletedAt=d['deletedat'] if d['deletedat'] else None
        return obj
