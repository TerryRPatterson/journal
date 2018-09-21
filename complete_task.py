import arrow

local = arrow.utcnow().to("US/Eastern")


def complete_daily(title, journal):
    dailies = journal["Daily"]
    output = "I am sorry that task was not found\n"
    for task in dailies:
        if task["Title"] == title:
            task["last_done"] = local.format()
            output = f"{title} completed.\n"
    return (output)


def complete_task(journal, section, title):
    found = False
    length = len(journal[section])
    for x in range(0, length):
        if journal[section][x]["Title"] == title:
            del journal[section][x]
            found = True
            break
    if found:
        return f"{section} objective: {title} was completed.\n"
    else:
        raise SyntaxError(f"{section} objective: {title} not found.\n")


def complete_primary(journal, new_title=None, due=None):
    old_title = journal["Primary"]["Title"]
    if new_title is None:
        del journal["Primary"]
        return f"You have completed: {old_title}!"
    else:
        journal["Primary"]["Title"] = new_title
        if due is not None:
            journal["Primary"]["Due"] = due
            return (f"You have completed: {old_title}\n Your new primary "
                    f"objective is {new_title} due "
                    f"{arrow.get(due).humanize()}.\n")
        else:
            journal["Primary"]["Due"] = "Not Due"
            return (f"You have completed: {old_title}\n Your new primary "
                    f"objective is {new_title}.\n")


def complete(args, journal):
    if "new_title" in args:
        new_title = args.new_title
    else:
        new_title = None
    if "due" in args:
        due = args.due
    else:
        due = None
    if "title" in args:
        title = args.title
    section = args.section

    if section == "Daily":
        return complete_daily(title, journal)
    elif section == "Primary":
        return complete_primary(journal, new_title=new_title, due=due)
    else:
        return complete_task(journal, section, title)
