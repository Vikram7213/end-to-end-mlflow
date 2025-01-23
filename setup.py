from setuptools import setup, find_packages

setup(
    name="ml_project",                     # Name of your project
    version="0.1.0",                       # Version of your project
    description="A sample Python project", # Short description of the project
    author="vikram",                    # Your name
    author_email="fatesend21@gmail.com", # Your email
    package_dir={"": "src"},               # Root of packages is the 'src' directory
    packages=find_packages(where="src"),   # Automatically find packages in 'src'        
)
