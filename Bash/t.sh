#!/bin/bash
create_java(){
DIRECTORY_NAME="javaFiles"
FILENAME="Main.java"
FULLPATH="$DIRECTORY_NAME/$FILENAME"
# Use a Heredoc to handle the multi-line string and variables
SCRIPT=$(cat <<EOF
package terminal.$DIRECTORY_NAME;
public class Main {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
EOF
)



if [ ! -f "$DIRECTORY_NAME" ]; then
    mkdir "$DIRECTORY_NAME"
    echo "Created folder: $DIRECTORY_NAME"

    
else
    echo "Folder already exists."
fi

if [ ! -d "$FULLPATH" ]; then 
     echo $SCRIPT > $FULLPATH
     cd  $FULLPATH
     javac $FILENAME
     java ${$FILENAME:0:4}
    fi
}
create_java



 

