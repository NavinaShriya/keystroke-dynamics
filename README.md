# Keystroke Behavioral Authentication System

A beginner-friendly Python application that analyzes typing behavior and compares a user's typing pattern with a saved behavioral profile.

## Overview

This project explores keystroke dynamics by measuring typing time and using it to create a simple behavioral profile.

The system collects typing samples, calculates basic statistical features, and compares a new typing attempt with the saved profile.

## Features

- Collects multiple typing samples
- Measures typing time
- Creates a personal typing profile
- Calculates average typing time
- Calculates minimum and maximum typing time
- Calculates standard deviation
- Stores typing data in CSV format
- Tests new typing attempts
- Performs a simple behavioral comparison
- Provides an authentication result

## Technologies

- Python
- CSV
- Statistics
- Basic behavioral biometrics

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
└── main.py
