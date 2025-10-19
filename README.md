# add-to-pet


Simple CLI utility to add commands to [`pet`](https://github.com/knqyf263/pet) idempotently.

<!-- #region -->
# Installation

```bash
pip install "git+https://github.com/astral-sh/ruff"
```

Using `uv`:

```bash
uvx --from git+https://github.com/lukastk/add-to-pet.git 
```
<!-- #endregion -->

<!-- #region -->
# Usage

To use `add-to-pet` you must first install [`pet`](https://github.com/knqyf263/pet).

## CLI

```bash
add-to-pet "echo 'Hello world'" -d "Display 'Hello world'" -t "a-tag" -t "another-tag"
```

To see a list of all available options:

```bash
add-to-pet --help
```

## Module

```python
from add_to_pet import add_to_pet

add_to_pet(
    cmd="echo 'Hello world'",
    description="Display 'Hello world'",
    tags=["a-tag", "another-tag"]
)
```

## Standalone script

Modify and run this script using [`uv`](https://docs.astral.sh/uv/) as follows:

```
uv run add_to_pet_example.py
```

The dependencies are all declared in the inline script metadata.
<!-- #endregion -->
