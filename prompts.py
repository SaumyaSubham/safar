from langchain.prompts import PromptTemplate

def get_prompt_template():
    return PromptTemplate(
        input_variables=["home_location", "destination", "places_to_visit", "return_via", "budget", "travel_mode", "stay_days"],
        template="""
You are an expert travel planner and guide. 
Generate a day-wise detailed travel itinerary from {home_location} to {destination}, covering:
- The tourist spots: {places_to_visit}
- Returning via {return_via}
- Consider budget: ₹{budget}
- Travel preference: {travel_mode}
- The user wants to spend {stay_days} days at the destination (excluding travel time)

🎯 Format:
- Use engaging storytelling (second person)
- Describe how the user will travel from one place to another (auto, cab, walk) with approx. distance
- Mention time to spend, entry fees, best time to visit
- Give food recommendations near those places (with dish names)
- Give tips or local hacks or local activities like rafting, bunjee jumping etc. if available 
- DO NOT use unnecessary "**" or "--------"
- Structure each day with **h2 headers** (`## Day 1: Haridwar...`) and **paragraphs**, NOT just bullets

🎒 Example of what a good section looks like:
> Start your morning with a 1-hour cab ride (₹500) or you can take a auto ride (₹200) from Haridwar Railway Station to Har Ki Pauri. This sacred ghat on the Ganges is just 3 km from the station and is known for its vibrant Ganga Aarti at sunrise. You can explore the market nearby and try hot jalebis from the famous Mohan Mishthan Bhandar. Around 10 AM, take a short auto ride to Mansa Devi Temple...

Now start planning the trip in this detailed, friendly, yet informative style.
"""
)
