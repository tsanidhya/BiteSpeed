import typing as t

class IdentifyRequest:
    email: t.Optional[str]
    phoneNumber: t.Optional[str]

    def __init__(self,email,phoneNumber):
        self.email=email
        self.phoneNumber=phoneNumber