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