# MAC Address Vendor Lookup

This is a simple Python script to look up the vendor of a list of MAC addresses using the [macvendors.com API](https://macvendors.com/).

## Overview

The script reads a list of MAC addresses from a specified file, queries the API for each address, and prints the corresponding vendor name to the console.

## Prerequisites

Before running the script, you need to install the `requests` library. You can install it using `pip`:

```
pip install requests
```

## Setup

1.  **Create a MAC address file:** Create a text file named `macs.txt` in the same directory as the script.

2.  **Add MAC addresses:** Add your MAC addresses to the `macs.txt` file, one per line. The format can be with or without colons (e.g., `00:1A:2B:3C:4D:5E` or `001A2B3C4D5E`).

    **Example `macs.txt`:**

    ```
    00:1A:2B:3C:4D:5E
    AA:BB:CC:DD:EE:FF
    ```

3.  **Update the script path:** Open the Python script and change the `path` variable to the correct location of your `macs.txt` file. For example:

    ```
    path = "/path/to/your/macs.txt"
    ```

    Note: The original script uses a specific path: `/home/ash27kan/Desktop/macs.txt`. Make sure to update this if your file is in a different location.

## Usage

To run the script, simply execute it from your terminal:

```
python your_script_name.py
```

The script will then print the MAC address and its corresponding vendor, one by one. There is a 1-second delay between each request to avoid overloading the API.

## Code Breakdown

  * `loader(path)`: This function reads the `macs.txt` file and returns a list of MAC addresses.
  * `finder(mac)`: This function sends a GET request to the macvendors.com API for a single MAC address and returns the vendor name.
  * `printer(macs)`: This function iterates through the list of MAC addresses, calls `finder` for each one, and prints the result to the console. It includes a `time.sleep(1)` to pause for one second between requests.
  * `main()`: This is the main function that orchestrates the entire process.
  * `if __name__ == "__main__":`: This standard Python block ensures that the `main()` function is called when the script is executed directly.
