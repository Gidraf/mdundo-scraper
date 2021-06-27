import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mdundo-scraper-pkg-Gidraf",
    version="0.0.1",
    author="Gidraf Orenja",
    author_email="orenjagidraf@gmail.com",
    description="Scrapes songs from mdundo.com site",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gidraf/mdundo-scraper",
    project_urls={
        "Bug Tracker": "https://github.com/Gidraf/mdundo-scraper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)