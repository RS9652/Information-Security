# Facebook Phishing - Educational Project

**Disclaimer**: This project is for educational and research purposes only. Unauthorized use of this tool to attack targets without prior consent is illegal. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Overview

A simple educational demonstration of how phishing attacks work, designed to raise awareness about online security. This project simulates a Facebook login page to demonstrate how phishing attempts can capture user credentials.

## Features

- Realistic Facebook login page clone
- Credential capture functionality
- Local storage of captured credentials (for educational purposes only)
- Email notification system (optional)

## Prerequisites

- Python 3.6+
- pip (Python package manager)
- Required Python packages (install via `pip install -r requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd Information-Security/phishing
   ```

2. Install the required packages:
   ```bash
   pip install flask flask-cors
   ```

## Configuration

1. For email notifications (optional), update the following in `mail.py`:
   - `sender_email`: Your Gmail address
   - `sender_password`: Your Gmail app password
   - `receiver_email`: Email to receive notifications

   Note: For Gmail, you'll need to generate an App Password if you have 2FA enabled.

## Usage

1. Start the server:
   ```bash
   python server.py
   ```

2. Open a web browser and navigate to:
   ```
   http://localhost:8000/login
   ```

3. The captured credentials will be saved to `login_data.txt`

## Security Considerations

- This tool should only be used in controlled environments for educational purposes
- Always obtain proper authorization before testing any security measures
- Never use this tool to collect actual user credentials without consent
- The project includes basic security headers and CORS policies

## Files

- `server.py` - Main Flask server handling requests
- `templates/Facebook template.html` - Phishing page template
- `static/css/login_form_2.css` - Styling for the login form
- `mail.py` - Email notification system
- `login_data.txt` - Stores captured credentials (created on first run)

## Educational Purpose

This project is designed to:
- Demonstrate how phishing attacks work
- Show the importance of verifying website URLs
- Teach about web security best practices
- Help security professionals understand attack vectors

## Legal and Ethical Use

By using this software, you agree to use it only for legal and ethical purposes, including:
- Security research
- Educational demonstrations
- Authorized penetration testing

## Author

Syimyk Rasulov
