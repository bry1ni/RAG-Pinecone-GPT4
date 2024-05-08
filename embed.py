import os
import openai

client = openai.OpenAI(api_key = os.environ["OPENAI_API_KEY"])

def ada_get_embedding(text, model="text-embedding-ada-002", client=client):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def embedData(documents, client=client):
    embeddings = []
    for document in documents:
        embeddings.append(ada_get_embedding(document))
    return embeddings