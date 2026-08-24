from ticket_creation import create_ticket


def test_create_ticket():
    ticket = create_ticket(
        "Network",
        "Unable to connect to the VPN"
    )
    assert ticket["id"] == "IT-1001"
    assert ticket["category"] == "Network"
    assert ticket["description"] == "Unable to connect to the VPN"
    assert ticket["status"] == "New"
    
def test_ticket_requires_category_and_description():
    ticket = create_ticket("", "")
    assert ticket is None