from extract import extract
from embed import embed
from store import store
from query import query
from answer import answer

def main():
    # Extract data from the web
    data_chunks = extract()
    # Embed the data
    embeddings = embed(data_chunks)
    # Store the embeddings
    store(embeddings)
    # Query the embeddings
    query_vector = embed(query)
    context = query(query_vector)
    # Answer the query
    generated_answer = answer(context)
    return generated_answer

if __name__ == "__main__":
    main()