def create_ticket(category, description):
    if not category or not description:
        return None

    ticket = {
        "id": "IT-1001",
        "category": category,
        "description": description,
        "status": "New"
    }

    return ticket

def assign_ticket(ticket, staff_name, authorized_staff):
    if staff_name not in authorized_staff:
        return False

    ticket["assigned_to"] = staff_name
    ticket["status"] = "Assigned"
    return True
    

