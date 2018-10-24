import arrow


def add_single(journal, section, title, due_date):
    if section not in journal.keys():
        raise SyntaxError("Section does not exist.")

    new_task = {"Title": title,
                "Due": due_date}
    journal[section].append(new_task)
    if due_date == "Not Due":
        return f"{title} was added as {section}."
    else:
        return (
                f"""{title} was added to {section} and is due in {arrow
                                                               .get(due_date)
                                                               .humanize()}."""
                                                               )


def add_primary(journal, title, due_date):
    if "Primary" in journal.keys() and journal["Primary"]:
        raise SyntaxWarning("You already have a primary objective please"
                            " complete it before assigning another")
    journal["Primary"] = {
                            "Title": title,
                            "Due": due_date
                            }
    if due_date == "Not Due":
        return f"{title} was added as primary."
    else:
        return (
                f"""{title} was added to primary and is due in {arrow
                                                                .get(due_date)
                                                               .humanize()}""")


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
    if "due_date" in args:
        due_date = args.due_date
    else:
        due_date = "Not Due"
    if "title" in args:
        title = args.title
    section = args.section
    if section == "Primary":
        return add_primary(journal, title, due_date)
    elif section == "Daily":
        return add_daily(journal, title)
    else:
        return add_single(journal, section, title, due_date)
