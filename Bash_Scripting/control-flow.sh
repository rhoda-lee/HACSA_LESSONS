#!/bin/bash

# # LOGICAL AND

# age=17

# if [ "$age" -gt 18 ] && [ "$age" -lt 30 ]
# then
#     echo "Age is valid"
# else 
#     echo "Age is not valid"
# fi

# LOGICAL OR - Only one condition needs to be met


# age=60

# if [ "$age" -gt 18 ] || [ "$age" -lt 30 ]
# then
#     echo "Age is valid"
# else 
#     echo "Age is not valid"
# fi

# read age
# if [ "$age" -ge 18 ] && [ "$age" -le 30 ]
# then
#      echo "You get a fortune: "
#      fortune
# else 
#      echo "You get a talking cow: " 
#      rad sentence
#  fi

# LOGICAL NOT (!) - To reveal the truth value of a statement

# string="Hi ladies!"

# if [[ ! $string == "Goodbye!" ]]
# then
#     echo "String is not equal to goodbye"
# else
#     echo "String is equal to goodbye"
# fi

# Write a scripts that asks the user for a username, check if the name is admin if not print access denied if not access granted

# username=$1

# if [[ ! $username == "$USER" ]]
# then
#     echo "Access denied"
# else
#     echo "Access granted"
# fi

# WHILE LOOPS
# while [ condition ]
# do
#     [ command ]
#     [ command ]
#     [ command ]
# done


# number=1

# while [ $number -le 10000000000 ]
# do
#     echo "$number" 
#     number=$((number+1))
# done



while true
do
    echo "Enter a number or type 'q' to quit"
    read number

    if [[ "$number" == "q" ]]
    then
        break
    fi

    echo "You entered $number"
done

echo "Exiting the loop"
