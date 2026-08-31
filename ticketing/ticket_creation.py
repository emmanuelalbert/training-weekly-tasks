class Ticket:
    def __init__(self, ticket_id, category, description):
        self.ticket_id = ticket_id
        self.category = category
        self.description = description
        self.status = "New"
        self.assigned_to = None
        self.resolution = None

    def assign(self, staff):
        self.assigned_to = staff
        self.status = "Assigned"

    def update_status(self, new_status):
        valid_statuses = [
            "New",
            "Assigned",
            "In Progress",
            "Pending",
            "Resolved",
            "Closed"
        ]

        if new_status not in valid_statuses:
            return False

        self.status = new_status
        return True

    def add_resolution(self, resolution):
        self.resolution = resolution
        self.status = "Resolved"

    def close(self):
        if self.resolution is None:
            return False

        self.status = "Closed"
        return True

    def display_ticket(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Assigned To: {self.assigned_to}")
        print(f"Resolution: {self.resolution}")