# A DAG of Domain Names found in BlueSky Handles

<img src="https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:i6misxex577k4q6o7gloen4s/bafkreibp3qhj3vym52kxbihn546w3nssxej2yyicejisv4aq3rlgqxwsqq@jpeg" width="512" alt="A directed acyclic graph. It looks like a constellation of stars">

Instructions:

1. Run `python get-domains.py`
    * Leave it running for however long you like.
    * It will generate a file called `domains.txt`
1. Run `python reverse-dns-to-csv.py`
    * It will generate a file called `domains.csv`
1. Start a webserver with `python -m http.server`
    * It will tell you the default IP and port
1. Open a Web browser and visit http://0.0.0.0/8000/view.html
    * If the preview step gives you different values, use those

##  Requirements

`pip install atproto`