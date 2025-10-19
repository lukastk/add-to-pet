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
def add(
    cmd: Annotated[str, Argument(help="The command to add to pet.")],
    description: Annotated[str, Option("-d", "--description", help="The description of the command.")] = "",
    output: Annotated[str, Option("-o", "--output", help="The output of the command.")] = None,
    tags: Annotated[list[str], Option("-t", "--tags", help="The tags of the command.")] = [],
    snippets_path: Annotated[str|None, Option("-p", "--snippets-path", help="Path to the snippets file.")] = None,
): ...


# %%
snippets_path = None

# %%
#|export
snippets_path = const.snippets_path if snippets_path is None else Path(snippets_path)

# %%
#|export

