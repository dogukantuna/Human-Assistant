from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="human_assistant",
    version="0.0.1",
    author="dogukantai",
    description="A simple chat template library to make transformations on Human & Assistant and Instruction datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dogukantai/human-assistant",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10",
    install_requires=["datasets>=2.14.5", "transformers>=4.33.3"],
    keywords="fine-tuning chat templates datasets transformations",
)
