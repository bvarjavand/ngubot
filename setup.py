import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nglbot",  # Replace with your own username
    version="0.0.1",
    author="Bijan Varjavand",
    author_email="bvarjavand@gmail.com",
    description="Tools to automate actions in NGL : Idle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bvarjavand/nglbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
