import openai
api_key = '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'
client = openai.OpenAI(api_key = api_key)

def ada_get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding