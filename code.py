import streamlit as st
import difflib
st.title("Mon mini chatbot IA")
st.write("Bonjour et bienvenue. Je suis SOLEA, ton mini chatbot.")
responses={
    "bonjour":"Salut!",
    "salut": "Salut! Comment ça va?",
    "comment ca va":"Je vais bien merci et toi?",
    "comment tu t'appelles":"Je m'appelle Sorelle",
    "quel temps fait-il?": "Je ne sais pas regarde la méteo",
    "au revoir":"A bientôt!",
    "yo":"yepp",
    "je vais bien":"D'accord.",
    "ca va et toi?":"Bien également. Merci!",
    "bien et toi?":"Bien aussi. Merci!",
    "ca va?":"très bien et toi?",
    "hi" : "hello",
    "ok" : "quoi de neuf ?",
    "d'accord" : "quoi de neuf ?"
}

user_input= st.text_input("Commencez une conversation ici:")


botresponses = {0}

if user_input:
    user_input = user_input.lower().strip()

    match = difflib.get_close_matches(user_input, responses.keys(), n=1, cutoff=0.3)

    if match :
        botresponses = responses[match[0]]
    else :
        botresponses = "Désolé, je ne sais pas répondre à ça"

st.markdown("### Réponse du bot : ")
st.success(botresponses)