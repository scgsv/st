import streamlit as st
import openai

st.title("CAP4936: Special Topics in Data Analytics with Dr. Lee")
st.sidebar.image('https://clipground.com/images/miami-dade-college-logo-7.png', width=100)
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    )


model_engine = 'text-davinci-003'
openai.api_key = "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"

# Add a function for each tab
def code_help_tab():
    user_query = st.text_input("Enter query here, to exit enter :q", "write a python class with a sample method?")
    if user_query != ":q" or user_query != "":
        response = ChatGPT(user_query)
        # st.code('for i in range(8): foo()')
        return st.code(f"{user_query} {response}")

def ChatGPT(user_query):
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0]["text"]
    lines = response.split("\n")
    indented_lines = ['    ' + line for line in lines]
    indented_response = '\n'.join(indented_lines)
    return indented_response

def concept_tab():
    user_query = st.text_input("Describe a concept that you would like to understand: ")
    if user_query != ":q" or user_query != "":
        prompt = "Explain this concept at the level of a 16 year old.  Use analogies, real world examples, and provide an easy, creative intuitive explanation: " + user_query
        chatgpt = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024)
        # print(chatgpt.choices[0]['text'])
        # print(type(chatgpt.choices[0]['text']))
        response = chatgpt.choices[0]["text"].replace("\n", "") # to remonve all the \n - Courtesy of Alex Z.
        # response = get_sentiment(user_query)
        return st.write(f"{response}")

def explain_code_tab():
    st.title("Code Editor")

    code_input = st.text_area("Paste your code here")

    if code_input:
        st.write("Output:")
        st.code(code_input)
def sentiment_tab():
    user_query = st.text_input("Place a passage or tweet here and we will decide the sentiment")
    if user_query != ":q" or user_query != "":
        prompt = "Decide the sentiment of a passage as positive,neutral, or negative and give the percent confidence: " + user_query
        chatgpt = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024)
        # print(chatgpt.choices[0]['text'])
        # print(type(chatgpt.choices[0]['text']))
        response = chatgpt.choices[0]["text"].replace("\n", "") # to remonve all the \n - Courtesy of Alex Z.
        # response = get_sentiment(user_query)
        return st.write(f"{response}")
    
  
def image_tab():
    user_query = st.text_input("Describe an image that you would like to see:")
    if user_query != ":q" or user_query != "":
        prompt = "photorealistic in the style of disney: " + user_query
        response = openai.Image.create(prompt=prompt, n=1,size="1024x1024")
        image_url = response['data'][0]['url']
        # return st.write(f"{image_url}")
        return st.image(image_url, width=400, # Manually Adjust the width of the image as per requirement
        )

# Add the tabs to the app
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio("Select a tab", ["Code Help", "Concept Help", "Explain this code", "Sentiment","Image"])

if selected_tab == "Code Help":
    code_help_tab()
elif selected_tab == "Concept Help":
    concept_tab()
elif selected_tab == "Sentiment":
    sentiment_tab()
elif selected_tab == "Image":
    image_tab()
else:
    explain_code_tab()
