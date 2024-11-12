# Robo-Speaker - Text-to-Speech Conversion Service

This is a simple Python-based Text-to-Speech Conversion Service that allows users to convert text into speech using a male or female voice option.

## Project Overview

This project uses the `pyttsx3` library to generate speech from text input. Users can choose between a male (Bob) or female (Alice) voice agent for a more customized experience.

## Prerequisites

1. **Python 3.6 or higher**: Ensure you have Python installed on your system.
2. **`pyttsx3` library**: This library is used to convert text to speech.

## Getting Started

### 1. Installing Python

If you haven't installed Python on your local machine, follow these steps:

- Go to the [Python website](https://www.python.org/downloads/).
- Download the installer for your operating system.
- Run the installer and check the box to add Python to your PATH before clicking "Install Now."
- Verify the installation by opening a terminal (or command prompt) and typing:

```bash
python --version
```
You should see the Python version displayed.

### 2. Setting Up the Project

**Step 1: Clone the Repository (optional)**

If you're downloading the code directly, skip this step. Otherwise, clone the repository with:

```bash
git clone <repository-url>
```

**Step 2: Install Required Python Libraries**

Open a terminal, navigate to the project directory, and install the required libraries with:

```bash
pip install pyttsx3
```

**Step 3: Run the Application**

Now, run the Python script using:

```bash
python main.py
```

## Usage : 
1) The application will display a welcome message:
`Welcome to the Text-to-Speech Conversion Service.`

2) Choose a voice by entering:
- `0` for a male voice (Bob)
- `1` for a female voice (Alice)

3) Enter any text you want to convert to speech.

4) To exit, type `q`.

### Example Interaction : 
```bash
Welcome to the Text-to-Speech Conversion Service.
Enter '0' for male voice agent or '1' for female voice agent: 0
Me: Hello, how are you?
Bob: .....
Me: q
```