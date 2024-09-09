import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class Generator:
    def __init__(self, api_key=None):
        load_dotenv()  # 加载.env文件
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(api_key=self.api_key)
        self.prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="Context: {context}\n\nQuestion: {question}\n\nAnswer:"
        )
    
    def generate(self, context, question):
        prompt = self.prompt_template.format(context=context, question=question)
        return self.llm(prompt)