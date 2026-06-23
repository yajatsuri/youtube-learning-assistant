import os
import json
import logging

from dotenv import load_dotenv

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from langchain_core.prompts import (
    ChatPromptTemplate
)

from app.exceptions.custom_exceptions import (
    LLMGenerationError
)

load_dotenv()

logger = logging.getLogger(__name__)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    ),
    temperature=0.3
)


def generate_notes(
    transcript: str
):

    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert learning assistant.

        Analyze the transcript and return ONLY valid JSON.

        Output format:

        {{
            "executive_summary": "string",
            "detailed_notes": "string",
            "key_takeaways": [
                "point 1",
                "point 2",
                "point 3"
            ]
        }}

        Rules:
        - Return valid JSON only
        - No markdown
        - No code fences
        - No explanations
        - No text before or after JSON

        Transcript:
        {transcript}
        """
    )

    chain = prompt | llm

    try:

        logger.info(
            "Generating notes using Gemini"
        )

        response = chain.invoke(
            {
                "transcript": transcript
            }
        )

        logger.info(
            "Gemini response received successfully"
        )

        logger.info(
            "Parsing Gemini JSON response"
        )

        notes = json.loads(
            response.content
        )

        logger.info(
            "Notes generated successfully"
        )

        return notes

    except Exception as e:

        logger.exception(
            "LLM generation failed"
        )

        raise LLMGenerationError(
            f"LLM generation failed: {str(e)}"
        )
