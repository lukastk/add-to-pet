#!/bin/bash

# Requires toml-cli
# > cargo install toml-cli


# Use yq instead ...

SNIPPETS_PATH="~/.config/pet/snippet.toml"
SNIPPETS_PATH="./snippet.toml"


CMD_TO_ADD="echo"
CMD_DESCRIPTION="Echo the command"
CMD_TAGS="tag1,tag2"
CMD_OUTPUT="output"

SNIPPETS=$(toml get $SNIPPETS_PATH "Snippets")

# Extract index of the first match, or length of list if not found
OLD_CMD_INDEX=$(
  jq --arg CMD_TO_ADD "$CMD_TO_ADD" '
    to_entries
    | map(select(.value.command == $CMD_TO_ADD) | .key)
    | if length > 0 then .[0] else (input | length) end
  ' <<< "$SNIPPETS" <<< "$SNIPPETS"
)

CMD_TAGS=$(jq -Rc 'split(",")' <<< "$CMD_TAGS")

toml set $SNIPPETS_PATH "Snippets[$OLD_CMD_INDEX].command" "$CMD_TO_ADD" > /tmp/tmp.toml
toml set /tmp/tmp.toml "Snippets[$OLD_CMD_INDEX].Description" "$CMD_DESCRIPTION" > /tmp/tmp2.toml
toml set /tmp/tmp3.toml "Snippets[$OLD_CMD_INDEX].Output" "$CMD_OUTPUT" > /tmp/tmp4.toml
mv /tmp/tmp4.toml $SNIPPETS_PATH

for i in {1..99}; do
  toml set $SNIPPETS_PATH "Snippets[$OLD_CMD_INDEX].Tag[$i]" " > /tmp/tmp.toml
  mv /tmp/tmp.toml $SNIPPETS_PATH
done




