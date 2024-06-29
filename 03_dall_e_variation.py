from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Variation is DALL-E-2 only
response = client.images.create_variation(
    model='dall-e-2',
    image=open('Coconut.png', 'rb'),
    n=1,
    size='1024x1024'
)

print(f'Variation image: {response.data[0].url}')


# Edit is also DALL-E-2 only
response = client.images.edit(
    model='dall-e-2',
    image=open('Coconut.png', 'rb'),
    mask=open('Mask.png', 'rb'),
    prompt='A football ball in the beach',
    n=1,
    size='1024x1024'
)

print(f'Edited image: {response.data[0].url}')

response = client.images.edit(
    model='dall-e-2',
    image=open('shinchan.png', 'rb'),
    mask=open('shinchan_mask.png', 'rb'),
    prompt=input('Describe the image in a way that you want to edit: '),
    n=1,
    size='1024x1024'
)

print(f'Edited image: {response.data[0].url}')
