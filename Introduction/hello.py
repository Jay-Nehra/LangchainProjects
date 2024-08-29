from pathlib import Path
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from loguru import logger
from ReachOut.third_parties.linkedIn_parser import linkedIn_scrap


def retrieve_information(filename: str) -> str:
    filepath = Path(filename)
    
    if filepath.is_file():
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    else:
        logger.error(f"The file {filename} does not exist.")
        raise FileNotFoundError(f"The file {filename} does not exist.")

def LLM_profile_summary(local: bool = False):
    if local:
        file = 'Introduction/elon_musk_wiki_intro.txt'
        context = retrieve_information(file)
    else:
        context = linkedIn_scrap('')
            
    summary_template = """
    Given the information in the context which is enclosed in the `CONTEXT` tags, Please create a summary introduction of this person and also provide two interesting facts from the given information:
    [CONTEXT]
    {context}
    [/CONTEXT]
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["context"],
        template=summary_template,
    )
    
    model = ChatOpenAI(
        temperature=0.75,
        model='gpt-3.5-turbo',
        )
    
    chain = summary_prompt_template | model
    
    try:
        response = chain.invoke(input={"context": context})
        print(response)
    except Exception as e:
        logger.error(f"An error occurred during the OpenAI call: {e}")

if __name__=='__main__':
    print("Langchain Version 0.2.6 Experimentation!")
    LLM_profile_summary()