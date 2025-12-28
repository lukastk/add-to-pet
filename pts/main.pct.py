# %% [markdown]
# # main

# %%
#|default_exp main
#|export_as_func true

# %%
#|hide
import nblite; from nbdev.showdoc import show_doc; nblite.nbl_export()

# %%
#|top_export
import typer
from typer import Argument, Option
from typing_extensions import Annotated
from pathlib import Path
import toml
import json

from add_to_pet import const
from add_to_pet.app import app


# %%
#|set_func_signature
@app.command()
def add_to_pet(
    cmd: Annotated[str, Argument(help="The command to add to pet.")],
    description: Annotated[str, Option("-d", "--description", help="The description of the command.")] = "",
    output: Annotated[str, Option("-o", "--output", help="The output of the command.")] = "",
    tag: Annotated[list[str], Option("-t", "--tag", help="The tags of the command.")] = [],
    alias: Annotated[str, Option("-a", "--alias", help="The alias of the command. Will be added to ~/.config/pet/aliases.sh, as well as to the description.")] = None,
    snippets_path: Annotated[str|None, Option("--snippets-path", help="Path to the snippets file.")] = None,
    aliases_path: Annotated[str|None, Option("--aliases-path", help="Path to the aliases file.")] = None,
): ...


# %%
cmd = "ls -l"
description = "List the contents of the current directory in long format"
output = ""
tag = ["list", "directory"]
snippets_path = "./test_snippet.toml"
aliases_path = "./test_aliases.sh"
alias = "lll"

# %%
#|export
if alias:
    _description = f"({alias}) {description}"
else:
    _description = description

snippet = {
    "command": cmd,
    "Description": _description,
    "Output": output,
    "Tag": tag,
    "alias": alias,
}

# %%
#|export
snippets_path = const.snippets_path if snippets_path is None else Path(snippets_path)
snippets_data = toml.loads(open(snippets_path).read())
if 'Snippets' not in snippets_data:
    snippets_data['Snippets'] = []
duplicate_snippets = [i for i, s in enumerate(snippets_data["Snippets"]) if s["command"] == cmd]

if len(duplicate_snippets) == 1:
    snippet_index = duplicate_snippets[0]
    snippets_data["Snippets"][snippet_index] = snippet
elif len(duplicate_snippets) > 1:
    raise ValueError(f"Found {len(duplicate_snippets)} duplicate snippets for command {cmd}. Maximum number of duplicates allowed is 1.")
else:
    snippets_data["Snippets"].append(snippet)

with open(snippets_path, "w") as f:
    f.write(toml.dumps(snippets_data))

# %%
const.snippets_path.parent / "alias.sh"

# %% [markdown]
# Create the `alias.sh` file

# %%
#|export
import shlex

aliases_path = const.aliases_path if aliases_path is None else Path(aliases_path)
if not aliases_path.exists():
    aliases_path.touch()

aliases = []

for snippet in snippets_data["Snippets"]:
    if 'alias' not in snippet: continue
    aliases.append(f"alias {snippet['alias']}={shlex.quote(snippet['command'])}")

aliases_path.write_text("\n".join(aliases));
