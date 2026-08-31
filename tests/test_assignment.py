from ticketing.ticket_creation import Ticket
from ticketing.staff_assignment import ITStaff


def test_assign_ticket():
    ticket = Ticket(
        "IT-1003",
        "Hardware",
        "Keyboard is not working"
    )

    staff = ITStaff(
        "Rohit",
        "IT001"
    )

    staff.assign_ticket(ticket)

    assert ticket.assigned_to == "Rohit"
    assert ticket.status == "Assigned"