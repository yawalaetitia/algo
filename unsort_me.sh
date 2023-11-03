function unsort_me (){
     array=($@)
     size=${#array[@]}
     for ((i=0; i<size; i++))
     do
       for((j=0; j<(($size-1)); j++))
       do
          if (( ${array[ $j]}<${array[$j+1]}))
          then
           tmp=${array[$j+1]}
           array[$j+1]=${array[$j]}
           array[$j]=$tmp 
          fi
       done  
    
    done
 echo ${array[@]}
}
unsort_me 1 3 5 7 65 43 0 -1