from flask import Flask, jsonify,request,render_template
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)


__data = None
__listdata = None


@app.route("/")
def index():
    global __data
    global __listdata
    with open("./artifacts/organ_wikipedia.txt",'r') as f:
        __data = f.readlines()
    __listdata = []
    for line in __data:
        __listdata.append(line)
    print(__listdata)
    return render_template("app.html")

@app.route("/get_response",methods=['GET','POST'])
def get_response():
    print("entered")
    user_response = request.form['user_text']
    query = user_response.lower()
    if query in ["hi", "hey", "is anyone there?", "hello", "hay", "hey you...","aare bhaiyaa"]:
        bot_response = "Hey there wassup!!!"
    elif query not in ['bye', 'good bye', 'take care']:
        bot_response = get_bot_response(query)
        __listdata.remove(query)
    else:
        bot_response = "See You Again"
    print(bot_response)
    response = jsonify({
            'bot_response':bot_response
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

def get_bot_response(input):
    global __data
    global __listdata
    __listdata.append(input)
    vectorizer = TfidfVectorizer()
    sentences_vectors = vectorizer.fit_transform(__listdata)
    vector_values = cosine_similarity(sentences_vectors[-1], sentences_vectors)
    answer = __listdata[vector_values.argsort()[0][-2]]
    input_check = vector_values.flatten()
    input_check.sort()
    
    if input_check[-2] == 0:
        return "Any other related chat?"
    else: 
        return answer


if __name__ =="__main__":
    app.run()
