### COVID 19 CHATBOT
import random
import nltk
nltk.download('Stopwords')
import numpy as np
import string
import sklearn 
f=open('covid19.txt','r',errors='ignore')
raw=f.read()

raw=raw.lower()

nltk. download('punkt')

nltk.download('wordnet')

sent_tokens=nltk.sent_tokenize(raw)

word_tokens=nltk.word_tokenize(raw)


### **Preprocessing**

lemmer=nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]

remove_punct_dict=dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



### **Greet**Response** 

GREETING_INPUTS=("hello","hi","greetings","sup","what's up","hey","namaste")
GREETING_RESPONSES=["hii","hey","*nods*","hi there","hello","I am glad! You are talking to me","namaste"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
     robo_response=''
     sent_tokens.append(user_response)
     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize,stop_words = set(stopwords.words('english') ) )
     tfidf= TfidfVec.fit_transform(sent_tokens)
     vals=cosine_similarity(tfidf[-1],tfidf)
     idx=vals.argsort()[0][-2]
     flat=vals.flatten()
     flat.sort() 
     req_tfidf=flat[-2]
     if (req_tfidf==0):
         robo_response=robo_response+"I am sorry! I don't understand you"
         return robo_response
     else:
         robo_response=robo_response+sent_tokens[idx]
         return robo_response

flag = True
print("Chatbot: My name is CovidBot ! I can help you with Information about covid19. If you want to quit, just type bye anytime!!")
while (flag==True):
    user_response= input()
    user_response=user_response.lower()
    if (user_response!='bye'):
        if (user_response=='thanks' or user_response=='thank you'):
            flag=False
            print("CovidBot: You're welcome")
        else:
            if (greeting(user_response)!=None):
                print("CovidBot: "+greeting(user_response))
            else:
                print("CovidBot: ",end="")
                print(response (user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("CovidBot: Thanks for Talking , wear mask and maintain social distancing.")

