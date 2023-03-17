import sys
import argparse
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from colorama import init, Fore, Style

init()  # initialize colorama

def get_snapshots(url):
    """Retrieves all available Wayback Machine snapshots for a given URL."""
    snapshots = set()  # set of unique snapshots
    parsed_url = urlparse(url)
    wayback_url = f"http://web.archive.org/cdx/search/cdx?url={parsed_url.netloc}%2F{parsed_url.path}&output=json&fl=timestamp"
    response = requests.get(wayback_url)
    if response.ok:
        for timestamp in response.json()[1:]:
            snapshot_url = f"http://web.archive.org/web/{timestamp[0]}if_/{url}"
            snapshots.add(snapshot_url)
    return snapshots

def get_source_code(snapshot_url):
    """Retrieves the source code of a given Wayback Machine snapshot."""
    response = requests.get(snapshot_url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.prettify()
    return ""

def main():
    parser = argparse.ArgumentParser(description="Retrieve Wayback Machine snapshots and output source code.")
    parser.add_argument("-u", "--urls-file", help="file containing list of URLs")
    args = parser.parse_args()

    urls = []  # list of URLs to process
    if args.urls_file:
        with open(args.urls_file) as f:
            urls = [line.strip() for line in f]
    else:
        urls = [line.strip() for line in sys.stdin]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_snapshot = {executor.submit(get_snapshots, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_snapshot):
            url = future_to_snapshot[future]
            snapshots = future.result()
            for snapshot in snapshots:
                future_to_code = executor.submit(get_source_code, snapshot)
                code = future_to_code.result()
                if code:
                    print(Fore.GREEN + f"{url} ({snapshot}):" + Style.RESET_ALL)
                    print(code)

if __name__ == "__main__":
    main()
