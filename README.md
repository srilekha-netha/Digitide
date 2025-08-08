#  Daily Progress

This repository contains the tasks completed as part of my daily learnings.

---

## 📅 Day-wise Summary

### ✅ Day 1: To-Do List App using Streamlit

- Built a fully functional To-Do List application using **Streamlit**.
- Features:
  - Add, edit, delete tasks
  - Mark tasks as complete
  - Display completed and deleted tasks
  <img width="1912" height="882" alt="tasktrek" src="https://github.com/user-attachments/assets/e6b53fa0-9576-455a-aa06-79b964dbde30" />


### ✅ Day 2: AWS Services — S3, EC2, Lambda

- **S3 Bucket:**
  - Created and uploaded folders/files to AWS S3.
- **EC2 Instance:**
  - Launched a virtual machine on AWS EC2.
- **Lambda Function:**
  - Developed a basic Python function deployed using AWS Lambda.


### ✅ Day 3: Myth Buster using Groq API + LangChain

- Built an AI chatbot that verifies common myths using:
  - Wikipedia (via LangChain wrapper)
  - Groq API with `meta-llama/llama-4-scout-17b-16e-instruct`
  - Natural language prompting
- Tech Stack:
  - LangChain
  - Groq Cloud LLM
  - Streamlit
  - Python
<img width="1902" height="877" alt="myth" src="https://github.com/user-attachments/assets/879e3fd8-1ab3-49ec-85e5-645cb1bd7ed2" />

### ✅ Day 4: PDF RAG Chatbot

- Build a simple PDF-based RAG chatbot using LangChain and Groq API.  
- Extract text from PDF, embed it, index it with FAISS, and use LLM to answer user queries.
- Features
  - Upload any **PDF** file
  - Automatic **text chunking**
  - **Semantic search** using FAISS
  - LLM-powered answers with **Groq LLaMA3**
  - Interactive **Streamlit UI**
  - Displays **retrieved context chunks**
<img width="1907" height="887" alt="image" src="https://github.com/user-attachments/assets/7118380a-3817-431c-a492-a4d176b922a9" />

### ✅ Additional Task: AWS Lambda + Amazon Bedrock (Prompt-Response Integration)

As part of the additional task given, I successfully implemented a Lambda function that interacts with Amazon Bedrock to send a prompt and receive a response.

#### 🔧 Tools & Technologies:
- AWS Lambda
- Amazon Bedrock (`meta.llama3-70b-instruct-v1:0`)
- Python (`boto3`)
- API Gateway (for external trigger)

### 📚 Assignment 3 & 4 – Rainbow Formation, Text Splitting, Poem Generator

#### Rainbow Formation

- Accepts custom prompts or uses default: _"Explain how rainbows are formed"_
- Uses **Groq LLM (LLaMA 3)** for generating explanations
- Displays AI explanation in clean paragraphs
- Generates a **vertical flowchart** visualizing the rainbow formation process
- Provides tips and fun facts about light, reflection, and dispersion
<img width="1910" height="1015" alt="r11" src="https://github.com/user-attachments/assets/c270ee1d-f869-48f2-a882-84636d909562" />
<img width="1918" height="1020" alt="r12" src="https://github.com/user-attachments/assets/c8feeeb7-8327-4325-9995-354741039011" />

#### Poem Generator

Users can input their poem preferences:
- **Topic** – e.g., love, rain, friendship, stars
- **Tone** – emotional, funny, romantic, etc.
- **Length** – number of lines
  <img width="1915" height="886" alt="poem" src="https://github.com/user-attachments/assets/6cb81880-595d-4750-8a8b-afbb6d381f57" />


#### Text Splitter

- Loads text with `TextLoader` (for `.txt`) or `PyPDFLoader` (for `.pdf`)
- Splits documents into overlapping chunks for processing
- Prints the total number of chunks generated


