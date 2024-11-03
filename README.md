# Hotkey Listener & JAR Launcher

This project is a Python-based utility that listens for a custom hotkey combination to execute a JAR launcher. The JAR launcher allows the user to specify a directory, scan for `.jar` files, and select one to execute. Additionally, the project includes setup and stop scripts for starting and stopping the listener, as well as a configuration script to customize the hotkey.

## Project Structure

The project contains the following main components:

1. **Hotkey Listener**: A script that continuously listens for a specified hotkey combination, stored in `config.txt`.
2. **JAR Launcher**: Activated by the hotkey listener, this script scans a directory for `.jar` files and allows the user to select one for execution.
3. **Hotkey Configuration**: A script that allows users to modify the hotkey combination stored in `config.txt`, with validation to prevent invalid combinations.
4. **Setup & Stop Scripts**: Batch scripts that start and stop the listener script, ensuring precise control over the listener process without affecting other Python processes.
5. **Requirements**: A `requirements.txt` file for easy installation of dependencies.

---

## Files Overview

| File                  | Description                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------|
| `start.bat`           | Starts `listener.py` globally, saves the process ID in `process_id.txt`, and initiates logging. |
| `listener.py`         | Listens for the specified hotkey in `config.txt`. When detected, it executes `jar_launcher.py`.|
| `jar_launcher.py`     | Prompts the user for a directory path, scans for `.jar` files, and lets the user select one to run. |
| `set_hotkey.py`       | Allows the user to change the hotkey combination in `config.txt`, validating the combination. |
| `stop.bat`            | Stops `listener.py` by using the ID from `process_id.txt`, ensuring no other Python processes are terminated. |
| `requirements.txt`    | Contains the required dependencies for running the project. Install with `pip install -r requirements.txt`. |

## Technologies Used
- Python
- keyboard

## Requirements
- Python 3.x
  - If you don’t have Python, download it from: [Python Download](https://www.python.org/downloads/)

---

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/RegreDanger/jar-launcher.git
2. **Navigate to the Project Directory**:
   - Open your command prompt (cmd) and navigate to the project folder:
     ```
     cd C:\Users\User\YourFolder\data-analysis-tool
     ```
3. **Install Dependencies**:
   - Execute the following command to install required libraries:
     ```
     pip install -r requirements.txt
     ```
3. **Configure the Hotkey**:
   - Run `set_hotkey.py` to set a custom hotkey combination.
   - The combination will be saved to `config.txt`.

----

## Usage
1. **Start the Listener**:
   - Run `start.bat` to initialize `listener.py`.
   - The listener script will store its process ID in `process_id.txt` and begin logging.
   - Once started, `listener.py` will wait for the hotkey specified in `config.txt`.
2. **Execute the JAR Launcher**:
   - Press the configured hotkey combination to activate `jar_launcher.py`.
   - Enter a directory path when prompted, and `jar_launcher.py` will scan for .jar files.
   - Select a .jar file from the list to execute it.
3. **Configuring the Hotkey**:
   - To set a custom hotkey, run:
     `python set_hotkey.py`
   - This script will guide you through setting a valid key combination, updating config.txt with the new hotkey.
3. **Stop the Listener**:
   - Run stop.bat to stop `listener.py` by terminating the process using the ID saved in `process_id.txt`.
