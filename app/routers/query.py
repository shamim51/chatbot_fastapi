# app/routers/query.py
from fastapi import APIRouter, HTTPException
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

import pinecone


router = APIRouter()

#need to see later
openai_api_key = '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'

# Initialize Pinecone and OpenAI embeddings
pinecone.init(api_key='952f1388-7340-4921-baba-5c97cdb95611', environment='us-west1-gcp-free')

index_name = "sillkroad"
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
docsearch = Pinecone.from_existing_index(index_name, embeddings)


@router.post('/query')
async def query_documents(data: dict):
    query = data.get('query')

    if not query:
        raise HTTPException(status_code=400, detail="Missing 'query' parameter.")

    # Query the vector database
    docs = docsearch.similarity_search(query)
    return docs

async def query_documents(query):
    docs = docsearch.similarity_search(query)
    plain_string = '\n'.join(doc.page_content for doc in docs)

    return plain_string