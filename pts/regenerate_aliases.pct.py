# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # regenerate_aliases

# %%
#|default_exp regenerate_aliases
#|export_as_func true

# %%
#|hide
import nblite; from nbdev.showdoc import show_doc; nblite.nbl_export()

# %%
#|top_export
import typer
from typer import Option
from typing import Annotated
from pathlib import Path
import toml
import shlex

from add_to_pet import const

regenerate_aliases_app = typer.Typer()

# %%
#|set_func_signature
@regenerate_aliases_app.command()
def regenerate_aliases(
    snippets_path: Annotated[str|None, Option("--snippets-path", help="Path to the snippets file.")] = None,
    aliases_path: Annotated[str|None, Option("--aliases-path", help="Path to the aliases file.")] = None,
): ...

# %%
#|export
snippets_path = const.snippets_path if snippets_path is None else Path(snippets_path)
snippets_data = toml.loads(open(snippets_path).read())
if 'Snippets' not in snippets_data:
    snippets_data['Snippets'] = []

aliases_path = const.aliases_path if aliases_path is None else Path(aliases_path)
if not aliases_path.exists():
    aliases_path.touch()

aliases = []

for snippet in snippets_data["Snippets"]:
    if 'name' not in snippet: continue
    aliases.append(f"alias {snippet['name']}={shlex.quote(snippet['command'])}")

aliases_path.write_text("\n".join(aliases));
