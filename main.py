# Ai Powered Course Recommendation App (@ Author: Hafsah Robleh)
# A Python app that recommends online courses based on a user's interests, skill level, and learning style
# <---- Importing Dependencies ---->
import requests

print("please answer the following questions to better recommend you a course")

def questions():
    question1= input("please type in a keyword on a topic you are interested in (for example machine learning):")
    question2= input('are you a beginner, intermediate or an advanced learner on the topic? type out "beginner", "intermediate" or "advanced": ')
    question3= input('Would you say you are more of a hands on or visual learner? type out "hands on" or "visual learner":')
questions()

def search():
    query=(f"{question2} AND {question1} AND {question3} course ")
    url= ("https://duckduckgo.com/")
    params = {"q":query}
    response=requests.post(url,data=params)
    print(response)
response()


