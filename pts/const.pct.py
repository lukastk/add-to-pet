# %% [markdown]
# # const

# %%
#|default_exp const

# %%
#|hide
import nblite; from nbdev.showdoc import show_doc; nblite.nbl_export()

# %%
#|export
from pathlib import Path
import add_to_pet as proj

# %%
#|export
snippets_path = Path.home() / ".config/pet/snippet.toml"
