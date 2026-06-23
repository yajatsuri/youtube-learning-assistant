from app.services.llm_service import generate_notes

result = generate_notes(
    "Python is a programming language used for AI and web development."
)

print(result)
