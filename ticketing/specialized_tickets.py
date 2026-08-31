from .ticket_creation import Ticket

class NetworkTicket(Ticket):
    def __init__(self, ticket_id, description, network_type):
        super().__init__(
            ticket_id,
            "Network",
            description
        )

        self.network_type = network_type

    def display_network_details(self):
        print(f"Network Type: {self.network_type}")