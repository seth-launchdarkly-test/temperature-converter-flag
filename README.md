# Temperature Converter with Feature Flag

This project is a simple temperature converter (Fahrenheit to Celsius) with a feature flag capability using LaunchDarkly. The flag controls whether the result text changes color based on temperature.

## Requirements

- Python 3.XX+
- LaunchDarkly Account (for setting up a feature flag)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/seth-launchdarkly-test/temperature-converter-flag.git
cd temperature-converter-flag


2. **Install Dependencies**:
    Use a virtual environment.
    Create and activate a virtual environment in Terminal:
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install the Required Packages:
    pip install -r requirements.txt

3. **Set Up LaunchDarkly**:

    Sign up or log in to your LaunchDarkly account.
    Create a new project and an environment (e.g., "Test").
    Create a feature flag called temperature-converter.
    Go to Account Settings > Projects > Your Project > SDK Keys and copy the SDK key for the appropriate environment.

4. **Configure the SDK Key**:
    In the Terminal, set the SDK key as an environment variable:
    export LAUNCHDARKLY_SDK_KEY=your_sdk_key_here

5. **Run the Application**:
    python3 main.py

   **Usage**
    The app will evaluate the temperature-converter feature flag.
    When the flag is on, text will change color:
      -Blue for temperatures ≤ 32°F.
      -Red for temperatures > 32°F.
    When the flag is off, the text remains black.

    **Troubleshooting**
    If you encounter an error saying "SDK failed to initialize," please ensure:

    The SDK key is correctly set and matches the LaunchDarkly environment.
    You have a stable internet connection to connect to LaunchDarkly's servers.
    Additional Notes
    To turn the flag on/off manually, use the LaunchDarkly dashboard or their REST API for quick toggling.
