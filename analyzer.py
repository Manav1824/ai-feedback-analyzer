import os
from google import genai
from google.genai import types

def analyze_feedback():
    # 1. Initialize the Gemini Client
    # The client automatically looks for the GEMINI_API_KEY environment variable
    try:
        client = genai.Client()
    except Exception as e:
        print("Error: Could not initialize client. Did you set your GEMINI_API_KEY?")
        return

    # 2. Simulated input data (In a real project, this would be a CSV or database read)
    feedbacks = [
        "The new dashboard is incredibly fast, but I can't find the export button.",
        "Support took 3 days to reply to my billing issue. Completely unacceptable.",
        "I love the automated reporting features! It saved my team 10 hours this week."
    ]

    print(f"Analyzing {len(feedbacks)} customer reviews using Gemini...")

    # 3. Structure the prompt and system instructions
    system_instruction = (
        "You are an AI data analyst. Extract insights from the customer feedback provided. "
        "Return a raw JSON array where each object contains: "
        "'summary' (a 1-sentence recap), 'sentiment' (Positive/Negative/Neutral), "
        "and 'requires_support_ticket' (boolean)."
    )
    
    prompt = f"Customer Feedback Data:\n{feedbacks}"

    # 4. Call the API and enforce JSON output
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json"
        )
    )

    # 5. Output the structured JSON response
    print("\n--- AI Analysis Results ---")
    print(response.text)

if __name__ == '__main__':
    analyze_feedback()