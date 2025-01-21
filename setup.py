from setuptools import setup, find_packages

setup(
    name="hiveagentai",
    version="0.2.0",
    author="HiveagentAI Dev",
    author_email="dev@hiveagentai.com",
    description="The ultimate platform for orchestrating intelligent teamwork.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://www.hiveagentai.com/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
