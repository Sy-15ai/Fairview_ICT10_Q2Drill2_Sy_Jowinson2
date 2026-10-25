from pyscript import display
from js import document


# Grade 7 members
grade_seven = {
    "Alex Cruz",
    "Mia Santos",
    "Noah Reyes"
}

# Grade 8 members
grade_eight = {
    "Liam Garcia",
    "Sofia Flores",
    "Ethan Ramos"
}

# Grade 9 members
grade_nine = {
    "Lucas Aquino",
    "Chloe Torres",
    "Daniel Mendoza"
}

# Grade 10 members
grade_ten = {
    "Nathan Navarro",
    "Emma Castillo",
    "Ryan Bautista"
}


# Adds a new student to the club
def add_member(event):

    # Get the first and last name
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    # Create a set for the new member
    added_member = {first + " " + last}

    # Combine all grade sets with the new member
    all_members = (
        grade_seven
        | grade_eight
        | grade_nine
        | grade_ten
        | added_member
    )

    # Sort the members alphabetically
    members_list = "<br>".join(sorted(all_members))

    # Find the total number of members
    member_count = len(all_members)

    # Create the HTML output using an f-string
    result = f"""
        <h5>Member Directory</h5>

        <div class="members">
            {members_list}
        </div>

        <hr>

        <div class="total">
            Total Members: {member_count}
        </div>
    """

    # Display the updated member list
    display(result, target="results")   