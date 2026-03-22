""" cacher.py -- sample for playlist download
"""

import sys
import requests
from urllib.parse import urlparse


def main():
    do_script(sys.argv[1:])


def do_script(args):
    param = args
    print("REQUESTS:", requests.__file__ is not None)
    a_id = param[0]
    run_script(a_id)


def run_script(a_id):
    url = f"https://www.deezer.com/us/playlist/{a_id}"
    print("Getting:", url)
    dump_url_content(url)


def dump_url_content(url: str):
    """ Extract the suffix from the URL path """
    parsed = urlparse(url)
    suffix = parsed.path.rstrip("/").split("/")[-1]
    if not suffix:
        raise ValueError("Could not extract a valid suffix from the URL.")
    # Build the output filename
    filename = f"{suffix}.raw"
    print(f"Using suffix: {suffix}")
    print(f"Output file: {filename}")
    # Perform the HTTP GET request
    response = requests.get(url)
    print(f"HTTP status: {response.status_code}")
    # Write the raw content to the file
    with open(filename, "wb") as fdout:
        fdout.write(response.content)
    return response, f"Content written to {filename}"


# Example usage
if __name__ == "__main__":
    main()
