# Support Ticket Prioritiser

A small Python prototype showing the processing logic behind a support ticket system. It stores a list of **fictional** support tickets and can:

- display every ticket
- list the unique ticket categories
- find a ticket by its ID
- sort tickets by priority (High → Medium → Low)

Formative Assignment 1 – Level 3 Software Development.

---

## Getting started

You need **Python 3** and **Git** installed. No extra packages are required.

**1. Clone the repository**

```bash
git clone https://github.com/whlon/REPOSITORY-NAME.git
```

**2. Move into the project folder**

```bash
cd REPOSITORY-NAME
```

**3. Run the program**

```bash
python3 FormativeAssignment1.py
```

When asked, type a ticket ID (for example `4`) and press Enter.

## Example output

```text
--- All Tickets ---
ID: 1, Category: Login, Priority: High, Summary: User cannot reset password
ID: 2, Category: Network, Priority: Medium, Summary: Slow VPN connection
...

--- Unique Categories ---
Hardware, Login, Network, Software

Enter a ticket id to search for: 4
Found: ID 4, Laptop won't power on

--- Tickets Sorted by Priority ---
ID: 1, Category: Login, Priority: High, Summary: User cannot reset password
ID: 4, Category: Hardware, Priority: High, Summary: Laptop won't power on
ID: 6, Category: Network, Priority: High, Summary: Office wifi down for whole floor
ID: 2, Category: Network, Priority: Medium, Summary: Slow VPN connection
ID: 5, Category: Software, Priority: Medium, Summary: Application crashes on save
ID: 3, Category: Login, Priority: Low, Summary: Minor UI glitch on login page
```

---

## How it works

### Data

Each ticket is a **dictionary** with four keys: `id`, `category`, `priority` and `summary`. All the tickets are kept in a **list** called `tickets`.

### Functions

| Function | What it does | Returns |
|---|---|---|
| `display_tickets(ticket_list)` | Prints each ticket on one line | Nothing (prints only) |
| `get_unique_categories(ticket_list)` | Collects every category, with no repeats | A **set** of category names |
| `find_ticket(ticket_list, search_id)` | Checks each ticket in turn (linear search) for a matching ID | The matching ticket, or `None` if not found |
| `sort_tickets_by_priority(ticket_list)` | Orders tickets High → Medium → Low | A new sorted list (the original is unchanged) |
| `get_ticket_id()` | Asks the user for an ID and keeps asking until a whole number is entered | The ID as a whole number |
| `main()` | Runs the program steps in order | Nothing |

### Key code

**Storing a ticket** – each ticket is a dictionary inside a list:

```python
tickets = [
    {"id": 1, "category": "Login", "priority": "High", "summary": "User cannot reset password"},
    {"id": 2, "category": "Network", "priority": "Medium", "summary": "Slow VPN connection"},
    # ... more tickets
]
```

**Finding unique categories** – a set comprehension removes duplicates:

```python
def get_unique_categories(ticket_list):
    """Return a set of category names, with duplicates removed."""
    return {ticket["category"] for ticket in ticket_list}
```

**Finding a ticket by ID** – a linear search that returns `None` if nothing matches:

```python
def find_ticket(ticket_list, search_id):
    """Return the ticket with the matching id, or None if there isn't one."""
    for ticket in ticket_list:
        if ticket["id"] == search_id:
            return ticket
    return None
```

**Sorting by priority** – a lookup table turns each priority word into a number:

```python
PRIORITY_ORDER = {"High": 1, "Medium": 2, "Low": 3}

def sort_tickets_by_priority(ticket_list):
    """Return a new list of tickets ordered High -> Medium -> Low."""
    return sorted(ticket_list, key=lambda ticket: PRIORITY_ORDER[ticket["priority"]])
```

**Checking the user's input** – keeps asking until a whole number is entered:

```python
def get_ticket_id():
    """Ask the user for a ticket id and keep asking until they enter a whole number."""
    while True:
        user_input = input("\nEnter a ticket id to search for: ")
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a whole number, for example 4.")
```

### Design decisions

- **A set for categories:** a set removes duplicates automatically, so "Login" and "Network" each appear once even though they are used twice. The categories are then sorted so they print in the same alphabetical order every time.
- **`None` for "not found":** the search always returns either a ticket or `None`, so the main program only needs to check `if found_ticket is not None`.
- **A priority lookup table:** sorting the priority words alphabetically would give High, Low, Medium, which is wrong. `PRIORITY_ORDER` turns each word into a number (High = 1, Medium = 2, Low = 3) so `sorted()` puts them in the correct order.
- **`sorted()` instead of `.sort()`:** `sorted()` returns a new list and leaves the original ticket list in its original order.
- **Input validation:** `get_ticket_id()` uses `try` / `except ValueError`, so typing something that isn't a number shows a friendly message instead of crashing the program.
- **A `main()` function:** all the program steps are kept in one function, which runs only when the file is run directly. This keeps the code organised and lets the functions be reused or tested on their own.

## Testing

| Test | Input | Expected result | Actual result |
|---|---|---|---|
| Find an existing ticket | `4` | `Found: ID 4, Laptop won't power on` | ✅ Pass |
| Search for a missing ticket | `99` | `No ticket found with id 99.` | ✅ Pass |
| Non-number input | `abc` | `Please enter a whole number, for example 4.` and asks again | ✅ Pass |
| Unique categories | – | 4 categories in alphabetical order, no duplicates | ✅ Pass |
| Priority sort | – | All High first, then Medium, then Low | ✅ Pass |

## Possible improvements

- The ticket data is written into the code, so any changes are lost when the program closes. A later version could load tickets from a file or a database.
- Users could be allowed to add new tickets or change a ticket's priority.
- The tests above were done by hand. Automated tests (for example with `unittest`) would make checking the code quicker and more reliable.

## Data and privacy

All tickets are made up for testing. No real ticket or personal data is used.

## Author

Helen Wong