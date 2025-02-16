#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import NewsProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'date': str(datetime.now()),
    }

    inputs_array = [
        {
            'topic': 'Facts about World',
            'date': str(datetime.now()),
        },
        {
            'topic': 'Artificial Intelligence',
            'date': str(datetime.now()),
        },
        {
            'topic': 'Machine Learning',
            'date': str(datetime.now()),   
        }
    ]
    
    try:
        NewsProject().crew().kickoff_for_each(inputs=inputs_array)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()

