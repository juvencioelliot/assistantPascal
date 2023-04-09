import openai
from dotenv import load_dotenv
import os

class ChatGPT:
    """
    Cette classe implémente un assistant de chat utilisant l'API de OpenAI pour générer des réponses à partir
    du modèle de langage GPT-3.5.

    Attributes:
    ----------
    api_key : str
        Clé d'API utilisée pour authentifier l'assistant auprès de OpenAI.
    model : str, optional
        Nom du modèle de langage à utiliser pour générer des réponses. Par défaut, le modèle 'gpt-3.5-turbo'
        est utilisé.
    messages : list[dict]
        Liste des messages échangés entre l'utilisateur et l'assistant. Chaque message est représenté par un
        dictionnaire avec les clés 'role' et 'content', qui indiquent respectivement le rôle du message ('user'
        pour un message de l'utilisateur ou 'assistant' pour un message de l'assistant) et le contenu du message
        sous forme de texte.

    Methods:
    -------
    add_message(role: str, content: str) -> None:
        Ajoute un message à la liste des messages échangés entre l'utilisateur et l'assistant.

    get_response(user_message: str) -> str:
        Génère une réponse à partir du modèle de langage GPT-3.5 en utilisant les messages échangés précédemment
        entre l'utilisateur et l'assistant, et renvoie la réponse générée sous forme de texte.

    """

    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo") -> None:
        """
        Initialise un nouvel assistant de chat avec la clé d'API `api_key` et le modèle de langage `model`.
        """
        self.model = model
        self.api_key = api_key
        openai.api_key = self.api_key
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]

    def add_message(self, role: str, content: str) -> None:
        """
        Ajoute un message à la liste des messages échangés entre l'utilisateur et l'assistant.

        Parameters:
        ----------
        role : str
            Rôle du message ('user' pour un message de l'utilisateur ou 'assistant' pour un message de l'assistant).
        content : str
            Contenu du message sous forme de texte.

        Returns:
        -------
        None
        """
        self.messages.append({"role": role, "content": content})

    def get_response(self, user_message: str) -> str:
        """
        Génère une réponse à partir du modèle de langage GPT-3.5 en utilisant les messages échangés précédemment
        entre l'utilisateur et l'assistant, et renvoie la réponse générée sous forme de texte.

        Parameters:
        ----------
        user_message : str
            Message de l'utilisateur auquel l'assistant doit répondre.

        Returns:
        -------
        str
            Réponse générée par l'assistant sous forme de texte.
        """
        self.add_message("user", user_message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        assistant_message = response.choices[0].message['content']
        self.add_message("assistant", assistant_message)
        return assistant_message
