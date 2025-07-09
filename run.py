import pytest
from framework import allure_generator

if __name__ == "__main__":

    pytest.main()

    allure_generator.report_generator()