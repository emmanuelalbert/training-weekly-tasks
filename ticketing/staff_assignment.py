class ITStaff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id
        self.assigned_tickets = []

    def assign_ticket(self, ticket):
        ticket.assign(self.name)
        self.assigned_tickets.append(ticket.ticket_id)

    def view_assigned_tickets(self):
        print(f"Tickets assigned to {self.name}:")

        for ticket_id in self.assigned_tickets:
            print(ticket_id)