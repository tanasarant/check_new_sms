# SMS Router Checker

A small Python project that automates checking for new SMS messages from a 4G modem router.  
The project retrieves unread messages via the router’s web UI, stores them in SQLite, and prints them out for easy monitoring.

## Project Structure
- **session_id.py** → Collects session ID from router web UI using Selenium.
- **check_new_sms.py** → Uses session ID, router URL, cookies, and headers to fetch SMS messages (JSON).
- **convert_to_sqlite3.py** → Converts JSON data into `sms.db` (SQLite3 format).
- **print_out.py** → Queries `sms.db` and prints unread SMS to the screen.

## Usage
1. Run `session_id.py` to obtain session cookies.
2. Call `check_new_sms.py` with:
   - `ROUTER_URL` (constant)
   - `COOKIES` (from session_id.py)
   - `HEADER` (constant JSON)
3. Convert JSON to SQLite using `convert_to_sqlite3.py`.
4. Print unread SMS with `print_out.py`.

## Notes
- **Do not commit `router_credential.py`** (contains router username/password).  
- Add `router_credential.py` to `.gitignore` for security.  
- Modular design allows easy extension (e.g., switching databases or integrating with monitoring tools).

## License
This project is shared for hobbyist and educational use.  
Feel free to adapt and extend it for your own setups.
