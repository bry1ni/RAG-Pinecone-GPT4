from langchain_openai import ChatOpenAI

api_key = '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'
gpt_model = ChatOpenAI(openai_api_key = api_key, temperature=0, model="gpt-4")

template =  " You are a data science & machine learning expert, your task is to assist students,\
            on understanding the concepts and answer their questions. \
            you would have the context resulted from a semantic search, rely on that to answer them.\
            question: {question}\
            context: {context}."

def get_answer(query, topk_results):
    augmented_template = template.format(question=query[0], context=topk_results)
    answer = gpt_model.invoke(augmented_template)
    return answer