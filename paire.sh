#!/bin/bash
function paire(){
    for i in $@
    do
      if(($i%2==0))
      then
        echo $i
        fi
    done
}
paire 1 2 4 8