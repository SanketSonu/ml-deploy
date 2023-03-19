# This file will be responsible for creating my ML application as a package. Others can install this package for their project and can use it.
# We can even deploy our python package (ML app) in official python PyPi so that other can use it (But here I'am not going to deploy in Pypi)

from setuptools import find_packages, setup 
from typing import List 

HYPEN_E_DOT = '-e .' # When user will run requirements.txt file to install all required packages, this '-e .' will automatically trigger 'setup.py' file.

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:            # We don't need '-e .' here in the list.
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Package name, version, other details:
setup(
    name = 'ml-deploy',
    version='0.0.1',
    author='Sanket',
    author_email='sanketsonu321@gmail.com',
    packages=find_packages(),
    # install_requires=['numpy','pandas','seaborn']
    install_requires=get_requirements('requirements.txt')
)