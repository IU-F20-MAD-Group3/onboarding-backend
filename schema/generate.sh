#!/usr/bin/env bash

set -e

IMAGES_DIR_PATH="images/"
SCHEMA_BASE_PATH="schema/"

echo "Cleaning images directory..."
rm -f "${IMAGES_DIR_PATH}*"
echo "Done"
echo

echo "Generating schema images..."
for f in "$SCHEMA_BASE_PATH"*.puml; do
  echo "$f"
  schema_name=$(basename "${f%%.*}")
  img_path="${IMAGES_DIR_PATH}${schema_name}.svg"
  docker run --rm -i think/plantuml:latest <"$f" >"$img_path"
done
echo "Done"
