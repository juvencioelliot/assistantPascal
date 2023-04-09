import openai
from dotenv import load_dotenv
import os
from src.gpt import ChatGPT
from src.voiceRecon import ReconnaissanceVocale

if __name__ == "__main__":

    recon = ReconnaissanceVocale()

    load_dotenv()
    api_key = os.getenv("CHATGPT_API_KEY")
    chat_gpt = ChatGPT(api_key)

    # user_message = "where is ccnb dieppe located?"

    user_message = recon.reconnaissance_vocale();
    response = chat_gpt.get_response(user_message)
    print(response)
    recon.engine.say(response)
    recon.engine.runAndWait()

    # user_message = "is that in canada?"
    # response = chat_gpt.get_response(user_message)
    # print(response)




