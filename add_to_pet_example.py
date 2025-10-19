# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "add-to-pet",
#     "toml",
#     "typer",
# ]
#
# [tool.uv.sources]
# add-to-pet = { git = "https://github.com/lukastk/add-to-pet.git" }
# ///

from add_to_pet import add_to_pet

add_to_pet(
    cmd="echo 'Hello world'",
    description="Display 'Hello world'",
    tags=["a-tag", "another-tag"],
    snippets_path="./nbs/test_snippet.toml"
)
