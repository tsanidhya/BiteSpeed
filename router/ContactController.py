from flask import Blueprint,request

from config.db import PostgresConnect
from dto.identify.request import IdentifyRequest
from db_repository.ContactRepository import ContactRepository
from service.ContactService import ContactService

#static initialize #singleton pattern
contact_blueprint = Blueprint('contact', __name__, url_prefix='/contact')
postgres_db = PostgresConnect()
engine = postgres_db.engine
contactRepository = ContactRepository(engine)
contactService = ContactService(contactRepository)


@contact_blueprint.route('/identify', methods=["POST"])
def identify(request=request):
    email = request.json['email']
    phoneNumber = request.json['phoneNumber']
    if not email and not phoneNumber:
        return "Email and phoneNumber cannot be both now", 400  # status return
    identify_request = IdentifyRequest(email, phoneNumber)
    return contactService.execute(identify_request), 200
