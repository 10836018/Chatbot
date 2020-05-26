import Chatbot.console as console
import Chatbot.chatbot as Chatbot

c = console.Console(model_path='model/word2vec.model')
while True:
    speech = input('Input a sentence:')
    res ,path = c.rule_match(speech)
    c.write_output(speech, res, path)

#chatter = Chatbot.Chatbot()
#chatter.waiting_loop()