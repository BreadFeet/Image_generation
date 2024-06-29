import torch
from diffusers import DiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"

pipeline = DiffusionPipeline.from_pretrained(
    model_id, torch_dtype=torch.float16, use_safetensors=True
)

# Set seed for reproducible images
generator = torch.Generator().manual_seed(123456789)

prompt = "A picture of a pepperoni pizza on a restaurant table"

image = pipeline(prompt, generator=generator).images[0]
image.save('output_image.png')