# 🔐 Random Password Generator

A simple, interactive command-line password generator built with Python.

## Features

- Choose your password length (8–64 characters)
- Toggle uppercase letters, numbers, and symbols
- Live password strength indicator (Weak → Very Strong)
- One-click copy to clipboard

## Demo

```
=============================================
      🔐 Random Password Generator
=============================================

Enter password length (8–64) [default: 16]: 20

Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols (!@#$...)? (y/n): y

=============================================
  Generated Password:

    tX#9mK@2wLp$5rN!dQ7v

  Strength : 🔒 Very Strong
  Length   : 20 characters
=============================================

Copy password to clipboard? (y/n): y
  ✅ Password copied to clipboard!

Stay safe! 🛡️
```

## Getting Started

### Prerequisites

- Python 3.7+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/megnabadal/password-generator.git
   cd password-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run

```bash
python main.py
```

## Project Structure

```
password-generator/
│
├── main.py           # Main script
├── requirements.txt  # Dependencies
└── README.md         # You're reading it!
```

## License

This project is open source and available under the [MIT License](LICENSE).
