from setuptools import setup , find_packages
from typing import List

'''
This function will return the list of requirements mentioned in the requirements.txt file
'''
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    return requirements

setup(
    name = 'heart-stroke-prediction',
    version = '1.0',
    author = 'Love Kumar Bansak',
    author_email = 'lovekumarsvgms@gmail.com',
    description = 'A machine learning model to predict the likelihood of a heart stroke based on user input.',
    packages = find_packages(),
    install_requires = [
        'streamlit',
        'pandas',
        'joblib',
        'scikit-learn'
    ]

)