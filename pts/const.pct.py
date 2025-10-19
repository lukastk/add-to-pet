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
root_path = Path(proj.__file__).parent.resolve()
store_path = Path(root_path, 'store')
caches_path = Path(store_path, 'caches')
data_path = Path(store_path, 'data')
misc_path = Path(store_path, 'misc')
pre_output = Path(store_path, 'pre_output')
output_path = Path(store_path, 'output')

# %%
#|export
store_path.mkdir(parents=True, exist_ok=True)
caches_path.mkdir(parents=True, exist_ok=True)
data_path.mkdir(parents=True, exist_ok=True)
misc_path.mkdir(parents=True, exist_ok=True)
pre_output.mkdir(parents=True, exist_ok=True)
output_path.mkdir(parents=True, exist_ok=True)

# %%
#|export
snippets_path = Path.home() / ".config/pet/snippet.toml"
