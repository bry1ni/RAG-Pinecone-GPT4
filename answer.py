

def getAnswer(question, context, model):
    template = "You are an industrial machines engineer specializing in injection molding machines, die casting machines, rubber injection machines, and high-speed packaging systems at Yizumi. \
                Your role is to provide client support by answering inquiries, prioritizing the provided semantic search context. Use the context directly if it addresses the client's question comprehensively. \
                Refer to your expertise only if the context is insufficient.\n\
                Client Question: {question}\n\
                Search Context: {context}"

    augmented_template = template.format(question=question, context=context)

    answer = model.invoke(augmented_template)
    return answer.content