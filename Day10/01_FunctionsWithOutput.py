# Functions with outputs

def format_name(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    print(f"{first_name} {last_name}")
    return f"{first_name} {last_name}"


format_name("louis", "FARES")
