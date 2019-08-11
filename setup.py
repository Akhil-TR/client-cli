from setuptools import setup
setup(
    name = 'client-cli',
    version = '0.1.0',
    packages = ['client'],
    entry_points = {
        'console_scripts': [
            'client = client.__main__:main'
        ]
    })