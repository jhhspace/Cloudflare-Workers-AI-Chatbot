# Cloudflare Workers AI Chatbot

#### Note: Cloudflare AI workers is currently in Beta, if things doesn't work out as expected, that's why.
#### Note: I'm currently studying AI and Python. If there's any place I can improve, feel free to tell me!

## What to prepare?
 - Create an account with [Cloudflare](https://dash.cloudflare.com/)
 - After creation, head over to AI > Workers AI. [Image](https://i.jhh.moe/3c79fc0d7e26.png)
 - Click on **Get API Token**. [Image](https://i.jhh.moe/470abe65d255.png)
 - Follow the instruction to create the API Token. Make sure to save it as it won't be showed again. [Image](https://i.jhh.moe/8e37b99eabd2.png)
 - At the link bar, copy your account ID. [Image](https://i.jhh.moe/b2653d4342d4.png)
 - In `main.py` __Line 7__, replace `:id` to your account ID
 - In `main.py` __Line 8__, replace `(TOKEN HERE)` [including the bracket] to your API Token
 - Change `AI_NAME` and `SYSTEM_PROMPT` to your own AI name and System Prompt

## Installation

This code was tested using Python 3.10.11. It might work on other versions (NOT TESTED)
 - Install [Python](https://www.python.org/downloads/)
 - Run `pip install -r requirements.txt` to install all the dependencies

## How to use?
 - Run `python main.py` to start chatting!

## Extra Notes:
 - Replace `memory.json` to `[]` to reset the memory! Make sure to restart gradio if you delete the memory.
 - This is how it should look like after you remove the memory: [Image](https://i.jhh.moe/67307ec8fde9.png)
 - Cloudflare allows 100K requests PER DAY. You can never run out of requests unless you share it to a lot of people.
 - Refer to the last 2nd line of `main.py` to see how to share it to the public. Gradio will create a public link for you. By default, it'll only be private link.
