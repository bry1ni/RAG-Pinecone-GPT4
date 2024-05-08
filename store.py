import numpy as np
from embed import embedData

def prepareData(splits):
    pages_content = []
    metadata = []
    ids = []
    for index in range(len(splits)):
        ids.append(str(index))  # Convert index to string if you require the ID in string format
        pages_content.append(splits[index].page_content)
        metadata_head = list(splits[index].metadata.values())

        metadata.append({'Headers' : metadata_head, 
                        'Content': metadata_head + [splits[index].page_content]})  # Convert splits[index].page_content to a list
    
    embeddings = embedData(pages_content)
    data_to_upsert = zip(ids, embeddings, metadata)
    return  data_to_upsert

def storeData(data2upsert, index):
    index.upsert(vectors = data2upsert, show_progress=True)
    return index.describe_index_stats()