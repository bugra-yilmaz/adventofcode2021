from setuptools import setup

setup(
    name="aoc-helper",
    version="1.0.0",
    py_modules="helper",
    entry_points={"console_scripts": ["aoc-download-input=helper:download_input_for_current_day",
                                      "aoc-submit-solution=helper:submit_solution_for_current_day",
                                      "aoc-prepare=helper:prepare_question_for_current_day"]}
)
