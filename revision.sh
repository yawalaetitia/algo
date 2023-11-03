#!/bin/bash

reverse_string() {
    local input="$1"
    local output=""
    local len=${#input}
    for ((i = len - 1; i >= 0; i--));
     do
        output="${output}${input:i:1}"
         if (( $output==$input))
        then
            echo "palindrome"
        else
            echo "not palindrome"
        fi
        done
}
   
reverse_string 