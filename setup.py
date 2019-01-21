from setuptools import setup


setup(
    name="scrape",
    version="0.1",
    py_modules=["scrape"],
    install_requires=[
        "Click",
        "requests",
        "beautifulsoup4"
    ],
    entry_points="""
        [console_scripts]
        scrape=scrape:cli
    """
    
)