from ticketing.ticket_creation import Ticket
from ticketing.specialized_tickets import NetworkTicket

def test_create_ticket():
    ticket = Ticket(
        "IT-1001",
        "Network",
        "Unable to connect to the VPN"
    )

    assert ticket.ticket_id == "IT-1001"
    assert ticket.category == "Network"
    assert ticket.description == "Unable to connect to the VPN"
    assert ticket.status == "New"


def test_create_network_ticket():
    ticket = NetworkTicket(
        "IT-1002",
        "Unable to connect to the VPN",
        "VPN"
    )

    assert ticket.ticket_id == "IT-1002"
    assert ticket.category == "Network"
    assert ticket.description == "Unable to connect to the VPN"
    assert ticket.network_type == "VPN"
    assert ticket.status == "New"