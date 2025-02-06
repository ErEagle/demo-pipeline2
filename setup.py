from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="vinnu",
      author_email="vinn@gmail.ccom",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )