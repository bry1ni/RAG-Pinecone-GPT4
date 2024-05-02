import os
import openai
from langchain_openai import ChatOpenAI
from pinecone import Pinecone, ServerlessSpec
import numpy as np

os.environ["PINECONE_API_KEY"] = "20c7ce7f-e433-4ac0-a026-9ff7acb804c1"

data_to_upsert = list(zip(ids, embeddings, dict_lines))

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
defects_index_name = "defects"
defects_index = pc.Index(defects_index_name)

defects_index.upsert(vectors = data_to_upsert, show_progress=True)