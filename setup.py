import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Vaibhav15032704"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "vaibhavdeshmukh5121@gmail.com"



setuptools.setup(
    name=Text-Summarizer-Project,
    version=0.0.0,
    author=Vaibhav15032704,
    author_email=vaibhavdeshmukh5121@gmail.com,
    description="A text Summarization Project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Vaibhav15032704}/{Text-Summarizer-Project}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Vaibhav15032704}/{Text-Summarizer-Project}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)