import pytest
from ticket import create_ticket
from ticket import assign_ticket


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

#parametrized testing for staff assignment
@pytest.mark.parametrize(
    "staff_name, expected_result, expected_status, expected_assignee",
    [
        ("Varghese", True, "Assigned", "Varghese"),
        ("Ryan", True, "Assigned", "Ryan"),
        ("David", False, "New", None),
    ]
)
def test_assign_ticket(
    staff_name,
    expected_result,
    expected_status,
    expected_assignee
):
    ticket = {
        "id": "IT-1001",
        "category": "Network",
        "description": "Wi-Fi is not working",
        "status": "New"
    }

    authorized_staff = ["Varghese", "Ryan", "Rinu"]

    result = assign_ticket(
        ticket,
        staff_name,
        authorized_staff
    )

    assert result is expected_result
    assert ticket["status"] == expected_status

    if expected_assignee:
        assert ticket["assigned_to"] == expected_assignee
    else:
        assert "assigned_to" not in ticket