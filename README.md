SnapGet
=======

SnapGet is a command-line tool for retrieving Wayback Machine snapshots of a list of URLs and outputting the source code of each unique snapshot. With concurrency and web scraping, SnapGet can quickly retrieve a large number of snapshots and highlight differences between them with colorama. Whether you're a web developer, a researcher, or just curious about a website's history, SnapGet is a powerful tool for exploring the past.

Features
--------

-   Retrieve all available Wayback Machine snapshots of a list of URLs
-   Output the source code of each unique snapshot with colorama highlighting
-   Use concurrency to speed up the retrieval of snapshots
-   Use web scraping to extract the source code of each snapshot

Installation
------------

1.  Clone the repository:

    `git clone https://github.com/yourusername/snapget.git`

2.  Install the dependencies:

    `cd snapget
    pip install -r requirements.txt`

Usage
-----

To retrieve snapshots of a list of URLs:

`python snapget.py -u urls.txt`

where `urls.txt` is a file containing a list of URLs, one per line.

To retrieve snapshots of URLs piped via stdin:

`cat urls.txt | python snapget.py`

Options
-------

-   `-u`, `--urls-file`: file containing list of URLs (default: read from stdin)
