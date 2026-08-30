# Keystroke Behavioral Authentication System

A beginner-friendly Python application that analyzes typing behavior and uses keystroke timing patterns for basic behavioral authentication.

## Overview

Keystroke dynamics is a behavioral biometric technique that studies the way a person types.

This project creates a basic typing profile from typing samples and compares a new typing attempt against that profile.

The system analyzes:

- Total typing time
- Key hold time
- Flight time between keystrokes
- Typing speed
- Typing-time variation

## Features

- Collects multiple typing samples
- Creates a typing profile
- Stores typing measurements in CSV format
- Measures total typing time
- Measures average key hold time
- Measures average flight time
- Calculates typing speed
- Calculates basic typing-time statistics
- Compares a new typing attempt with the saved profile
- Provides an authentication result
- Includes a graphical typing-test interface

## Technologies

- Python 3
- Tkinter
- CSV
- Statistics
- Behavioral Biometrics

## How It Works

```text
              Typing Samples
                    |
                    v
             Typing Profile
                    |
                    v
          Statistical Analysis
                    |
                    v
          New Typing Attempt
                    |
                    v
           Keystroke Capture
                    |
          +---------+---------+
          |                   |
          v                   v
      Hold Time         Flight Time
          |                   |
          +---------+---------+
                    |
                    v
             Typing Time
                    |
                    v
             Typing Speed
                    |
                    v
           Profile Comparison
                    |
             +------+------+
             |             |
             v             v
          Similar       Different
             |             |
             v             v
      AUTHENTICATED   NOT AUTHENTICATED
