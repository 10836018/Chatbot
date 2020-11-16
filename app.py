from flask import Flask, request
import Chatbot.chatbot as Chatbot

app = Flask(__name__)
chatter = Chatbot.Chatbot(w2v_model_path='model/word2vec.model')


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':

        # Post方法：raw
        # data = json.loads(request.get_data().decode('utf-8'))
        # question = data["question"]

        # Post方法：form-data
        question = request.values['question']

        print("get POST request data: ", question)

        ans = {
            'answer': chatter.waiting_loop(question)
        }

        print("answer is: ", ans)

        return ans

    elif request.method == 'GET':
        return 'GET OK!'


if __name__ == '__main__':
    app.run()
