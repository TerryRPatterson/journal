Welcome to Quest Journal's documentation!
*****************************************
```
   usage: journal [-h] {get,complete,add} ...
```

Positional Arguments
====================

subcommand

Possible choices: get, complete, add


Sub-commands:
=============


get
---

Retrive information on the current journal state.
```
   journal get [-h] [--no-flavor] section [title]
```

**Positional Arguments**


__section__

Get information on a specfic section of the journal.

__title__

Get information on a specfic task.


**Named Arguments**


__--no-flavor__

Remove flavor text display objectives in a line seperated format.


complete
--------

Complete a specified objective.
```
   journal complete [-h] section [title]

```
**Positional Arguments**


__section__

The section of the objective to complete.

__title__

The title of the objective to complete.


add
---

Adds a new objective to the journal in the specified section
```
   journal add [-h] section [title] [due_date]
```

Positional Arguments


__section__

The section for the new journal entry.

__title__

The title of new journal entry

__due_date__

The due date of the new entry
