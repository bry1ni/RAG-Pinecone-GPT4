from llama_parse import LlamaParse
from langchain_text_splitters import RecursiveCharacterTextSplitter
import nest_asyncio; nest_asyncio.apply()
import os


os.environ["LLAMA_CLOUD_API_KEY"] = "llx-H6JEjz8kAgLPd0z7oyMkiCRqZr1kXVvOz8tqkS5NgzVhCnhq"

def extract_data(pdf_path):
    documents = LlamaParse(result_type="text").load_data(pdf_path)

    chunk_size = 512
    chunk_overlap = 100
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    splits = text_splitter.split_documents(documents[0].text)
    return splits

pdf_path = "Data/DSML.pdf"
splits = extract_data(pdf_path)
print(splits[10:20])