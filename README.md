# Keystroke Behavioral Authentication System

A beginner-friendly Python application that analyzes typing behavior and uses keystroke timing patterns for basic behavioral authentication.

## Overview

Keystroke dynamics is a behavioral biometric technique that studies the way a person types.

This project creates a basic typing profile and compares a new typing attempt against that profile.

The system currently analyzes:

- Total typing time
- Key hold time
- Flight time between keystrokes
- Typing-time variation

## Features

- Collects multiple typing samples
- Creates a personal typing profile
- Stores typing measurements in CSV format
- Measures total typing time
- Measures average key hold time
- Measures average flight time
- Calculates typing-time statistics
- Compares a new typing attempt with the saved profile
- Provides a basic authentication result

## Technologies

- Python
- Tkinter
- CSV
- Statistics
- Behavioral Biometrics

## Project Structure

```text
keystroke-dynamics/
│
├── data/
│   ├── sample_typing_data.csv
│   └── typing_profile.csv
│
├── README.md
├── keystroke_auth.py
├── authenticate.py
├── typing_test.py
├── keystroke_features.py
├── keystroke_capture.py
├── main.py
├── requirements.txt
└── .gitignore
