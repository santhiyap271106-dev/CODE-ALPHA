import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
faq_questions = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening",
    "how are you",
    "who are you",
    "what can you do",
    "what is python",
    "what is ai",
    "what is machine learning",
    "what is data science",
    "what is deep learning",
    "what is nlp",
    "what is chatbot",
    "what is github",
    "what is tkinter",
    "what is internship",
    "what is codealpha",
    "how do i learn python",
    "thank you",
    "thanks"
]
faq_answers = [
    "Hello! How can I help you?",
    "Hi! Nice to meet you.",
    "Hey! How can I assist you?",
    "Good Morning! Have a great day.",
    "Good Evening! How can I help you?",
    "I am doing well. Thank you for asking.",
    "I am an FAQ Chatbot created using Python.",
    "I can answer frequently asked questions.",
    "Python is a popular programming language.",
    "AI stands for Artificial Intelligence.",
    "Machine Learning helps computers learn from data.",
    "Data Science extracts insights from data.",
    "Deep Learning is a subset of Machine Learning.",
    "NLP stands for Natural Language Processing.",
    "A chatbot is a software application that interacts with users.",
    "GitHub is a platform for storing and managing code.",
    "Tkinter is Python's built-in GUI library.",
    "An internship helps students gain practical experience.",
    "CodeAlpha provides internship opportunities and projects.",
    "You can learn Python through practice and projects.",
    "You're welcome!",
    "You're welcome!"
]
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)
def send_message():
    user_question = entry.get()
    if user_question.lower() == "bye":
        chat_box.insert(tk.END, "You: " + user_question + "\n")
        chat_box.insert(tk.END, "Bot: Goodbye!\n\n")
        entry.delete(0, tk.END)
        return
    user_vector = vectorizer.transform([user_question])
    similarity = cosine_similarity(
        user_vector,
        faq_vectors
    )
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]
    if best_score > 0.2:
        response = faq_answers[best_match_index]
    else:
        response = "Sorry, I don't understand your question."
    chat_box.insert(tk.END, "You: " + user_question + "\n")
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)
window = tk.Tk()
window.title("FAQ Chatbot")
window.geometry("600x500")
title = tk.Label(
    window,
    text="FAQ Chatbot",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)
chat_box = tk.Text(
    window,
    height=20,
    width=65
)
chat_box.pack()
entry = tk.Entry(
    window,
    width=50
)
entry.pack(pady=10)
send_button = tk.Button(
    window,
    text="Send",
    command=send_message
)
send_button.pack()
window.mainloop()