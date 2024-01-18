import json
import requests
import gradio as gr

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/:id/ai/run/"
HEADERS = {"Authorization": f"Bearer (TOKEN HERE)"}

AI_NAME = "Replace your AI name here"
SYSTEM_PROMPT = "Replace your prompt here"


def run(model, inputs):
    input_data = {"messages": inputs}
    response = requests.post(f"{API_BASE_URL}{model}", headers=HEADERS, json=input_data)
    return response.json()

def save_to_memory(memory_data, user_question, ai_answer):
    conversation_entry = {"user_question": user_question, "ai_answer": ai_answer}
    memory_data["conversation_history"].append(conversation_entry)
    with open("memory.json", "w") as memory_file:
        json.dump(memory_data, memory_file, indent=2)

def cloudflare_ai_workers(question):
    with open("memory.json", "r") as memory_file:
        memory_data = json.load(memory_file)

    inputs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    if memory_data["conversation_history"]:
        conversation_context = "\n".join([
            f"AI: {entry['ai_answer']}" for entry in memory_data["conversation_history"]
        ])
        context_message = f"Recent Conversations:\n{conversation_context}\n\n"

        inputs.append({"role": "system", "content": context_message})

    output = run("@cf/meta/llama-2-7b-chat-int8", inputs)

    exported_json = output["result"].get("response", "")

    save_to_memory(memory_data, question, exported_json)

    if exported_json and f"Please respond as {AI_NAME}" not in exported_json:
        return exported_json
    else:
        return "It seems like Cloudflare AI did not generate a response. " \
               "If this persists, it might be a specific question that it's not familiar with. " \
               "Feel free to ask another question."

iface = gr.Interface(fn=cloudflare_ai_workers, inputs="text", outputs="text")

# If you want to make a public link, do `share=True` in `launch()`
iface.launch()