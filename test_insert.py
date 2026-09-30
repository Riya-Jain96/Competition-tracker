import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from the .env file
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
# Use the publishable/anon key for standard operations
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Sample competition entry
sample_data = {
    "title": "Deloitte Strategy Challenge 2026",
    "sponsor_name": "Deloitte",
    "sponsor_type": "CORPORATE",
    "domain": "Strategy",
    "skills_addressed": "Financial Modeling, Market Sizing",
    "location_format": "ONLINE",
    "registration_fee": 0.00,
    "prize_pool": "$10,000",
    "min_team_size": 2,
    "max_team_size": 4,
    "registration_deadline": "2026-11-20T23:59:59Z",
    "direct_link": "https://deloitte.com/careers/challenge-2026"
}

# Insert into your database table
response = supabase.table("competitions").insert(sample_data).execute()

print("Successfully inserted row into Supabase!")
print(response.data)