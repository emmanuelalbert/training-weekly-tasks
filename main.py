from ticketing.specialized_tickets import NetworkTicket
from ticketing.staff_assignment import ITStaff


ticket = NetworkTicket(
    "IT-1001",
    "Wi-Fi is not working",
    "Wi-Fi"
)

staff = ITStaff(
    "Varghese",
    "IT001"
)

staff.assign_ticket(ticket)

ticket.update_status("In Progress")

ticket.add_resolution(
    "Reset network configuration and reconnected the device."
)

ticket.close()

ticket.display_ticket()