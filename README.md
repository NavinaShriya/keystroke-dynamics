# Keystroke Behavioral Authentication System

A beginner-friendly Python application that analyzes typing patterns and detects unusual changes in typing behavior.

## Technologies

Python | Behavioral Biometrics | Anomaly Detection

## Features

- Behavioral authentication using keystroke dynamics
- Hold-time and flight-time feature extraction
- User behavioral data processing
- Simple baseline comparison
- Anomaly detection based on typing patterns

## How It Works

The user types a fixed phrase several times during training.

The program measures timing features such as:

- Dwell time — how long a key is held
- Flight time — time between keystrokes
- Typing speed

These measurements are used to create a basic behavioral profile.

A later typing attempt is compared with this profile to determine whether the typing pattern is similar or significantly different.

## Project Status

Beginner implementation in progress.

## Future Improvements

- Store anonymized user profiles
- Add more behavioral features
- Improve anomaly scoring
- Add machine-learning classification
- Evaluate false acceptance and false rejection rates
