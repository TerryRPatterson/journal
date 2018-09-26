def add_single(journal, section, title, due_date=None):
    if section not in journal.keys():
        raise SyntaxError("Section does not exist.")
    new_task = {"Title": title,
                "Due": due_date}
    journal[section].append(new_task)
    return f"{title} added to {section}"


def add_primary(journal, title, due_date=None):
    if "Primary" in journal.keys():
        raise SyntaxWarning("You already have a primary objective please"
                            " complete it before assigning another")


def add_daily(journal, title):
    new_daily = {"Title": title,
                 "last_done": "NULL"}
    journal["Daily"].append(new_daily)
    return f"Daily {title} has been added to the agenda"


def add(args, journal):
    if "new_title" in args:
        new_title = args.new_title
    else:
        new_title = None
    if "due" in args:
        due_date = args.due
    else:
        due_date = "Not Due"
    if "title" in args:
        title = args.title
    section = args.section
    if section == "Primary":
        return add_primary(journal, section, title, due_date)
    elif section == "Daily":
        return add_daily(journal, title)
    else:
        return add_single(journal, section, title, due_date)
