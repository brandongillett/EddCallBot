# EddCallBot
This EDD call bot uses Python with Twilio to call the EDD hundereds of times an hour and calling you once the bot gets ahold of them!  

For this you will have to create a Twilio account and pay a standard fee of $20 to use the phone line.  
This is a short instruction list of what you will have to do in order to get Twilio and This Python script setup.  

1 : Sign-Up for Twilio at https://www.twilio.com/try-twilio  
2 : Fund your account and add a phone number  
3 : Click the 3 dots on the left hand tool bar and find TwiMl Bins  
4 : Create a new bin and name it whatever you like, then copy the code from the CallXml.xml file and paste it into the TwiMl textbox  
5 : Copy the URL generated for you and paste into callbot.py where it says XML_URL between the quotes  
6 : Press the home icon in twilio and locate Account SID and Auth Token and paste those in callbot.py also between the quotes.  
7 : Click the # on twilio and it will take you to phone numbers and find the phone number that you have purchased, and in callbot.py you are going to type that number where it says FROM out (with +1 before it) without any other characters  
8 : Type your phone number in the where it says NUMBER (also including the +1 before it) without any characters  
9 : Where it says BOT_NUM enter how many bots you would like to call every cycle which is approximately 3 Minutes and 30 Seconds (Recomended 20 For Best Effect)  
10 : Lastly Run the callbot.py script in the terminal using "python3 callbot.py" Python3 and Pip are required for this  
