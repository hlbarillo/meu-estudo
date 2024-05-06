import requests
import streamlit as st
import json

app = requests

base_url="https://jsonplaceholder.typicode.com"


# response=app.get(f"{base_url}/posts")
response=app.post(f"{base_url}/posts",data={"title":"flamengo","userId":2,"body":"ola"})

# response =json.loads(response.data)

response=response.json()
print(response)
# for post in response:
#     print(post['title'])
#     st.title(post['body'])
#     # st.text(post.body)