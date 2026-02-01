print("HOSPITAL LOADED FROM:", __file__)
#Module
import pandas as pd
import requests
import json
#Directories
url = "http://127.0.0.1:11434/api/chat"
xlsx = "patient_input.xlsx"
#Backend
def converter_excel(input_file):
    output_file = "file.csv"
    df = pd.read_excel(input_file)
    df.to_csv(output_file, index=False)
    return output_file







def ai(csv_file_path, user_prompt):
    csv_text = open(csv_file_path, "r", encoding="utf-8").read()

    response_text = ""

    packed_prompt = f"""
    Dont give medical advice
    Only Output data
    No explanations

    {user_prompt}

    {csv_text}
    """



    ollama_input = {
        "model": "llama3.1:8b",
        "messages": [{"role": "user", "content": packed_prompt}],
    }

    Ai_response = requests.post(url, json=ollama_input, stream=True)

    if Ai_response.status_code == 200:
        for line in Ai_response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_data = json.loads(line)
                    if "message" in json_data and "content" in json_data["message"]:
                        response_text += json_data["message"]["content"]
                except json.JSONDecodeError:
                    print("UGANDA FORVERE")
        return response_text
