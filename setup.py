from setuptools import setup, find_packages

setup(
    name="math_quiz",
    author="MD Mahmudul Hasan",
    description="A simple math quiz application",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",
        ],
    }

)
