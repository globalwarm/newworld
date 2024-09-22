Google Form Bot

This Python script automates the filling and submission of a Google Form. It uses Selenium WebDriver to interact with the form elements and simulate user input.

Features

    Fills out various question types in the Google Form (multiple choice, text input, etc.)
    Randomly selects answers based on weighted probabilities to mimic realistic responses
    Supports multiple languages
    Handles form navigation (moving between pages)
    Includes time delays between submissions to avoid detection
    Option to specify a specific country or select one randomly
    Allows setting the number of form submissions

Setup

    Prerequisites
        Python 3.x
        Selenium WebDriver
        Chrome browser
        Chromedriver (make sure it's in your PATH or provide the path in the script)

    Installation
    Bash

    pip install selenium webdriver-manager 

    Use code with caution.

    Configuration
        Replace the placeholder self.link with the actual URL of your Google Form.
        Adjust the weighted probabilities in the code to match your desired response distribution.
        Set the country_code if you want to target a specific country, or leave it as None for random selection.
        Modify the time variable to control the delay between submissions (in seconds).
        Update the nof (number of form submissions) as needed.

Usage

    Make sure you have Chrome and Chromedriver installed.

    Run the script:
    Bash

    python your_script_name.py

    Use code with caution.

Disclaimer

    Use this script responsibly and ethically.
    Avoid overloading the Google Form with excessive submissions.
    Be aware that automated form filling might be against the terms of service of some platforms.

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

License

This project is licensed under the MIT License.  

Additional Notes for the README

    You might want to add a section explaining the purpose of the form filling (e.g., for research, testing, etc.)
    If there are specific instructions or limitations for the form, mention them in the README
    Consider adding error handling to the code and documenting it in the README
    Include any relevant credits or references if you used external resources
