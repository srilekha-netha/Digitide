import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

load_dotenv()

def check_myth_with_wiki(user_input):
    # Setup Groq LLM
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="meta-llama/llama-4-scout-17b-16e-instruct"
    )

    # Fetch Wikipedia summary
    wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1500)
    wiki_result = wiki.run(user_input)

    # Prompt template
    prompt_template = """
You are an expert AI trained to verify common beliefs using reliable data.

Task:
Based on the Wikipedia extract, determine if the belief is TRUE, FALSE, or UNVERIFIED. Then provide a short explanation.

Belief: "{belief}"

Wikipedia Summary:
{wiki_summary}

Respond strictly in the following format:
Verdict: (True / False / Unverified)
Explanation: (2-3 sentence reasoning)
"""

    prompt = PromptTemplate(
        input_variables=["belief", "wiki_summary"],
        template=prompt_template
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    result = chain.run({
        "belief": user_input,
        "wiki_summary": wiki_result
    })

    return result
