from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    
    this function will return the list of requirements
    
    '''
    requirements = []
    HYPEN_E_DOT = '-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



setup(
    name = 'mlproject',
    version='0.01',
    author='Harsh',
    author_email='harsh.1020kc@gmai.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)