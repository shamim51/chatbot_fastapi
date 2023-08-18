import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone

pinecone.init(api_key='952f1388-7340-4921-baba-5c97cdb95611', environment='us-west1-gcp-free')

index_name = "silkroad"

openai_api_key = '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'
os.environ['OPENAI_API_KEY'] = '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'

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
docsearch = Pinecone.from_existing_index(index_name, embeddings)

async def get_similiar_docs(query, k=2, score = False):
    if score:
        docs = docsearch.similarity_search_with_score(query, k=k)
    #plain_string = '\n'.join(doc.page_content for doc in docs)
        doc_contents = [doc.page_content for doc in docs]

    else:
        docs = docsearch.similarity_search(query, k=k)
        doc_contents = [doc.page_content for doc in docs]

    return doc_contents

# model_name = "text-davinci-003"
model_name = "gpt-3.5-turbo"
llm = OpenAI(model_name=model_name)
chain = load_qa_chain(llm, chain_type="stuff")

def genResponse(message):
    print("i am in getResponse function")
    #docs = docsearch.similarity_search(message)
    i=0
    while(i<2):
        i = i+1
        print(i)
    docs = f"This is a dummy response to your message: {message}"
    print(docs)
    #answer = chain.run(input_documents=docs, question=message)

    print(message)
    return {"answer": f"{docs}"}