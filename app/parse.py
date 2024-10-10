from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from typing import List
import logging
from dotenv import load_dotenv
import os

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv() 
# Define prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the model outside the function to avoid re-initializing
model = OllamaLLM(model=os.getenv('OLLAMA_MODEL', "llama3.2:1b"))

def parse_with_ollama(dom_chunks: List[str], parse_description: str) -> str:
    """
    Parses chunks of DOM content using the Ollama LLM based on the provided description.

    Args:
        dom_chunks (List[str]): List of DOM content chunks to process.
        parse_description (str): The description of the data to be extracted.

    Returns:
        str: Concatenated parsed results from all chunks.
    """
    # Create the prompt template
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model  # Create chain once for reuse

    parsed_result = []
    
    for index, chunk in enumerate(dom_chunks, start=1):
        try:
            # Invoke the chain with the chunk and description
            response = chain.invoke(
                {"dom_content": chunk, "parse_description": parse_description}
            )
            logger.info(f"Parsed batch {index} of {len(dom_chunks)}")
            parsed_result.append(response)
        except Exception as e:
            logger.error(f"Error parsing batch {index}: {e}")
            parsed_result.append("")  # Optionally append empty on error

    # Return concatenated result
    return "\n".join(parsed_result)

