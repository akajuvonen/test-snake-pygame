from setuptools import setup, find_packages


setup(
    name='test-snake-pygame',
    version='1.1.0',
    description='A snake-like game make using Pygame',
    author='Antti Juvonen',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['pygame'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    entry_points = {
        'console_scripts': [
            'snake-run=test_snake_pygame.game:main'
            ]
    }
)
