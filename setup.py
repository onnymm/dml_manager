from setuptools import setup, find_packages

setup(
    # Library name and version
    name="dml_manager",
    version="0.1.1",
    
    # Dependencies
    install_requires=[
        "pandas==2.2.3",
        "psycopg2==2.9.10",
        "SQLAlchemy==2.0.37",
    ],

    # My name here
    author="Pável Hernández",
    # Feel free to email me
    author_email="onnymm@outlook.com",

    # Library description
    description="Librería dedicada a la gestión de transacciones en bases de datos, orientada a PostgreSQL",

    # Documentation
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/onnymm/dml_manager",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    packages=find_packages(),
)