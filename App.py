import flask
import nltk

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from nltk.tokenize import sent_tokenize


app = flask.Flask(__name__)
app.config["DEBUG"] = True


def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    # Calculating the Sentiment Score
    sentiment_scores = sid_obj.polarity_scores(sentence)
    return sentiment_scores
    
    
@app.route('/', methods=['GET'])
def sentiments():
    text_2000= "That doesn't seem like it would be too hard to do, I replied. I've been hearing a lot about the power of a largely vegetarian diet. Just last week, Jenny told me about a study in Finland where it was found that thirty-eight percent of new vegetarians studied reported that they felt far less tired and much more alert after only seven months of this new way of life. I should try eating a salad with every meal. Looking at you, Julian, I might even make the salad the meal. Try it for about a month and judge the results for yourself You will feel phenomenal. Okay. If it's good enough for the sages, it's good enough for me. I promise you I will give it a shot. It doesn't sound like too much of a stretch, and anyway I'm getting pretty tired of firing up the barbeque every night. If I have sold you on the Ritual of Live Nourishment, I think you will love the fourth one. Your student is still holding his empty cup. The fourth ritual is known as the Ritual of Abundant Knowledge. It centers around the whole notion of lifelong learning and expanding your knowledge base for the good of yourself and all those around you. The old 'knowledge is power' idea? It involves far more than that, John. Knowledge is only potential power. For the power to be manifested, it must be applied. Most people know what they should do in any given situation, or in their lives for that matter. The problem is that they don't take daily, consistent action to apply the knowledge and realize their dreams. The Ritual of Abundant Knowledge is all."
    text = text_2000
    # Breaking Sentences
    textl = sent_tokenize(text)
    # Sentences in Lines
    eachInASeparateLine = "\n".join(sent_tokenize(text))
    # Creating new file
    for t in textl:
        res.append(sentiment_scores(t))
    return str(res)
    
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4200)
