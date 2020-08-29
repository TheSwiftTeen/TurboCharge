from setuptools import setup

setup(
    name = 'Speed',
    version = '1.0',
    description= 'Simple And Speedy Way To Install All The Packages You Love!',
    author = 'TheBossProSniper',
    author_email = 'tejas.ravishankar0526@gmail.com',
    py_modules=['speed'],
    install_requires = [
        'Click',
        'progress',
    ],
    entry_points = 
    '''
        [console_scripts]
        speed=speed:cli
    '''
)
