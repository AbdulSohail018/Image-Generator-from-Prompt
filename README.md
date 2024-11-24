# 🎨 Image Generator from Prompt

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-v1.5-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

*Transform your imagination into stunning visual reality with AI-powered image generation*

[Installation](#installation) • [Quick Start](#quick-start) • [Features](#features) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

## 🌟 Overview

Welcome to **Image-Generator-from-Prompt**, an advanced AI-powered image-generation system that transforms textual descriptions into stunning visual artworks. Built on the foundation of Stable Diffusion technology, this project represents a sophisticated blend of natural language processing and image generation capabilities.

## ⚡ Installation

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (optional)
- 8GB+ RAM recommended

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/AbdulSohail018/Image-Generator-from-Prompt.git
cd Image-Generator-from-Prompt
```

2. **Create and activate virtual environment:**
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. **Install the package:**
```bash
pip install -e .
```

## 🚀 Quick Start

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

## 🎯 Features

- 🎨 Text-to-image generation using Stable Diffusion
- 🔄 Support for multiple images per prompt
- 🎯 Negative prompts for better control
- ⚙️ Customizable generation parameters
- 💻 Automatic device selection (CPU/GPU)
- 📝 Comprehensive logging
- 🛡️ Error handling and validation
- 📁 Organized output management

## ⚙️ Configuration

Customize the generator behavior using the `GeneratorConfig` class:

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

## 👨‍💻 Development

1. **Install development dependencies:**
```bash
pip install pytest black flake8 isort
```

2. **Run tests:**
```bash
pytest tests/
```

3. **Format code:**
```bash
black src/ tests/
isort src/ tests/
flake8 src/ tests/
```

## 📁 Project Structure

```
Image-Generator-from-Prompt/
│
├── src/                  # Source code
│   ├── __init__.py      # Makes src a Python package
│   ├── generator.py     # Main generator class
│   ├── config.py        # Configuration handling
│   └── utils.py         # Utility functions
│
├── tests/               # Test suite
│   ├── __init__.py     
│   └── test_generator.py
│
├── examples/            # Example scripts
│   └── basic_usage.py  
│
├── output_images/       # Generated images
│
├── .gitignore          # Git ignore file
├── LICENSE             # License file
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
├── setup.py           # Package setup file
└── run.py             # Main script
```

## 🛠️ Technical Stack

- **Core:** Python 3.8+, PyTorch
- **AI Models:** Stable Diffusion, Transformers
- **Image Processing:** Pillow, OpenCV
- **Development:** pytest, black, flake8
- **Documentation:** Markdown

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💡 Tips for Better Results

- Be specific in your prompts
- Use quality indicators like "high quality", "detailed"
- Experiment with negative prompts
- Adjust parameters for optimal results

## 📫 Support

For support, please open an issue in the GitHub repository.

---

<div align="center">

Made with ❤️ by [AbdulSohail018](https://github.com/AbdulSohail018)

</div>
