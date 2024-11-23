# Image Generator from Prompt

A Python package for generating images from text descriptions using Stable Diffusion.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AbdulSohail018/multimodal-generator.git
cd multimodal-generator
```

2. Create and activate a virtual environment:
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install the package:
```bash
pip install -e .
```

## Quick Start

```python
from src.generator import MultimodalGenerator

# Initialize the generator
generator = MultimodalGenerator()

# Generate a single image
image_path = generator("a serene lake surrounded by mountains")
print(f"Image saved to: {image_path}")

# Generate multiple images with custom parameters
images = generator.generate_image(
    prompt="a cute puppy playing in the park",
    negative_prompt="blur, low quality",
    num_images=2,
    num_inference_steps=50,
    guidance_scale=7.5
)
```

## Features

- Text-to-image generation using Stable Diffusion
- Support for multiple images per prompt
- Negative prompts for better control
- Customizable generation parameters
- Automatic device selection (CPU/GPU)
- Comprehensive logging
- Error handling and validation
- Organized output management

## Configuration

You can customize the generator behavior using the `GeneratorConfig` class:

```python
from src.config import GeneratorConfig

config = GeneratorConfig(
    model_id="runwayml/stable-diffusion-v1-5",
    num_inference_steps=50,
    guidance_scale=7.5,
    output_dir="my_generated_images",
    save_format="png"
)

generator = MultimodalGenerator(config)
```

## Development

1. Install development dependencies:
```bash
pip install pytest black flake8 isort
```

2. Run tests:
```bash
pytest tests/
```

3. Format code:
```bash
black src/ tests/
isort src/ tests/
flake8 src/ tests/
```

## Project Structure

```
Image Generator from Prompt/
│
├── src/
│   ├── __init__.py       # Makes src a Python package
│   ├── generator.py      # Main generator class
│   ├── config.py         # Configuration handling
│   └── utils.py          # Utility functions
│
├── tests/
│   ├── __init__.py       # Makes tests a package
│   └── test_generator.py # Test cases
│
├── examples/
│   └── basic_usage.py    # Example usage
│
├── output_images/        # Directory for generated images
│
├── .gitignore           # Git ignore file
├── LICENSE              # License file
├── README.md           # Project documentation
├── setup.py           # Package setup file
└── run.py             # Main script to run the generator
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Requirements

- Python 3.8+
- PyTorch
- Diffusers
- Transformers
- Other dependencies listed in requirements.txt
