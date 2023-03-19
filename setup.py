from setuptools import find_packages, setup    ##automaticall to find all packages installed in our ml project
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'ml-project',
    version = '0.0.1',
    author = 'Abker',
    author_email = 'aabdalla1088@gmail.com',
    packages = find_packages(),
    install_requires= get_requirements('requirements.txt')


)