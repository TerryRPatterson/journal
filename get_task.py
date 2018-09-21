import arrow
local = arrow.utcnow().to("US/Eastern")


def get_single(due, title, section, flavor):
    if due == "Not Due":
        if flavor:
            return (f"\t{section} objective: {title}.")
        else:
            return f"{title}"
    else:
        dueDate = arrow.get(due)
        print(flavor)
        if flavor:
            if local > dueDate:
                    return (f"\t{section} objective {title} was due "
                            f"{dueDate.humanize()}.")
            else:
                if flavor:
                    return (f"\t{section} objective {title} must be completed "
                            f"in {dueDate.humanize()}.")
        else:
            return f"{Title} Due:{dueDate.humanize()}"


def primary_get(journal, flavor):
    title = journal["Primary"]["Title"]
    due = journal["Primary"]["Due"]
    return get_single(due, title, "Primary", flavor)


def section_get(section, journal, flavor):
    output = ""
    for objective in journal[section]:
        title = objective["Title"]
        due = objective["Due"]
        output += f"{get_single(due, title, section, flavor)} \n"
    if flavor:
        return f"Your objectives in {section} are:\n{output}"
    else:
        return output


def daily_get(journal, flavor):
    if not flavor:
        prefix = ""
    else:
        prefix = "\t"
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
        not_completed_string += f"{prefix}{title}\n"
    for task in completed:
        title = task["Title"]
        completed_string += f"{prefix}{title}\n"
    if not flavor:
        return not_completed_string
    else:
        if len(completed) == 0:
            return ("You have not completed any tasks today.\nYou must finish:"
                    f"\n{not_completed_string}")
        elif len(not_completed) == 0:
            return ("You have completed all daily objective")
        else:
            return (output_completed + completed_string + output_not_completed
                    + not_completed_string)


def get(args, journal):
    if args.section == "Primary":
        return primary_get(journal, args.flavor)
    elif args.section == "Daily":
        return daily_get(journal, args.flavor)
    elif args.section in journal.keys():
        return section_get(args.section, journal, args.flavor)
    else:
        raise SyntaxError(f"Section: {section} was not found")
