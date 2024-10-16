#Used to read user input from the terminal
#read command

echo "What is your name? "
read name

echo "How old are you? "
read age

echo "What is your password?"
read -sp password: 


name="Dede"

my_fortune=$(fortune)
echo "Hello $name, you are $age years old! 
That is too old! Anyway, your password has been saved. And your fortune is: $my_fortune"