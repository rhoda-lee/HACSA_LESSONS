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

talking_cow=$(cowsay "Hii")

echo "Hello $name, you are $age years old! 
That is too old! Anyway, your password has been saved. 
And your fortune is: $my_fortune 
And the cow said $talking_cow"

read -p "Enter your firstname and lastname" firstname lastname
echo $firstname
echo $lastname