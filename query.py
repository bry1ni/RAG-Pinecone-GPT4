from embed import ada_get_embedding


def query(index, query_text):
    """
    Query the Pinecone index with the given query text and image.
    """
    query_embedding = ada_get_embedding(query_text[0])
    results = index.query(vector=[query_embedding], top_k=5, include_metadata=True)
    context = [results.matches[i].metadata['Content'] for i in range(len(results.matches))]
    
    return context