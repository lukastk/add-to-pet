# %% [markdown]
# # app

# %%
#|default_exp app

# %%
#|hide
import nblite; from nbdev.showdoc import show_doc; nblite.nbl_export()

# %%
#|export
import typer

# %%
#|export
app = typer.Typer(invoke_without_command=True)
