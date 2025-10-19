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
    tags: Annotated[list[str], Option("-t", "--tags", help="The tags of the command.")] = [],
    snippets_path: Annotated[str|None, Option("-p", "--snippets-path", help="Path to the snippets file.")] = None,
): ...


# %%
cmd = "ls -l"
description = "List the contents of the current directory in long format"
output = ""
tags = ["list", "directory"]
snippets_path = "./test_snippet.toml"

# %%
#|export
snippet = {
    "command": cmd,
    "Description": description,
    "Output": output,
    "Tag": tags,
}

# %%
#|export
snippets_path = const.snippets_path if snippets_path is None else Path(snippets_path)
snippets_data = toml.loads(open(snippets_path).read())
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
