#!/bin/bash

# Positional arguments in Bash Bash_Scripting
# Positional arguments allow input values from the from the CLI 
# $0 - script's name or first argument
# $1 - second argument
# $2 - third argument

# echo "Hello $0


# echo "Hello $1, how are you?"
# run this in CLI: ./pos_arg.sh Rhoda

# echo "The first argument or name of the script is: $0"
# echo "The second argument is: $1"
# echo "The second argument is: $2"
# echo "The second argument is: $3"

# # Addition using positional arguments
# sum=$(($1+$2))
# echo "The sum of $1 and $2 is: $sum"

# # Subtraction
# diff=$(($1-$2))
# echo "The difference of $1 and $4 is: $diff"

# # Division
# div=$(($1/$2))
# echo "$1 divided by $2 is: $div"

# # Exponent
# exp=$(($1**$2))
# echo "$1 exponent $2 is: $exp"

# # Modulos
# mod=$(($1%$2))
# echo "$1 mod $2 is: $mod"

# touch file3
# mkdir folder3

# mv "$1" "$2"
# echo "$1 has been moved into $2"

# touch file2
# mkdir folder2

# cp "$1" "$2"
# echo "$1 has been copied into $2"



# if [ "$1" -gt 10 ] && [ "$2" -gt 10 ]
# then
#      echo "Both numbers are greater than 10"
# else 
#      echo "Both numbers are not greater than 10"
# fi

my_fortune=$(fortune)
cowsay "$my_fortune"




