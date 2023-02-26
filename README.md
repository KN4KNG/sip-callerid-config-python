
# SIP Caller ID Configuration with Python

This is a simple Python script that demonstrates how to configure a SIP phone service with a custom caller ID using a Raspberry Pi and the Asterisk software. The script updates the SIP credentials and sets the caller ID in the configuration file of Asterisk, allowing you to use your personal phone number as the caller ID for outgoing calls.

## Prerequisites

Before using this script, you need to have the following:

-   A Raspberry Pi with Raspbian or a compatible operating system installed
-   A SIP phone service with a phone number associated with it
-   The Asterisk software installed on the Raspberry Pi (you can use the `apt-get` package manager to install it)
-   Python 3 installed on the Raspberry Pi (you can use the `apt-get` package manager to install it)

## Usage

To use this script, follow these steps:

1.  Clone this repository to your Raspberry Pi or download the `sip_caller_id.py` file.
2.  Open the `sip_caller_id.py` file with a text editor and replace the placeholders in the `caller_id`, `sip_username`, `sip_password`, and `sip_server` variables with your actual values. Save the file.
3.  Open a terminal window on your Raspberry Pi and navigate to the directory where the `sip_caller_id.py` file is located.
4.  Run the following command to execute the script:

Copy code

`sudo python3 sip_caller_id.py` 

5.  Verify that the script has successfully updated the SIP credentials and set the caller ID by checking the `/etc/asterisk/sip.conf` file. You should see your phone number in the `callerid` field.

## Notes

-   This script is just a proof of concept and may not work with all SIP phone services or configurations. Make sure to test it thoroughly and consult the documentation of your service before using it in production.
-   Running the script with `sudo` privileges is necessary because it needs to modify system files.
-   The script uses the `os` module to execute terminal commands, which may not work on all operating systems or configurations.
-   You can customize the script to your needs by modifying the values of the `caller_id`, `sip_username`, `sip_password`, and `sip_server` variables or by using a different approach to configure the SIP phone service.
