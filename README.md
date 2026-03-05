# Quick-Calc

Quick-Calc is a simple calculator application that supports addition, subtraction, multiplication, and division.

## Setup
Install dependencies:

pip install -r requirements.txt

## Run Application
python main.py

## Run Tests
python -m pytest

## Testing Framework Research
This project uses Pytest as the testing framework. Pytest provides simple syntax and automatic test discovery, making it easier to write and maintain tests compared to Python’s built-in Unittest framework.
## Testing Framework Comparison

Two common Python testing frameworks are Pytest and Unittest.

Unittest is the built-in testing framework in Python and follows the xUnit testing style. However, it often requires more boilerplate code and setup.

Pytest is more flexible and easier to use. It provides automatic test discovery, simple assertions, and powerful fixtures.

For this project, Pytest was chosen because it allows writing clean and readable tests with minimal configuration.