# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`add-to-pet` is a CLI tool and Python library that idempotently adds command snippets to [`pet`](https://github.com/knqyf263/pet), a simple command-line snippet manager. It manages pet's `~/.config/pet/snippet.toml` and generates shell aliases in `~/.config/pet/aliases.sh`.

## Development Setup

- Python 3.11, managed with `uv`
- direnv (`.envrc`) auto-activates the venv
- Install deps: `uv sync`

## Architecture

- **`const.py`** — Default paths for pet config (`snippets_path`, `aliases_path`)
- **`app.py`** — Typer app instance
- **`main.py`** — Core `add_to_pet()` command: parses args, upserts snippet into TOML, regenerates aliases.sh. Uses nblite's function export mode (`#|export_as_func true`) — all `#|export` cells become the body of the `add_to_pet()` function.
- **`utils.py`** — Placeholder utilities

CLI entry point: `add-to-pet` -> `add_to_pet.app:app`

## Running

```bash
# CLI
add-to-pet "echo hello" -d "Say hello" -t "greeting" -n "hello"

# With test fixtures
add-to-pet "ls -l" --snippets-path ./nbs/test_snippet.toml --aliases-path ./nbs/test_aliases.sh
```

## Build System: nblite (literate programming)

This project uses [nblite](https://github.com/lukastk/nblite) (based on nbdev). Source code is authored in notebooks, then exported to Python modules.

**Export pipeline (defined in `nblite.toml`):** `nbs/` (ipynb) -> `pts/` (percent-format .pct.py) -> `add_to_pet/` (library)

### Where to make changes

- **`pts/`** — Percent-format notebook source files (.pct.py). These are the **primary files to edit** for code changes. Cells delimited by `# %%`, with `# %% [markdown]` for markdown cells.
- **`nbs/`** — Jupyter notebook mirrors (synced from/to pts). Used for interactive development.
- **`add_to_pet/`** — **Never edit directly.** Auto-generated library code, overwritten by `nbl export`.

### Critical workflow rules

1. **Never modify files in `add_to_pet/` directly** — they are auto-generated and will be overwritten.
2. **After editing `.pct.py` files, always run `nbl export --reverse`** — this syncs changes back to `.ipynb`. Without this, running `nbl export` (which goes `nbs->pts->lib`) will overwrite your `.pct.py` changes with older `.ipynb` versions.
3. **Then run `nbl export`** to regenerate the Python module from notebooks.

### Workflow for modifying code

```bash
# 1. Edit the .pct.py file in pts/
# 2. Sync pts back to nbs (REQUIRED, otherwise changes get overwritten)
nbl export --reverse
# 3. Export to Python module
nbl export
# 4. Test notebooks execute correctly
nbl test
```

### Workflow for adding a new module

```bash
# 1. Create a new notebook
nbl new pts/new_module.pct.py          # plain module
nbl new pts/new_cmd.pct.py --template script  # function export template
# 2. Edit, then sync and export
nbl export --reverse && nbl export
# 3. Manually update add_to_pet/__init__.py to re-export new public symbols
```

### Key nblite directives

| Directive | Description |
|-----------|-------------|
| `#\|default_exp mod` | Set default export module (once per notebook, near top) |
| `#\|export` | Export cell to module |
| `#\|exporti` | Export but exclude from `__all__` (internal) |
| `#\|top_export` | Export to top of module file, outside function (for imports/constants in function export mode) |
| `#\|hide` | Hide cell from docs (used for setup cells) |
| `#\|export_as_func true` | All `#\|export` cells become the function body |
| `#\|set_func_signature` | Define the function name, parameters, and docstring |
| `#\|func_return` | Prepend `return` to first line of cell |
| `#\|return_line` | Inline directive: adds `return` to that specific line |
| `#\|eval: false` | Skip cell during `nbl fill`/`nbl test` |
| `#\|skip_evals` / `#\|skip_evals_stop` | Skip/resume cell execution |

### Import conventions

nblite automatically converts absolute imports to relative imports during export:
```python
from add_to_pet.utils import helper  # becomes: from .utils import helper
```

### Other nbl commands

```bash
nbl fill                        # Execute notebooks and save outputs
nbl fill path/to/nb.ipynb       # Fill a specific notebook
nbl test                        # Test all notebooks execute without errors
nbl test path/to/nb.ipynb       # Test a specific notebook
nbl clean                       # Remove outputs/metadata from notebooks
```
