import logging
from src.generator import MultimodalGenerator
from src.config import GeneratorConfig

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        # Create configuration
        config = GeneratorConfig(
            num_inference_steps=30,
            output_dir="output_images"
        )
        
        # Initialize generator
        print("Initializing generator... This may take a moment...")
        generator = MultimodalGenerator(config)
        
        # Get prompt from user
        prompt = input("\nEnter your image prompt: ")
        
        print("\nGenerating image... This may take a few minutes.")
        
        # Generate image
        image_path = generator.generate_image(
            prompt=prompt,
            negative_prompt="blur, low quality, distorted, deformed"
        )
        
        print(f"\nSuccess! Image saved at: {image_path}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()