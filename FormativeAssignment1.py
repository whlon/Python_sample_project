# FormativeAssignment1.py - Support Ticket Prioritiser
# Purpose: Prototype processing logic for a support ticket system -
# stores fictional tickets, finds a ticket by id, lists unique categories
# and sorts tickets by priority. No real ticket data is used.

tickets = [
    {"id": 1, "category": "Login", "priority": "High", "summary": "User cannot reset password"},
    {"id": 2, "category": "Network", "priority": "Medium", "summary": "Slow VPN connection"},
    {"id": 3, "category": "Login", "priority": "Low", "summary": "Minor UI glitch on login page"},
    {"id": 4, "category": "Hardware", "priority": "High", "summary": "Laptop won't power on"},
    {"id": 5, "category": "Software", "priority": "Medium", "summary": "Application crashes on save"},
    {"id": 6, "category": "Network", "priority": "High", "summary": "Office wifi down for whole floor"},
]

# Maps each priority label to a number for sorting - lower number = higher priority
PRIORITY_ORDER = {"High": 1, "Medium": 2, "Low": 3}


def display_tickets(ticket_list):
    """Print each ticket on its own line."""
    for ticket in ticket_list:
        print(f"ID: {ticket['id']}, Category: {ticket['category']}, "
              f"Priority: {ticket['priority']}, Summary: {ticket['summary']}")


def get_unique_categories(ticket_list):
    """Return a set of category names, with duplicates removed."""
    return {ticket["category"] for ticket in ticket_list}


def find_ticket(ticket_list, search_id):
    """Return the ticket with the matching id, or None if there isn't one."""
    for ticket in ticket_list:
        if ticket["id"] == search_id:
            return ticket
    # None is always the "not found" result, so the caller can
    # simply check "if result is None"
    return None


def sort_tickets_by_priority(ticket_list):
    """Return a new list of tickets ordered High -> Medium -> Low."""
    # Sorting the words alphabetically would give High, Low, Medium,
    # which is wrong. PRIORITY_ORDER turns each word into a number instead.
    return sorted(ticket_list, key=lambda ticket: PRIORITY_ORDER[ticket["priority"]])


def get_ticket_id():
    """Ask the user for a ticket id and keep asking until they enter a whole number."""
    while True:
        user_input = input("\nEnter a ticket id to search for: ")
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a whole number, for example 4.")


def main():
    print("--- All Tickets ---")
    display_tickets(tickets)

    print("\n--- Unique Categories ---")
    categories = get_unique_categories(tickets)
    # sorted() gives the same alphabetical order every time the program runs
    print(", ".join(sorted(categories)))

    search_id = get_ticket_id()
    found_ticket = find_ticket(tickets, search_id)

    if found_ticket is not None:
        print(f"Found: ID {found_ticket['id']}, {found_ticket['summary']}")
    else:
        print(f"No ticket found with id {search_id}.")

    print("\n--- Tickets Sorted by Priority ---")
    sorted_tickets = sort_tickets_by_priority(tickets)
    display_tickets(sorted_tickets)


if __name__ == "__main__":
    main()