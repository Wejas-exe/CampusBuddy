# 🎓 CampusBuddy — A Simple Rule-Based College Info Chatbot

CampusBuddy is a lightweight Python chatbot that answers frequently asked questions about a fictional college. It uses basic logic (no AI or machine learning) to simulate a helpful virtual assistant.

---

## 🚀 Features

- Greets and personalizes conversation using the user's name.
- Answers common FAQs about:
  - 🕘 College timings
  - 🎓 Available courses
  - 📍 Location
  - 📝 Admission process
  - 📞 Contact information
- Adds a **typing delay** using the `time` module for a realistic feel.
- Logs unknown questions into `unanswered_questions.txt` to help improve the bot later.
- Clean, modular code with clear comments.

---

## 🛠️ How to Run

1. Make sure you have Python installed (version 3.x).
2. Save the script as `chatbot.py`.
3. Open a terminal or command prompt in the script's folder.
4. Run:

```bash
python campusbuddy.py
```
---

## ✅ Requirements

- Python 3.x
- No external libraries needed — just the built-in `time` module

---

## ❓ Challenges Faced

- Creating responses that are both helpful and conversational
- Handling varied user phrasing (e.g., "timings", "hours", "open") using keyword checks
- Making the bot feel human without using any AI or NLP
- Ensuring scalability and code readability by modularizing logic

---

## 🧠 Future Improvements

- Add support for more questions
- Integrate NLP for flexible input handling
- Turn into a web or mobile chatbot with a UI
- Store logs in a database instead of a file
