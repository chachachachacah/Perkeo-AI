#Module
import pandas as pd
import requests
import json
#Directories
xlsx_file = "patient_input2.xlsx"
Output_file = "Output2.csv"
url = "http://127.0.0.1:11434/api/chat"
#Backend

def ai(xlsx_file, Output_file):
    xlsx = pd.read_excel(xlsx_file)
    xlsx.to_csv(Output_file, index=False)
    dv = xlsx.to_csv(index=False)
    
    ollama_input = {
        "model": "llama3.1:8b",
        "messages": [{"role": "system", "content": "ANalyze the data given dont give medical advice just list on whats there. Give data about patientunitstayid that number is 308316"},
                     {"role": "user", "content": dv}]
    }
    Ai_response = requests.post(url, json=ollama_input, stream=True)

    if Ai_response.status_code == 200:
        for line in Ai_response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_data = json.loads(line)
                    if "message" in json_data and "content" in json_data["message"]:
                        print(json_data["message"]["content"], end="")
                except json.JSONDecodeError:
                    print("UGANDA FORVERE")
    
#Frontend

door = ai(xlsx_file, Output_file)
