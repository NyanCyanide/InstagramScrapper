# Instagram Scrapper

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Usage](#usage)
    - [Running the Program](#running-the-program)
    - [CSV File Format](#csv-file-format)
4. [Important Notes](#important-notes)
5. [Contributions and Feedback](#contributions-and-feedback)
6. [License](#license)

## 1. Introduction <a name="introduction"></a>

The Instagram Follower and Following Scraper is a Python program designed to scrape follower and following data from Instagram profiles using the Selenium automation framework. This tool allows you to gather valuable information about your Instagram followers and accounts you are following, such as profile names, profile links, profile image links, blue tick presence, and follow-back status. Before using this program, please ensure that you have the necessary prerequisites in place.

## 2. Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Microsoft Edge browser
- Selenium Python package
- Microsoft Edge WebDriver

### Installation <a name="installation"></a>

Follow these steps to set up the project:

1. Clone or download this repository to your local machine.

2. Open the project directory in your terminal or command prompt.

3. Install the required packages by running:

   ```bash
   pip install -r requirements.txt
   ```

## 3. Usage <a name="usage"></a>

### Running the Program <a name="running-the-program"></a>

To use the Instagram Follower and Following Scraper, follow these steps:

1. Open the `main.py` file in a text editor.

2. Locate the following lines of code in `main.py`:

   ```python
   # Replace 'your_username' and 'your_password' with your actual Instagram credentials
   username = 'your_username'
   password = 'your_password'
   ```

3. Replace `'your_username'` and `'your_password'` with your actual Instagram username and password.

4. Save the `main.py` file after making the changes.

5. Run the program by executing the following command:

   ```bash
   python main.py
   ```

6. Wait for the program to complete the scraping process. The data will be stored in two CSV files: `followers.csv` and `following.csv`.

### CSV File Format <a name="csv-file-format"></a>

The CSV file formats remain the same as mentioned in the previous documentation:

#### followers.csv

- `Profile Name`: The name of the Instagram user.
- `Profile Link`: The link to the user's Instagram profile.
- `Profile Image Link`: The link to the user's profile image (if available). If it is "False," it means the user has an active story, and the image link cannot be retrieved.
- `Blue Tick`: Either `True` or `False` based on the presence of a blue verification tick on the account.
- `Follow Back`: `True` if you are following the user; otherwise, `False`.

#### following.csv

- `Profile Name`: The name of the Instagram user.
- `Profile Link`: The link to the user's Instagram profile.
- `Profile Image Link`: The link to the user's profile image (if available). If it is "False," it means the user has an active story, and the image link cannot be retrieved.
- `Blue Tick`: Either `True` or `False` based on the presence of a blue verification tick on the account.

## 4. Important Notes <a name="important-notes"></a>

- Avoid running this program excessively, as Instagram may temporarily block access to your account from the specific IP address.
- Be cautious about sharing your Instagram username and password in the `main.py` file.


## 5. Contributions and Feedback <a name="contributions-and-feedback"></a>

We welcome any suggestions, improvements, or bug reports from the community. Please feel free to open issues or submit pull requests on the project's [GitHub repository](#).

## 6. License <a name="license"></a>

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

**Disclaimer:** This project is for educational and informational purposes only. Use it responsibly and in compliance with Instagram's terms of service and policies.
