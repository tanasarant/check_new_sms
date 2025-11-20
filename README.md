# SMS Router Checker

A small Python project that checks new unread SMS messages from a 4G modem router (Tenda 4G680)   
The project retrieves unread messages via the router’s web UI, stores them in SQLite, and prints them out for easy monitoring.

## Project Structure
- **session_id.py** → Collects session ID from router web UI using Python Selenium & geckodriver
- **check_new_sms.py** → Uses session ID, router URL, cookies, and headers to fetch SMS messages (JSON).
- **convert_to_sqlite3.py** → Converts JSON data, which is all SMS in the modem, into `messages.db` (SQLite3 format).
- **print_out.py** → Queries `messages.db` for the unread SMS to the screen.

## Usage
1. git clone this repository to your local. 
2. RUN "pip install -r `requirements.txt`"
3. PUT GECKODRIVER on /usr/local/bin directory (geckodriver v0.36.0-linux64)
4. PREPARE `router_credential.py` file which have 2 lines:
   - ROUTER_USERNAME = 'admin'
   - ROUTER_PASSWORD = 'your-4G680-router-passwd'
5. execute `print_out.py` python script to print the new incoming SMS.

## Applicable equipment 
Tested with Tenda 4G680 4G Mifi Modem Router. FW V 2.0.6Tai 
Can check new incoming SMS, so OTP or important SMS will not be missed out. 

## Notes
- **Do not commit `router_credential.py`** (contains router username/password).  
- Add `router_credential.py` to `.gitignore` for security.  
- Modular design allows easy extension (e.g., switching databases or integrating with monitoring tools).

## License
This project is shared for hobbyist and educational use.  
Feel free to adapt and extend it for your own setups.
If you want this software, for your own router model. Feel free to let me know. 
