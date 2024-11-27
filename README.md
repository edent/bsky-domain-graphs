# An Interactive DAG of Domain Names used as BlueSky Handles

<a href="https://edent.github.io/bsky-domain-graphs/view.html"><img src="https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:i6misxex577k4q6o7gloen4s/bafkreibp3qhj3vym52kxbihn546w3nssxej2yyicejisv4aq3rlgqxwsqq@jpeg" width="512" alt="A directed acyclic graph. It looks like a constellation of stars"></a>

* [Play with the 3D demo](https://edent.github.io/bsky-domain-graphs/view.html)
* [View the TreeMap](https://edent.github.io/bsky-domain-graphs/treemap.html)
* [Explore the Public Suffixes](https://edent.github.io/bsky-domain-graphs/public-suffix.html)

## Instructions

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

## Background

As part of my [MSc Dissertation](https://shkspr.mobi/blog/2023/04/msc-dissertation-exploring-the-visualisation-of-hierarchical-cybersecurity-data-within-the-metaverse/) I investigated using interactive 3D Directed Acyclic Graphs to explore domain name data.

BlueSky users can set their usernames to be their verified domain name.

So I've applied the same techniques to visualise how BSky's usernames are distributed.

In November 2024, I spent several days sampling their AT Protocol Firehose. I gathered 22,410 unique domain usernames and processed them into this graph.

I don't claim this to be a fully representative sample - but I couldn't be bothered running the process for ages. So you get what you get.