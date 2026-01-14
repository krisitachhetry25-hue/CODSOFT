
# CodSoft Internship - Task 1

import wikipedia
import pyjokes


dictionary = {
"python": "Python is a high-level, interpreted programming language.",
 "chatbot": "A chatbot is a program that simulates human conversation.",
 "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
 "machine learning": "Machine learning is a type of AI that allows systems to learn from data.",
"deep learning": "Deep learning is a subset of machine learning using neural networks.",
"algorithm": "An algorithm is a step-by-step procedure to solve a problem.",
"data": "Data is raw information that is processed to get meaningful insights.",
"neural network": "A neural network is a model inspired by the human brain.",
"computer vision": "Computer vision enables computers to understand images and videos.",
"nlp": "Natural Language Processing helps computers understand human language.",
"opencv": "OpenCV is a library used for image processing and computer vision tasks.",
"internet": "The internet is a global network of connected computers.",
"cloud computing": "Cloud computing delivers services over the internet.",
"database": "A database stores structured information digitally.",
"server": "A server provides data or services to other computers."

}

def chatbot():
    print(" ChatBot: Hello! I am your assistant tess but i am more like your friend.")
    print("you can Type 'help' to see what I can do or 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower()

        
        if user_input in ["exit","bye","see you","goodbye"]:
            print("Tess: Goodbye! Have a nice and warm day friend")
            break

        
        elif "hello" in user_input or "hi" in user_input:
            print(" Tess: Hello! How can I help you my friend?")

        
        elif "help" in user_input:
            print(""" Tess: yes of course, my friend I can help you with:
1. Wikipedia search → 'tell me about python'
2. Jokes → 'tell me a joke'
3. Word meaning → 'meaning of ai'
4. Basic chat → hello, how are you
5. Exit → exit
""")

        

        elif "how are you" in user_input:
            print("Tess: I'm doing great! Thanks for asking friend")

        elif "who created you" in user_input or "who made you" in user_input:
            print(" Tess: I was created by my friend kris, a curious developer learning Python and AI ")
        elif "are you human" in user_input:
            print(" Tess: I'm AI, but I have a big heart ")
        elif any(word in user_input for word in ["thanks", "thank you"]):
            print("Tess: You're welcome ")



        
        elif "crack a joke for me" in user_input:
            print(" Tess:here comes a hillarious one make sure you laugh" )
            print (pyjokes.get_joke())

        
        elif "tell me about" in user_input:
            topic = user_input.replace("tell me about", "").strip()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                print(" Tess:", summary)
            except:
                print(" Tess: Sorry, I couldn't find information on that topic.can you try another word for me")

        
        elif "meaning of" in user_input:
            word = user_input.replace("meaning of", "").strip()
            if word in dictionary:
                print(" Tess:", dictionary[word])
            else:
                print(" Tess: Sorry, I don't have the meaning of that word.")

        
        else:
            print(" Tess: I'm not sure how to respond to that. Try typing 'help'.")


chatbot()
