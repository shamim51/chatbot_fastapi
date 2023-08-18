def genResponse(message):
    print("i am in getResponse function")
    i=0
    while(i<2):
        i = i+1
        print(i)
    docs = f"This is a dummy response to your message: {message}"
    print(docs)
    print(message)
    return {"answer": f"{docs}"}