from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    """
    this function will return the list of requirements
    
    """
    try:
        with open('requirements.txt') as file:
            #Read lines from the file
            lines=file.readlines()
            #process each line 
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author="Abhinand",
    author_email="abhiprameesh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)