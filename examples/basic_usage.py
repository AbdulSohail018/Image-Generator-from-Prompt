import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generator import MultimodalGenerator
from src.config import GeneratorConfig

def main():
    # Create a custom configuration
    config = GeneratorConfig(
        num_inference_steps=50,
        guidance_scale=7.5,
        output_dir="example_outputs"
    )
    
    # Initialize the generator
    print("Initializing generator...")
    generator = MultimodalGenerator(config)
    
    # Example 1: Basic image generation
    prompt = "a serene lake surrounded by snow-capped mountains at sunset"
    print(f"\nGenerating image for: {prompt}")
    image_path = generator(prompt)
    print(f"Image saved at: {image_path}")
    
    # Example 2: Generation with negative prompt
    prompt = "a cute golden retriever puppy playing in a sunny park"
    negative_prompt = "blur, low quality, distorted"
    print(f"\nGenerating image with negative prompt...")
    image_path = generator.generate_image(
        prompt=prompt,
        negative_prompt=negative_prompt
    )
    print(f"Image saved at: {image_path}")

if __name__ == "__main__":
    main()