# Automated Wireshark Capture Script

This repository contains a Python script that automates Wireshark captures using the PyShark library. The script captures network traffic and saves it to a pcapng file for further analysis.

## About

Wireshark is a powerful network protocol analyzer that allows users to capture and analyze network traffic. This script provides a convenient way to automate the capture process using Python and the PyShark library.

## Usage

To use this script, follow these steps:

1. Install Wireshark: Make sure you have Wireshark installed on your system. You can download it from the official website: [wireshark.org](https://www.wireshark.org/).

2. Install PyShark: Install the PyShark library by running the following command:

   ```shell
   pip install pyshark
   ```

3. Run the Script: Execute the Python script in your preferred Python environment. The script will start capturing network traffic and save it to a pcapng file. The default capture duration is 3600 seconds (1 hour), but you can modify it as needed.

   ```shell
   python wireshark_capture.py
   ```

4. Analyze the Capture: Once the capture is complete, you can open the generated pcapng file in Wireshark for analysis. Use Wireshark's powerful features to dissect and interpret the captured network traffic.

## Contributing

This project is open source, and contributions from the community are welcome. If you have any improvements, bug fixes, or new features to add, please feel free to fork the repository, make your changes, and submit a pull request. Together, we can enhance the functionality and usability of this automated Wireshark capture script.

If you encounter any issues or have suggestions for improvements, please open an issue on the repository's issue tracker. Your feedback is valuable and helps us make the script better for everyone.

Happy capturing and analyzing network traffic!
