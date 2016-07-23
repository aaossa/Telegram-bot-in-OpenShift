from setuptools import setup

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = str()
with open('README.md') as f:
    readme = f.read()

setup(name='Telegram bot in OpenShift',

      # PEP 440 -- Version Identification and Dependency Specification
      version='0.0.1',

      # Project description
      description='A really small and simple Telegram bot',
      long_description=readme,

      # Author details
      author='Antonio Ossa',
      author_email='aaossa@uc.cl',

      # Project details
      url='https://github.com/aaossa/Telegram-bot-in-OpenShift',
      license="GNU v3",

      # Project dependencies
      install_requires=requirements,
      )
