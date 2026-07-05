from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL")

def update_sheet(data):
    client = OpenAI(
        base_url= base_url,
        api_key= api_key
    )

    query = client.chat.completions.create(
        model= model,
        messages= [{
            "role": "user", 
            "content": f"""You will receive expense data from a spreadsheet (CSV/XLSX), as a list of rows where some rows have a blank "category" field.
                For each row with a BLANK category, classify the expense based on its description into exactly one of these categories: Food, Transportation, Housing, Health, Leisure, Other.
                Return ONLY a JSON object mapping the row index (as a string) to the new category. Do not include rows that already have a category. Do not include any text outside the JSON.
                Example output format:
                {{"3": "Food", "7": "Transportation", "9": "Housing"}}
                Data:
                {data}
            """
            }
        ],
        temperature= 0.7
    )

    return query.choices[0].message.content

