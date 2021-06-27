import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mdundo-scraper',
    description='Get songs data in json from mdundo.com site with ease inspired by https://soundcloud-scraper.js.org/ ',
    long_description=long_description,
    version='0.0.1',
    url='https://github.com/Gidraf/mdundo-scraper',
    license='BSD-2',
    author='Gidraf Orenja',
    author_email='orenjagidraf@gmail.com',
    maintainer='Gidraf Orenjaa',
    maintainer_email='orenjagidraf@gmail.com',
    install_requires=[
        'beautifulsoup4',
        'requests-cache',
        'lxml',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    project_urls={
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/Gidraf/mdundo-scraper',
        'Tracker': 'https://github.com/Gidraf/mdundo-scraper/issues',
    },
    python_requires='>=3.6',
    zip_safe=False
)