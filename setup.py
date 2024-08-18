from httplib2.auth import authentication_info
from setuptools import setup, find_packages
from typing import  List


def get_requirements():
    '''
    :return: List of requirements
    '''
    requirements = []

    try:
        with open('requirements.txt', 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement !='-e .':
                    requirements.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')

    return requirements


print(get_requirements())




setup(
        name='opsurlsecurity',
        version='0.0.1',
        description='opsurlsecurity',
        author='Shoaib Shaikh',
        author_email='shoowaib95@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements()
     )

