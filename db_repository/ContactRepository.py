from sqlalchemy import Engine
from sqlalchemy import text
from model.Contact import Contact
from datetime import datetime
from enums.ContactEnums import LINKED_PRECEDENCE_ENUMS
class ContactRepository:
    engine:Engine

    def __init__(self,engine):
        self.engine = engine

    def insert_when_phone_number_null(self,email): # returns linked id
        records = self.get_contacts_with_email(email)
        updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")
        if not records:
            #entry as primary
            linkPrecedence = LINKED_PRECEDENCE_ENUMS.PRIMARY.value
            query = f"""
            insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
                values(NULL,'{email}',NULL,'{linkPrecedence}','{updatedAt}',NULL);
            """
            with self.engine.connect() as conn:
                conn.execute(text(query))
                return None
            ################ DONE #################
        # else
        linkedId = records[0].linkedId
        if not linkedId:
            linkedId = records[0].id
        linkPrecedence = LINKED_PRECEDENCE_ENUMS.SECONDARY.value
        query = f"""
        insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
            values(NULL,'{email}',{linkedId},'{linkPrecedence}','{updatedAt}',NULL);
        """
        with self.engine.connect() as conn:
            conn.execute(text(query))
            return linkedId

    def insert_when_email_null(self,phone_number): # returns linked id
        records = self.get_contacts_with_phone(phone_number)
        updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")
        if not records:
            # entry as primary
            linkPrecedence = LINKED_PRECEDENCE_ENUMS.PRIMARY.value
            query = f"""
                    insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
                        values('{phone_number}',NULL,NULL,'{linkPrecedence}','{updatedAt}',NULL);
                    """
            with self.engine.connect() as conn:
                conn.execute(text(query))
                return None
            ################ DONE #################
        # else
        linkedId = records[0].linkedId
        if not linkedId:
            linkedId = records[0].id
        linkPrecedence = LINKED_PRECEDENCE_ENUMS.SECONDARY.value
        query = f"""
                insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
                    values('{phone_number}',NULL,{linkedId},'{linkPrecedence}','{updatedAt}',NULL);
                """
        with self.engine.connect() as conn:
            conn.execute(text(query))
            return linkedId

    def insert_when_email_phone_present(self,email,phone_number): # returns linked id
        records, doEntry = self.get_contacts_with_phone_email(email,phone_number)
        print("records do entry",records,doEntry)
        updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")
        if not doEntry:
            #do no entry, primary already exists
            return records[0].linkedId
        # else
        if not records:
            # entry as primary
            linkPrecedence = LINKED_PRECEDENCE_ENUMS.PRIMARY.value
            query = f"""
                    insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
                        values('{phone_number}','{email}',NULL,'{linkPrecedence}','{updatedAt}',NULL);
                    """
            print("query",query)
            with self.engine.connect() as conn:
                conn.execute(text(query))
                return None
        #else
        linkedId = records[0].linkedId
        if not linkedId:
            linkedId = records[0].id
        linkPrecedence = LINKED_PRECEDENCE_ENUMS.SECONDARY.value
        query = f"""
                    insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
                        values('{phone_number}','{email}',{linkedId},'{linkPrecedence}','{updatedAt}',NULL);
                    """
        with self.engine.connect() as conn:
            conn.execute(text(query))
            return linkedId

    def get_contacts_with_email(self,email):
        query = f"select * from Contact where email = '{email}' order by id asc;"
        with self.engine.connect() as conn:
            response_db = conn.execute(text(query)).mappings().fetchall()
            return Contact.from_responses(response_db)

    def get_contacts_with_phone(self,phone):
        query = f"select * from Contact where phonenumber = '{phone}' order by id asc;"
        with self.engine.connect() as conn:
            response_db = conn.execute(text(query)).mappings().fetchall()
            return Contact.from_responses(response_db)

    def get_contacts_with_linked_id(self,linkedid):
        query = f"select * from Contact where linkedid = '{linkedid}' order by id asc;"
        with self.engine.connect() as conn:
            response_db = conn.execute(text(query)).mappings().fetchall()
            return Contact.from_responses(response_db)

    def get_contacts_with_phone_email(self,email,phone):
        email_responses = self.get_contacts_with_email(email)
        phone_responses = self.get_contacts_with_phone(phone)
        print("email_responses", email_responses)
        print("phone_responses", phone_responses)
        if email_responses and phone_responses:
            return email_responses, False
        if email_responses:
            return email_responses, True
        if phone_responses:
            return phone_responses, True
        return [], True

# Types of operations
# 1. If no entry found for email or phone_number
#     create entry(linkPrecedence  "primary")
# 2. If entry found for email but not phone number
#     create entry(linkPrecedence  "secondary")
#
# email but no phone (primary)
# email & phone (seco)
# phone & no email (seco)
