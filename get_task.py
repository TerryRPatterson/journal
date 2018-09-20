import arrow
local = arrow.utcnow().to("US/Eastern")


def get_single(due, title, section):
    if due == "Not Due":
        return (f"\t{section} objective: {title}.\n")
    else:
        dueDate = arrow.get(due)
        if local > dueDate:
            return (f"\t{section} objective {title} was due "
                    f"{dueDate.humanize()}.\n")
        else:
            return (f"\t{section} objective {title} must be completed in"
                    f"{dueDate.humanize()}.\n")


def primary_get(journal):
    title = journal["Primary"]["Title"]
    due = journal["Primary"]["Due"]
    return get_single(due, title, "Primary")


def section_get(section, journal):
    output = ""
    for objective in journal[section]:
        title = objective["Title"]
        due = objective["Due"]
        output += get_single(due, title, section)
    return f"Your objectives in {section} are:\n{output}"


def daily_get(journal):
    completed = []
    not_completed = []
    output_not_completed = " Now you must complete:\n"
    output_completed = "You have finshed:\n"
    not_completed_string = ""
    completed_string = ""

    for task in journal["Daily"]:
        last_done = task["last_done"]
        if last_done == "NULL":
            not_completed.append(task)
            continue
        day = local.format("DD")
        last_day = arrow.get(last_done).format("DD")
        if day == last_day:
            completed.append(task)
        else:
            not_completed.append(task)

    for task in not_completed:
        title = task["Title"]
        not_completed_string += f"\t{title}\n"
    for task in completed:
        title = task["Title"]
        completed_string += f"\t{title}\n"
    if len(completed) == 0:
        return ("You have not completed any tasks today.\nYou must finish:\n"
                f"{not_completed_string}")
    elif len(not_completed) == 0:
        return ("You have completed all daily objective")
    else:
        return (output_completed + completed_string + output_not_completed +
                not_completed_string)


def get(args, journal):
    if args.section == "Primary":
        return primary_get(journal)
    elif args.section == "Daily":
        return daily_get(journal)
    elif args.section in journal.keys():
        return section_get(args.section, journal)
    else:
        raise SyntaxError(f"Section: {section} was not found")
