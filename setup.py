from setuptools import setup, find_packages

setup(
    name="earthquake_parser",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to parse and analyze earthquake data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_GITHUB_USERNAME/earthquake_parser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


