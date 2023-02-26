import os

caller_id = "your_caller_id"  # your phone number
sip_username = "your_sip_username"
sip_password = "your_sip_password"
sip_server = "your_sip_server_address"

# set the SIP credentials
os.system(f"sudo sed -i 's/username=.*/username={sip_username}/g' /etc/asterisk/sip.conf")
os.system(f"sudo sed -i 's/secret=.*/secret={sip_password}/g' /etc/asterisk/sip.conf")
os.system(f"sudo sed -i 's/fromuser=.*/fromuser={sip_username}/g' /etc/asterisk/sip.conf")
os.system(f"sudo sed -i 's/fromdomain=.*/fromdomain={sip_server}/g' /etc/asterisk/sip.conf")
os.system(f"sudo sed -i 's/host=.*/host={sip_server}/g' /etc/asterisk/sip.conf")

# set the caller ID
os.system(f"sudo sed -i 's/callerid=.*/callerid={caller_id}/g' /etc/asterisk/sip.conf")
