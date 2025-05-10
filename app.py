import streamlit as st
from prompts import get_prompt_template
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# --- Page Config ---
st.set_page_config(page_title="SaFar | AI Travel Planner", page_icon="🌍", layout="centered")

# --- Inject CSS ---
with open("theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #3B82F6;'> SaFar 🌍</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Your Smart Travel Companion</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Plan a personalized journey from your home to your destination, including scenic stopovers on your return!</p>", unsafe_allow_html=True)

# --- Input Fields ---
st.markdown("### 📌 Let's Plan Your Travel Itinerary")

home_location = st.text_input("🏠 Where are you starting from?", placeholder="e.g., Cuttack, Odisha")
destination = st.text_input("🗺️ What's your main destination?", placeholder="e.g., Uttarakhand")
places_to_visit = st.text_area("📍What places do you want to visit?", placeholder="e.g., Kedarnath, Badrinath, Rishikesh, Haridwar")
stay_days = st.number_input("🕒 How many full days do you want to spend at the destination?", min_value=1, value=3)
return_via = st.text_input("🔄 Any stop on return journey?", placeholder="e.g., Varanasi")
budget = st.number_input("💰 What's your budget for the trip (in INR)?", min_value=1000, value=20000, step=1000)
travel_mode = st.selectbox("🚄 Preferred mode of travel?", ["Train", "Flight", "Bus", "Cab", "Mixed"])

# --- LLM Config ---
llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("groq_api_key"),
    model_name="llama3-70b-8192"
)
prompt_template = get_prompt_template()
chain = prompt_template | llm

# --- Generate Itinerary ---
if st.button("🌍 Generate My Itinerary"):
    if not all([home_location, destination, places_to_visit, budget, travel_mode, stay_days]):
        st.warning("Please fill all required fields before generating the itinerary.")
    else:
        with st.spinner("Crafting your personalized itinerary..."):
            response = chain.invoke({
                "home_location": home_location,
                "destination": destination,
                "places_to_visit": places_to_visit,
                "return_via": return_via or "None",
                "budget": budget,
                "travel_mode": travel_mode,
                "stay_days": stay_days
            })

            st.markdown("## ✈️ Your Travel Itinerary")

            st.markdown("""
                <style>
                    .grid-container {
                        display: grid;
                        grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
                        gap: 2rem;
                        margin-top: 2rem;
                    }
                    .grid-item {
                        background-color: #1f2937;
                        padding: 1.5rem;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(59, 130, 246, 0.2);
                        color: #f9fafb;
                    }
                    .grid-item h3 {
                        color: #3B82F6;
                    }
                </style>
            """, unsafe_allow_html=True)

            cleaned_response = response.content.replace("**", "").replace("—", "").replace("---", "").replace("\n\n", "\n")

            days = cleaned_response.split("## ")
            for day in days:
                if day.strip():
                    st.markdown(f"""
                        <div style="background-color:#1f2937; padding: 1.5rem; border-radius: 0.75rem; 
                                    margin-bottom: 1.5rem; box-shadow: 0 4px 14px rgba(0,0,0,0.3);">
                            <h3 style="color:#3b82f6;">{day.splitlines()[0]}</h3>
                            <p style="color:#e5e7eb; line-height:1.8;">{"<br>".join(day.splitlines()[1:])}</p>
                        </div>
                    """, unsafe_allow_html=True)
