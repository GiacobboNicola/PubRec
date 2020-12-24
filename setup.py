import setuptools

setuptools.setup(
    name="pubrec",
    version="1.0",
    author="Nicola Giacobbo",
    author_email="giacobbo.nicola@gmail.com",
    description="Count citations of paper available in ADS archive",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Languages :: Python :: 3",
        "License :: OIS Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)