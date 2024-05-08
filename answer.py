

def getAnswer(question, context, model):
    template = "You are an expert in deep learning and computer vision\
                Your role is to provide searchers with informations related to punlished research papers , \
                prioritizing the provided semantic search context retrieved from the paper. \
                Use the context directly if it addresses the researcher's question comprehensively. \
                Refer to your expertise to augment the explanation only if you think the context is insufficient.\n\
                Searcher Question: {question}\n\
                Search Context: {context}"

    augmented_template = template.format(question=question, context=context)

    answer = model.invoke(augmented_template)
    return answer.content