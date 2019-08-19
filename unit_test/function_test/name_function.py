def get_formatted_name(first_name, last_name, middle_name=''):
    """generate a neatly formatted fullname."""
    if middle_name:
        fullname = f"{first_name} {middle_name} {last_name}"
    else:
        fullname = f"{first_name} {last_name}"

    return fullname.title()