# SaFar 🌍 – Smart Travel Itinerary Planner

**SaFar** is an AI-powered travel itinerary planner that helps you plan a detailed, personalized trip from your home to your dream destinations — including return via scenic routes, activity recommendations, budgets, travel modes, and local food suggestions.

Whether you're a solo explorer, a spiritual seeker, or a group adventurer — **SaFar** crafts your journey with context-aware storytelling using powerful LLMs.

## The Deployed Link: https://safar-ai-itinerarymaker.streamlit.app/

---
## ✨ Features

- 📍 **Multi-location itinerary planning**
- 💰 **Budget-based travel** (adjusts mode: train vs. flight)
- 🚅 **Travel preferences** (train, flight, etc.)
- 📅 **Day-wise planning** with:
  - Distances, timings, travel hacks
  - Entry fees, booking links, food suggestions
  - Return journey options
- 🌐 Powered by **LLaMA 3.3 70B via Groq API**
- 🖌️ Beautiful **blue-themed UI** with grid layout

---

## 🧠 Tech Stack

| Layer           | Tools / Frameworks                         |
|----------------|---------------------------------------------|
| Frontend       | [Streamlit](https://streamlit.io)           |
| Backend (LLM)  | [LangChain](https://www.langchain.com/), [Groq API](https://console.groq.com/) |
| Styling        | Custom CSS                                  |
| Secrets Mgmt   | `dotenv`, `.env`                            |
| Deployment     | [Streamlit Community Cloud](https://streamlit.io/cloud) |

---

## 📸 Screenshots

### 🔹 Home Page  
![Screenshot 1](assets/screenshot01.png)

### 🔹 Generate Itinerary View  
![Screenshot 2](assets/screenshots/screenshot02.png)

### 🔹 Itinerary Grid View  
![Screenshot 3](assets/screenshots/screenshot03.png)

---

## 🚀 How to Run Locally

1. **Clone the Repo**

```bash
git clone https://github.com/your-username/safar-app.git
cd safar-app
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Setup API Key**

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the App**

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
├── app.py                    # Main app launcher
├── prompts.py                # All prompt templates for LLM
├── theme.css                 # Styling
├── .env                      # Secret key (not pushed)
├── requirements.txt          # Dependencies
├── assets/
│   ├── screenshot 01.png     # UI screenshots for README
    ├── screenshot 02.png
    └── screenshot 03.png
```

---

## 🤖 Model Info

- 🔍 **Model**: `llama3-70b-8192`
- 💡 **LLM Host**: Groq
- 🔗 **LangChain** used for chain invocation & prompt templating

---

## 🧳 Sample Prompt

```
"Plan a round trip from Cuttack to Uttarakhand covering Kedarnath, Badrinath, Rishikesh and Varanasi. Budget is ₹20,000. Travel by train."
```

---

## 🛡️ Security

- ✅ `.env` is **excluded** from GitHub
- ✅ API keys are accessed via `os.getenv()`
- ✅ Safe deployment on Streamlit Cloud

---

## 🙋‍♂️ Author

- ✍️ Developed by: Saumya Subham Mishra
- 📧 Email: sm025663@gmail.com
- 🌐 [LinkedIn](https://www.linkedin.com/in/saumya-subham-mishra/)

---

## 🌟 Show Your Support

If you liked **SaFar**, please ⭐ star the repo and share with your travel-enthusiast friends!
