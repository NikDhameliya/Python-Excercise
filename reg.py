import json


# TODO
# 1) Try to match registrant's email to our Contacts list
# 2) If not matched, try to match registrant's phone to our Contacts list
# 3) Otherwise try to match our LeadsList with email (if Lead is matched, remove it from LeadsList and add to ContactsList)
# 4) Else match our Leads with phone (same rule as above applies)
# 5) If not matched, simply add it to ContactsList
# Check existing or not if yes then update missing data only


class ContactsList:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class LeadsList:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


def registration():
    contact_data = []
    contact_data.append(ContactsList('Alice Brown', '', '1231112223'))
    contact_data.append(ContactsList('Bob', 'bob@crowns.com', ''))
    contact_data.append(ContactsList(
        'Carlos Drew', 'carl@drewess.com', '3453334445'))
    contact_data.append(ContactsList('Doug', '', '4564445556'))
    contact_data.append(ContactsList(
        'Egan Fair', 'eg@fairness.com', '5675556667'))

    lead_data = []
    lead_data.append(LeadsList('', 'kevin@keith.com', ''))
    lead_data.append(LeadsList('Lucy', 'lucy@liu.com', '3210001112'))
    lead_data.append(LeadsList('Mary Middle', 'mary@middle.com', '3331112223'))
    lead_data.append(LeadsList('', '', '4442223334'))
    lead_data.append(LeadsList('', 'ole@olson.com', ''))

    json_input = '''[
        {"registrant":
            { 
                "name": "Lucy Liu",
                "email": "lucy@liu.com",
                "phone": ""
            }
        },
        {"registrant":
            {
                "name": "Doug",
                "email": "doug@emmy.com",
                "phone": "4564445556"
            }
        },
        {
        "registrant":
            {
                "name": "Uma Thurman",
                "email": "uma@thurs.com",
                "phone": ""
            }
        }
    ]'''

    print ("CONTACT BEFORE >>>>>")
    for contact in contact_data:
        print (json.dumps(contact.__dict__))

    print ("LEAD BEFORE >>>>>")
    for lead in lead_data:
        print (json.dumps(lead.__dict__))

    registrants = json.loads(json_input)

    for registrant in registrants:
        email = registrant['registrant']['email']
        phone = registrant['registrant']['phone']
        name = registrant['registrant']['name']
        is_found_in_contact = False
        is_found_in_lead = False

        for contact in contact_data:
            # Try to match and update missing data
            if email and email == contact.email:
                print("FOUND EMAIL IN CONTACT", contact.email)
                # Update missing data
                if name and not contact.name:
                    setattr(contact, 'name', name)
                if phone and not contact.phone:
                    setattr(contact, 'phone', phone)
                is_found_in_contact = True
            elif phone and phone == contact.phone:
                # Update missing data
                if name and not contact.name:
                    setattr(contact, 'name', name)
                if email and not contact.email:
                    setattr(contact, 'email', email)
                    print("FOUND PHONE IN CONTACT", contact.email)
                is_found_in_contact = True

        if not is_found_in_contact:
            for lead in lead_data:
                if email and email == lead.email:
                    print("FOUND EMAIL IN LEAD", lead.email)
                    # add contact and remove lead
                    contact_data.append(ContactsList(name, email, phone))
                    is_found_in_lead = True
                    lead_data.remove(lead)
                elif phone and phone == lead.phone:
                    print("FOUND PHONE IN LEAD", lead.phone)
                    contact_data.append(ContactsList(name, email, phone))
                    # add contact and remove lead
                    is_found_in_lead = True
                    lead_data.remove(lead)


        if not is_found_in_lead and not is_found_in_contact:
            # add to the contactlist
            contact_data.append(ContactsList(name, email, phone))

    print ("CONTACT AFTER >>>>>")
    for contact in contact_data:
        print (json.dumps(contact.__dict__))

    print ("LEAD AFTER >>>>>")
    for lead in lead_data:
        print (json.dumps(lead.__dict__))



registration()
