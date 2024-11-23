from dataclasses import dataclass
from typing import Optional

@dataclass
class GeneratorConfig:
    """Configuration for the multimodal generator."""
    
    # Model configuration
    model_id: str = "runwayml/stable-diffusion-v1-5"
    device: Optional[str] = None  # If None, will be automatically determined
    
    # Generation parameters
    num_inference_steps: int = 50
    guidance_scale: float = 7.5
    image_size: tuple = (512, 512)
    
    # Output configuration
    output_dir: str = "generated_images"
    save_format: str = "png"
    
    # Advanced options
    enable_attention_slicing: bool = True
    enable_vae_slicing: bool = True
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if self.num_inference_steps < 1:
            raise ValueError("num_inference_steps must be positive")
        if self.guidance_scale < 1:
            raise ValueError("guidance_scale must be at least 1.0")