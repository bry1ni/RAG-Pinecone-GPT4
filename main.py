import os

from langchain_openai import ChatOpenAI
from extract import extractData
from query import query
from store import prepareData, storeData
from pinecone import Pinecone, ServerlessSpec
from answer import getAnswer

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

def createIndex(index_name, pineconeClient=pc):
    if index_name in pineconeClient.list_indexes():
        index = pineconeClient.Index(index_name)
    else:
        index = pineconeClient.create_index(
            name=index_name, 
            metric="cosine", 
            dimension=1536, # Dimension of the embeddings model
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ) 
  )
    return index

def main(pdf_path, index):
    # First, upsertion step
    splits = extractData(pdf_path)
    data_to_upsert = prepareData(splits)
    status = storeData(data_to_upsert, index)
    print(status)

    """# Second, Query step
    query_text = ["What is the MDRNet architecture?"]
    context = query(index, query_text)

    # Third, generate the response
    model = ChatOpenAI(openai_api_key = os.environ.get("OPENAI_API_KEY"), temperature=0, model="gpt-4")
    answer = getAnswer(context, query_text, model)
    print(answer)"""

if __name__ == "__main__":
    pdf_path = "Data/mdrNet.pdf"
    index_name = "pdf-test"
    index = createIndex(index_name)
    main(pdf_path, index)