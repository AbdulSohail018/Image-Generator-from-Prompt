import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import logging
from typing import Optional, Union, List
import os

from .config import GeneratorConfig
from .utils import setup_device, generate_filename, ensure_directory, save_image

logger = logging.getLogger(__name__)

class MultimodalGenerator:
    """A class for generating images from text prompts using Stable Diffusion."""
    
    def __init__(self, config: Optional[GeneratorConfig] = None):
        """
        Initialize the multimodal generator.
        
        Args:
            config: Configuration for the generator
        """
        self.config = config or GeneratorConfig()
        self.device = setup_device(self.config.device)
        
        # Initialize the model
        self._initialize_model()
        
        # Set up output directory
        self.output_dir = ensure_directory(self.config.output_dir)
    
    def _initialize_model(self):
        """Initialize the Stable Diffusion model with appropriate settings."""
        try:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                self.config.model_id,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
            )
            self.pipe = self.pipe.to(self.device)
            
            # Apply optimization settings
            if self.config.enable_attention_slicing:
                self.pipe.enable_attention_slicing()
            if self.config.enable_vae_slicing:
                self.pipe.enable_vae_slicing()
                
            logger.info("Model initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing model: {str(e)}")
            raise
    
    def generate_image(
        self,
        prompt: str,
        negative_prompt: Optional[str] = None,
        num_images: int = 1,
        **kwargs
    ) -> Union[str, List[str]]:
        """
        Generate image(s) based on the text prompt.
        
        Args:
            prompt: Text description of the image to generate
            negative_prompt: Things to avoid in the image
            num_images: Number of images to generate
            **kwargs: Additional arguments to pass to the pipeline
        
        Returns:
            Union[str, List[str]]: Path(s) to the saved image(s)
        """
        try:
            # Update generation parameters with any provided kwargs
            params = {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "num_inference_steps": self.config.num_inference_steps,
                "guidance_scale": self.config.guidance_scale,
                "num_images_per_prompt": num_images,
                **kwargs
            }
            
            # Generate images
            logger.info(f"Generating {num_images} image(s) for prompt: {prompt}")
            result = self.pipe(**params)
            
            # Save images and collect paths
            paths = []
            for i, image in enumerate(result.images):
                filename = generate_filename(f"generated_{i+1}", self.config.save_format)
                filepath = os.path.join(self.output_dir, filename)
                save_image(image, filepath, self.config.save_format)
                paths.append(filepath)
            
            return paths[0] if num_images == 1 else paths
            
        except Exception as e:
            logger.error(f"Error generating image: {str(e)}")
            raise
    
    def __call__(self, prompt: str) -> str:
        """
        Convenient way to generate a single image.
        
        Args:
            prompt: Text description of the image to generate
            
        Returns:
            str: Path to the saved image
        """
        return self.generate_image(prompt)