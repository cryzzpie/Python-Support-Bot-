#support bot
jmeno = input ("what is your name?")
print("Hello" ,jmeno, "," "and welcome! my name is support bot and i will be helping you today!")
print("What can i help you with today" ,jmeno, "?" ",")
help = int(input("(1) I didnt recieve my pament yet) "))
if help ==1:
    print("Hmm was the payment sent later than 7 days ago?")
pomocdva = int(input("(1) Yes (2) No) "))
if pomocdva ==1:
    print("We will take a look at the payment and give you more information through the email you entered while registrating into our website.")
if pomocdva ==2:
    print("Please be patient and wait untill the payment is atleast 7 days old, if you will still be experiencing any type of problems just use our support bot again!  ")
    print(" Is there anything else i can help you with" ,jmeno, "?" )
pomoctri = int(input("(1) Yes (2) No) "))
if pomoctri ==1:
    print("Please contact us via email on adress czechclouduvsyn@twitchmanager.com, our humans will help you figure it out! ")
if pomoctri ==2:
    print("Thank you for contacting support bot" ,jmeno, "Feel free to contact us again using me or email czechclouduvsyn@twitchmanager.com! ")