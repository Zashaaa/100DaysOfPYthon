# Functions with outputs

def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Names cannot be empty"
    first_name = first_name.title()
    last_name = last_name.title()
    return f"{first_name} {last_name}"


fn = input("What is your first name? ")
ln = input("What is your last name? ")
print(format_name(fn, ln))
