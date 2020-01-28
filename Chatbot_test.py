#This chatbot section plays with echoing back user inputs.

print ("Hello, Welcome to Chatbox1")
#echo back name
name = input ("What is your name?")
bot_name = "! My name is Chatbox1, nice to meet you!"
print ("Ah, you are called " + name + bot_name)
#echo back favorite color
print ("This bot will echo your answer")
stuff_to_echo = input ("Tell me your favorite colour please!")
print ("You said: " + stuff_to_echo)
#connect multiple echos
m1 = "There are "
m2 = " apples in the kitchen. The "
m3 = " is in the living room eating shoes. This house is in "

echo1 = input ("Write a random number (example: 2):")
echo2 = input ("Write an animal type (example: cat):")
echo3 = input ("Write a country (example: France):")
echo1_1 = str(echo1)
message = m1 + echo1_1 + m2 + echo2 + m3 + echo3
print (message)

