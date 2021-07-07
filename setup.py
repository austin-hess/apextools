from setuptools import setup
setup(
    name="apextools",
    version="0.0.1",
    entry_points={
        'console_scripts': [
            'apextools=apextools:main'
        ]
    },
    install_requires=[
        'click==7.1.2'
    ]
)