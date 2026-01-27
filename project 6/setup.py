from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This Funcation will return the list of requirements
    
    '''
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements =[req.replace('\n',"") for req in requirements]
        
        return requirements

setup(
    name='MLproject',
    version=0.01,
    author='chilesh',
    author_email='tschilesh7@gmail.com',
    packages=find_packages(),
    install_reguires = get_requirements('requirements.txt')
)

