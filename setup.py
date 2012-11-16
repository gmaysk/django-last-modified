from setuptools import setup

setup(
    name="django-last-modified",
    version="0.1",
    author="Eric Davis",
    author_email="ed@npri.org",
    packages=["last_modified"],
    url="http://github.com/edavis/django-last-modified",
    license="MIT",
    description="Django middleware for adding freshness and validation cache headers",
    classifiers = [
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)