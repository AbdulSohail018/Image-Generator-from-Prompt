from setuptools import setup, find_packages

setup(
    name="image-generator-from-prompt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "diffusers>=0.19.0",
        "transformers>=4.30.0",
        "accelerate>=0.21.0",
        "Pillow>=9.5.0",
        "opencv-python>=4.7.0",
        "numpy>=1.24.0",
        "tqdm>=4.65.0",
        "requests>=2.31.0",
    ],
    author="Abdul Sohail Ahmed",
    author_email="abdulsohail018@gmail.com",
    description="An Image generator using LLMs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AbdulSohail018/image-generator-from-prompt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)