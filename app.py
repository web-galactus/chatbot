from flask import Flask,request,render_template
app = Flask(__name__)


 
# print("hi i am mb")
# print("ask about artificial intelligence\n")

 
def mb(user_input):
         
            user = user_input.lower()

            h = ["hello", "hey", "hi"]
            if user in h:
                return("hi ! what do you want to know about artificial intelligence \n")

            elif "what is artificial intelligence" in user or "what is ai" in user:
                 return("ai is when computers or machines are made to think and solve problems like humans.\n")

            elif "why is ai important" in user:
                 return("because it helps in automating tasks, saving time, and solving problems faster.\n")

            elif "is ai the same as robots" in user:
              return("no. robots are machines; ai is the brain that can control them.\n")

            elif "goal" in user:
                return("to create machines that can learn, reason, and make decisions like humans.\n")

            elif "invented" in user:
                return("the term artificial intelligence was first introduced by john mccarthy in 1956.\n")

            elif "think like human" in user:
                return("not exactly. it can mimic human thinking but doesn’t have emotions or full understanding.\n")

            elif "about coding" in user:
                 return("no, it involves coding, math, data, and logical problem-solving.\n")

            elif "types" in user:
                 return("weak ai, strong ai, and super ai.\n")

            elif "emotions" in user:
                print("no, ai doesn’t feel emotions. it only processes data.\n")

            elif "machine learning" in user:
                 return("machine learning is a part of ai that allows machines to learn from data.\n")

            elif "daily life" in user or "use of ai" in user:
                return("google search, youtube recommendations, face unlock, alexa/siri, maps, etc.\n")

            elif "google maps" in user or "google" in user:
                 return("it analyzes traffic data to suggest the fastest routes.for google maps\n")

            elif "self driving" in user:
                return("self-driving cars use ai to detect roads, traffic, and obstacles.\n")

            elif "healthcare" in user:
                 return("ai helps in detecting diseases, predicting risks, and supporting doctors in diagnosis.\n")

            elif "education" in user:
                 return("ai can personalize learning, recommend study materials, and even act as a tutor.\n")

            elif "gaming" in user:
                 return("ai makes games smarter by controlling enemies and creating realistic environments.\n")

            elif "future of ai" in user:
                return("ai may improve healthcare, transport, and education, but it also raises job and ethics issues.\n")

            elif "ai dangerous" in user:
                 return("ai is not dangerous by itself, but misuse by humans can be harmful.\n")

            elif "jobs" in user or "job" in user:
                return("ai may replace some repetitive jobs, but it also creates new technology-based jobs.\n")

            elif "programming languages" in user:
                 return("python, r, java, and c++ are common programming languages for ai.\n")

            elif "difference between ai and ml" in user:
                return("ai is the big concept of machines acting smart; ml is a part of ai where machines learn from data.\n")

            elif "movies" in user or "jarvis" in user:
                 return("yes, jarvis in iron man is a fictional example of ai. real ai is still not that advanced.\n")

            elif "data in ai" in user:
                 return("data is the fuel of ai. ai learns patterns and makes predictions from data.\n")

            elif "deep learning" in user:
               return("deep learning is a branch of machine learning using neural networks.\n")

            elif "neural network" in user:
                 return("a neural network is a model inspired by the human brain that processes information in layers.\n")

            elif "speech recognition" in user:
                 return("ai converts spoken words into text using natural language processing.\n")

            elif "chatbot" in user:
                 return("a chatbot is an ai program that can talk to humans through text or voice.\n")

            elif "ai in banking" in user:
                 return("ai is used in fraud detection, customer service, and financial advice.\n")

            elif "ai in agriculture" in user:
                 return("ai helps farmers by predicting weather, monitoring crops, and automating tasks.\n")

            elif "ai in business" in user:
                 return("ai is used for customer support, sales prediction, and decision making.\n")

            elif "ai in social media" in user:
                 return("ai recommends friends, filters spam, and suggests content.\n")

            elif "ai in recommendation" in user:
                 return("ai suggests movies, songs, or products based on user behavior.\n")

            elif "natural language processing" in user or "nlp" in user:
                 return("nlp is a field of ai that helps machines understand human language.\n")

            elif "ai vs human brain" in user:
                 return("ai is faster in calculations but lacks creativity, emotions, and common sense like humans.\n")

            elif "ai limitations" in user:
                 return("ai depends on data, lacks emotions, and can’t truly understand context.\n")

            elif "ai bias" in user or "bias" in user:
                 return("if ai is trained on biased data, it can produce unfair results.\n")

            elif "ai history" in user or "history" in user:
                url="https://en.wikipedia.org/wiki/Artificial_intelligence"
                return(f"""the concept of ai started in the 1950s with john mccarthy and alan turing.visit this link for more information {url}\n""")

            elif "alan turing" in user:
                 return("alan turing is known as the father of computer science and ai.\n")

            elif "turing test" in user:
                 return("a test to check if a machine can imitate human intelligence.\n")

            elif "ai in military" in user or "military" in user:
                 return("ai is used in drones, surveillance, and defense systems.\n")

            elif "ai in transport" in user:
                 return("ai helps in traffic prediction, self-driving cars, and route planning.\n")

            elif "ai in space" in user or "space" in user:
                 return("ai helps nasa in spacecraft navigation and data analysis from satellites.\n")

            elif   "music" in user:
                 return("ai can compose music and recommend playlists.\n")

            elif  "movies industry" in user:
                 return("ai suggests movies, creates effects, and even writes scripts.")  
            elif "ai in weather" in user:
                 return("ai predicts weather patterns and natural disasters.\n")

            elif "ai ethics" in user:
                 return("ai ethics deals with fairness, safety, privacy, and misuse concerns.\n")

            elif "ai in police" in user or "police" in user:
                return("ai is used in face recognition and crime prediction tools.\n")

            elif "ai in shopping" in user:
                 return("ai recommends products and personalizes ads.\n")

            elif "ai vs automation" in user:
                 return("automation follows fixed rules, while ai learns and adapts.\n")

            elif "ai vs human jobs" in user:
               return "ai may replace repetitive jobs, but humans are needed for creativity and emotions.\n"

            elif "ai languages" in user:
                 return("python is the most popular language for ai.\n")

            elif "ai tools" in user:
                 return("common ai tools are tensorflow, pytorch, keras, and scikit-learn.\n")

            elif "ai challenges" in user:
                 return("lack of data, high cost, bias, and ethical issues.\n")

            elif "ai in india" in user:
                 return("ai is used in agriculture, banking, health, and education in india.\n")

            elif "ai in future jobs" in user:
                return("ai will create jobs in robotics, data science, and machine learning.\n")

            elif "ai companies" in user:
                 return("openai ,meta ,microsoft , google are some of top companies in ai race")

            elif  "exit" in user or "quit" in user:
                 return("goodbye!")
                 

            else:  
               return("sorry, i don't know the answer to that yet.\n")




@app.route("/", methods=["GET", "POST"])
 
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = mb(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)