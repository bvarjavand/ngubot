import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ngubot",  # Replace with your own username
    version="0.0.1",
    author="Bijan Varjavand",
    author_email="bvarjavand@gmail.com",
    description="Tools to automate actions in NGU : Idle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bvarjavand/nglbot",
    packages=setuptools.find_packages(),
    install_requires=[
        "MouseInfo==0.1.3",
        "mss==6.0.0",
        "numpy==1.19.0",
        "opencv-python==4.3.0.36",
        "pandas==1.0.5",
        "Pillow==10.0.1",
        "PyAutoGUI==0.9.50",
        "PyGetWindow==0.0.8",
        "PyMsgBox==1.0.8",
        "pyperclip==1.8.0",
        "PyRect==0.1.4",
        "PyScreeze==0.1.26",
        "python-dateutil==2.8.1",
        "PyTweening==1.0.3",
        "pytz==2020.1",
        "six==1.15.0",
        "xlrd==1.2.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
