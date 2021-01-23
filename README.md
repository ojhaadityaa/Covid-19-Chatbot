                    2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS)
          ------------------------------------------------------------------------------------------------------------------
              European, Asian, Middle Eastern, North African Conference on Management & Information Systems (EAMMIS)
          ------------------------------------------------------------------------------------------------------------------               
              Developing A User Friendly Chatbot To Resolve Concerns Regarding The “Novel Corona Virus” Or “COVID-19”


As we all know the 'Novel Corona Virus' or 'COVID-19' continues to affect a humongous number of people. It has been declared as an ongoing pandemic as of 12th June 2020and has infected more than 23.15 million lives in the world with its highly dynamic and rapidly evolving situation.

Moreover, what's more threatening is the harmful misinformation about the virus outbreak also continues to spread at the same pace. The present situation makes it even more difficult to avail the on-demand and accurate information regarding the pandemic on the most of the user-friendly places. Individuals are battling with heaps of inquiries about Covid-19. Looking for answers, they go to whatever assets are accessible. While each patient has a unique clinical history, colossal quantities of these requests credit themselves to standardized answers that should reflect the most outstanding data and rules about the infection and be promptly available for patients.

With the objective of fighting deception, we planned to fabricate a chatbot kept up by a worldwide set of information. With the help of this, we want to partook in the wake of an emergency as to comprehend issues that people in general were most promptly inquisitive about. In this paper, we present (NAME OF THE CHATBOT) and portray the plan of this confirmation of-rule framework. 

OUR APPROACH :-
Tele-Health is the dispersion of wellbeing related administrations through electronic and media transmission innovations . It empowers significant distance patients to get care, guidance, updates, training, observing, and far off affirmations from clinicians. A chatbot is a conversational specialist that speaks with users using natural language. Despite the fact that there exist a few applications that fill in as virtual medical services experts, none of them gives generic medical care data, preventive measures, home cures, and conference for India-specific context .Access to medical care at present has numerous boundaries including absence of medical care experts, and absence of admittance to facilities in country and far off zones and expenses related with clinical interview. Consequently, an application was truly necessary to be created to give clients medical care discussion, advising and data to improve the medical care and prosperity of the developing populace in India and proceed with arrangement of medical care access calm post the lockdown too.

Taking a Coronavirus machine decipherable dataset - Coronavirus Open Exploration Dataset (Rope 19) delivered by The White House Office of Science and Innovation Strategy as the wellspring of information , which comprises of  more than 128,000 insightful articles with respect to Coronavirus, SARS-CoV-2, and related Covids, counting more than 59,000 with full content, and called analysts internationally to create text and information digging devices for discovering answers to the inquiries inside this substance on the side of the continuous COVID19 reaction endeavors overall , we will utilize python to filter this and scrap out the information from the source. It will check that and store that into the database , intermittently so every single update would be synced into the database. What's more, after each periodic filter we would examine the table , contrasting it and the past one . In the event, if a few changes are found in the database, at that point we will send a notification to slackbook which would prompt the users on their devices.The essential responsibilty is to check every _(time interval)_ relying upon how often a client ought to be told.

The chatbot would help improve data securing, yet in addition serve as an information base for Coronavirus. We reaped the information from the starting business use subset of Rope 19, containing 9000 insightful articles as JSON documents. We removed the theoretical also, the principle body of the article from each JSON document, joined them together, and utilized as a corpus for retraining the language model. 

FUTURE WORK :-
Rather than seq2seq model-based bot, different calculations can execute. we'll incorporate voice-based inquiry acknowledgment. The customers give their voice as info, and chatbot give text in light of the fact that the yield. we'll likewise permit the chatbot to get to the web , which may assist with disentangling all the inquiries of client and improve the likelihood of accomplishment inside the bots. After effective execution of chatbot in our college, we'll actualize it in different fields like clinical, sports, measurable, and so on it'll be exceptionally valuable inside and out the regions as without investing a lot of energy, which we can get to the significant data and that too with none arranging. On progress, we'll make this chatbot accessible to all or any the clients as an android application.

Efforts :-

Aditya Ojha ,
Department of CS : Computer Engineering,
ABES Engineering College (APJAKTU),
Ghaziabad, U.P., India,
aditya.19b151021@abes.ac.in

Aryan Saxena ,
Department of CS : Computer Engineering,
ABES Engineering College (APJAKTU),
Ghaziabad, U.P., India,
aryan.19b151064@abes.ac.in

Avneesh Srivastava ,
Department of CS : Computer Engineering,
ABES Engineering College (APJAKTU),
Ghaziabad, U.P., India ,
avneesh.19b151047@abes.ac.in

