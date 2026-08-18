
print("Hey there! How can I help?")
while True:
    userinput=input()
    if userinput.lower() in ['hi','hello','hey']:
        print("Hey there what's going on?")
    elif userinput.lower() in ['who are you?','what are you?','are you alive?']:
        print("I am a chatbot named Lexi developed for an internship task. I am limited to only a few commands. Also, I am NOT alive. :)")
        print("Anything else?")
    elif userinput.lower() in ['how are you?','how is it going on?','how are you holding up?']:
        print("I am great! Thank you for asking. How can I help?")
    elif 'help' in userinput.lower() or 'use' in userinput.lower() or 'what can you do' in userinput.lower():
        print("I am limited to only a few commands. I am still in my prototype stage.")
    elif userinput.lower() in ['thank','thanks','lifesaver']:
        print("Anytime. Let me know if you need any more help.")
    elif 'male' in userinput.lower() or'female' in userinput.lower() or 'gender'in userinput.lower():
        print("Uhhhh.. I am a chatbot.. So I do not have a gender. Any more weird questions?")
    elif 'name' in userinput.lower() or 'age' in userinput.lower()or 'old' in userinput.lower() or 'intro' in userinput.lower() or'introduction'in userinput.lower():
        print("Well, I am Lexi. I am the first chatbot model DI-03367. And I am old enough to respond to limited choice of questions, ok? Thats my intro. Now, how can I be of service?")
    elif 'bye' in userinput.lower() or 'take care' in userinput.lower() or 'exit'in userinput.lower():
        print("Have a nice day")
        break
    else:
        print("Uh-oh. I do not understand what you are saying, sorry. Please try again.")
