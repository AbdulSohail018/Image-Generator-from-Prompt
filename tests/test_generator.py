import pytest
import os
from PIL import Image
from src.generator import MultimodalGenerator
from src.config import GeneratorConfig

@pytest.fixture
def generator():
    """Create a generator instance for testing."""
    config = GeneratorConfig(
        model_id="runwayml/stable-diffusion-v1-5",
        num_inference_steps=20,  # Lower for faster testing
        output_dir="test_outputs"
    )
    return MultimodalGenerator(config)

def test_generator_initialization(generator):
    """Test that the generator initializes properly."""
    assert generator is not None
    assert generator.pipe is not None
    assert os.path.exists(generator.output_dir)

def test_generate_single_image(generator):
    """Test generating a single image."""
    prompt = "a test image of a blue circle"
    result = generator.generate_image(prompt)
    
    assert isinstance(result, str)
    assert os.path.exists(result)
    assert result.endswith(".png")
    
    # Verify the image
    img = Image.open(result)
    assert img.size == (512, 512)  # Default size

def test_negative_prompt(generator):
    """Test generation with negative prompt."""
    prompt = "a colorful landscape"
    negative_prompt = "monochrome, black and white"
    result = generator.generate_image(prompt, negative_prompt=negative_prompt)
    
    assert isinstance(result, str)
    assert os.path.exists(result)

def teardown_module(module):
    """Clean up test outputs."""
    import shutil
    if os.path.exists("test_outputs"):
        shutil.rmtree("test_outputs")