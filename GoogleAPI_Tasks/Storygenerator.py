from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

#  Inputs


genre = input("Enter story genre ( horror, mystery, fantasy): ")
character_name = input("Enter main character name: ")
character_trait = input("Enter character trait (brave, shy, funny, evil, etc.): ")
setting = input("Enter story setting (city, jungle, space, ancient times): ")
conflict = input("Enter main conflict (lost treasure, alien invasion, broken friendship, etc.): ")
story_length = input("Enter story length (short, medium, long): ")
output_format = input("Enter output format (narrative, script, dialogue-based): ")

story_prompt = f"""
Write a {story_length} {genre} story.
Main character: {character_name}, who is {character_trait}.
Setting: {setting}.
Main conflict: {conflict}.
Output format: {output_format}.
"""

result = model.invoke(story_prompt)
print("GENERATED STORY!!!")
print(result.content)

