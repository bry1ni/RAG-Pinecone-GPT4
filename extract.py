from llama_parse import LlamaParse
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
import nest_asyncio; nest_asyncio.apply()
import os


os.environ["LLAMA_CLOUD_API_KEY"]

def extractData(pdf_path):
    markdown_document = LlamaParse(result_type="markdown").load_data(pdf_path)

    headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4")]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)
    md_header_splits = markdown_splitter.split_text(markdown_document[0].text)

    chunk_size = 256
    chunk_overlap = 50
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    splits = text_splitter.split_documents(md_header_splits)
    return splits