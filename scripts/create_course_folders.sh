#!/bin/bash

# Create course folders for Computer Science with Python
# Safe to run multiple times - won't overwrite existing folders

echo "Creating course directory structure..."

folders=(
    "assessments"
    "challenge_problems"
    "computer_labs"
    "etc"
    "misc"
    "lessons"
    "html"
)

for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        mkdir "$folder"
        echo "✅ Created folder: $folder"
    else
        echo "→ Folder already exists: $folder (skipped)"
    fi
done

echo ""
echo "🎉 All folders are ready!"
