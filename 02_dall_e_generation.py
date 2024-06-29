from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.images.generate(
    model='dall-e-2',
    prompt=input('Describe the image you want to generate: '),
    size='512x512',
    n=1
)

print(response)    # openai.types.images_response.ImagesResponse class
print(response.data[0].url)