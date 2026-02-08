#!/bin/bash

# 1. VARIABLES (No spaces around '=')
NAME="Hersy"
COUNT=1
DIRECTORY_NAME="test_folder"

# 2. FUNCTIONS
# Note: Functions must be defined BEFORE they are called.
greet_user() {
    echo "--- Function Start ---"
    echo "Hello, $1! You are learning $2." # $1 and $2 are arguments
}

# 3. CALLING A FUNCTION
greet_user "$NAME" "Bash Scripting"

# 4. CONDITIONAL (IF/ELSE)
# [ ] is actually a command, so spaces are MANDATORY.
if [ "$NAME" == "Hersy" ]; then
    echo "Access granted: Hello Admin."
else
    echo "Access denied."
fi

# 5. WORKING WITH THE FILE SYSTEM (The "Cool Stuff")
echo "Checking for directory..."
if [ ! -d "$DIRECTORY_NAME" ]; then
    mkdir "$DIRECTORY_NAME"
    echo "Created folder: $DIRECTORY_NAME"
else
    echo "Folder already exists."
fi

# 6. FOR LOOP (Iterating through a range)
echo "Counting to 3:"
for i in {1..3}; do
    echo "Number: $i"
done

# 7. FOR LOOP (Iterating through files - Very common in Bash)
echo "Files in current directory:"
for file in *; do
    echo "Found file: $file"
done

# 8. WHILE LOOP
echo "While loop demo:"
while [ $COUNT -le 3 ]; do
    echo "Count is $COUNT"
    ((COUNT++)) # Double parentheses for math/arithmetic
done

# 9. CAPTURING COMMAND OUTPUT
# This is like 'var result = command()' in other languages
CURRENT_TIME=$(date +%H:%M:%S)
echo "Script finished at: $CURRENT_TIME"
