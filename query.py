pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
defects_index_name = "manual-1-metadata"
defects_index = pc.Index(defects_index_name)

query_text = ['What are the procedures for daily electrical and mechanical maintenance of the machine?']
query_embedding = ada_get_embedding(query_text[0])
results = defects_index.query(vector = [query_embedding], top_k=5, include_metadata=True)
topk_results = [f"Headers:{results.matches[i].metadata['Headers']} / Content: {results.matches[i].metadata['Content']}" for i in range(len(results.matches))]

