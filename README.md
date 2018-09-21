Welcome to Quest Journal's documentation!
*****************************************

   usage: journal [-h] {get,complete,add} ...


Positional Arguments
====================

subcommand

Possible choices: get, complete, add


Sub-commands:
=============


get
---

Retrive information on the current journal state.

   journal get [-h] [--no-flavor] section [title]


Positional Arguments
~~~~~~~~~~~~~~~~~~~~

section

Get information on a specfic section of the journal.

title

Get information on a specfic task.


Named Arguments
~~~~~~~~~~~~~~~

--no-flavor

Remove flavor text display objectives in a line seperated format

Default: False


complete
--------

Complete a specified objective.

   journal complete [-h] section [title]


Positional Arguments
~~~~~~~~~~~~~~~~~~~~

section

The section of the objective to complete.

title

The title of the objective to complete.


add
---

Adds a new objective to the journal in the specified section

   journal add [-h] section [title] [due_date]


Positional Arguments
~~~~~~~~~~~~~~~~~~~~

section

The section for the new journal entry.

title

The title of new journal entry

due_date

The due date of the new entry

Copyright 2018 Terry Patterson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
