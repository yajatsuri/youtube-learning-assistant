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
        You are an expert learning assistant that transforms video transcripts into high-quality study material.

        Your goal is to help students understand, revise, retain and apply the knowledge from the video.

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

        EXECUTIVE SUMMARY GUIDELINES:

        - Provide a concise but information-dense overview.
        - Capture the main topic, purpose and conclusions.
        - Focus on the most important ideas.

        DETAILED NOTES GUIDELINES:

        - Convert the transcript into structured study notes.
        - Organize information logically.
        - Focus on concepts, definitions, explanations, frameworks, processes and examples.
        - Remove filler content and repetition.
        - Preserve technical accuracy.
        - Explain complex ideas in simpler language.
        - Include important examples when available.

        IMPORTANT:

        - Write detailed_notes as plain text paragraphs.
        - Do not use markdown headings.
        - Do not use bullet points.
        - Do not include JSON snippets inside detailed_notes.

        KEY TAKEAWAYS GUIDELINES:

        - Extract the most important lessons.
        - Each takeaway should be specific and meaningful.

        RULES:

        - Return valid JSON only.
        - No markdown code fences.
        - No explanations.
        - No text before JSON.
        - No text after JSON.

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


        if isinstance(response.content, dict):
            return response.content

        if isinstance(response.content, list):
            return {
                "executive_summary": "Response returned as list",
                "detailed_notes": str(response.content),
                "key_takeaways": []
            }

        cleaned_response = response.content.strip()

        if cleaned_response.startswith("```json"):
            cleaned_response = cleaned_response.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            ).strip()

        notes = json.loads(
            cleaned_response
        )

        return notes

    except Exception as e:

        logger.exception(
            "LLM generation failed"
        )

        raise LLMGenerationError(
            f"LLM generation failed: {str(e)}"
        )


def generate_audio_insights(
    transcript: str
):

    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert communication analyst.

        Analyze the transcript and return ONLY valid JSON.

        Output format:

        {{
            "summary": "string",

            "key_takeaways": [
                "point 1",
                "point 2",
                "point 3"
            ],

            "communication_analysis": {{
                "overall_sentiment": "positive | neutral | negative | mixed",

                "emotional_tone": "string",

                "speaker_intent": "string",

                "urgency_level": "low | medium | high",

                "confidence_level": "low | medium | high",

                "communication_style": "string",

                "likely_emotional_state": "string"
            }}
        }}

        Rules:

        - Return valid JSON only.
        - No markdown.
        - No code fences.
        - No explanations.
        - No text before or after JSON.

        Transcript:
        {transcript}
        """
    )

    chain = prompt | llm

    try:

        logger.info(
            "Generating audio insights using Gemini"
        )

        response = chain.invoke(
            {
                "transcript": transcript
            }
        )

        if isinstance(response.content, dict):
            return response.content

        if isinstance(response.content, list):
            return {
                "summary": str(response.content),
                "key_takeaways": [],
                "communication_analysis": {}
            }

        cleaned_response = response.content.strip()

        if cleaned_response.startswith("```json"):
            cleaned_response = cleaned_response.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            ).strip()

        insights = json.loads(
            cleaned_response
        )

        return insights

    except Exception as e:

        logger.exception(
            "Audio insights generation failed"
        )

        raise LLMGenerationError(
            f"Audio insights generation failed: {str(e)}"
        )
