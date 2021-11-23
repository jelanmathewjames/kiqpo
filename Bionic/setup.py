import setuptools

with open("./public/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bionic.web",
    version="1.0.1",
    author="shajin-sha",
    author_email="shajin.sha10@gmail.com",
    description="Bionic is Python Framework for crafting beautiful",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bionic-py/Bionic",
    project_urls={
        "Bug Tracker": "https://github.com/bionic-py/Bionic/issues",
        "doc": "https://bionic-py.github.io/Bionic-Documentation/"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["core"],
    scripts=["./Bionic.py"],
    python_requires=">=3.6",
)