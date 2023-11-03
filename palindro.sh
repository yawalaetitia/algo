#!/bin/bash
read -p "entrer un mot" mot
 res=$(echo $mot | rev)

 if (("$res" = "$mot"))
 then
    echo "vrai"

 else
   echo "faux"
fi



