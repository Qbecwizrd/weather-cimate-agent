# climate_agent/ingest.py

import os
import feedparser
import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader
from climate_agent.config import SOURCE_URLS, RAW_DATA_PATH
from climate_agent.utils import save_documents


def fetch_rss_links(rss_url):
    """Parses RSS feed and returns list of article links."""
    feed = feedparser.parse(rss_url)
    return [entry.link for entry in feed.entries]


def ingest_documents(urls = SOURCE_URLS):
    all_docs = []

    for url in SOURCE_URLS:
        try:
            if url.endswith(".xml") or "feed" in url:
                links = fetch_rss_links(url)
                print(f"[🔗] RSS feed: {url} → {len(links)} articles")

                for link in links:
                    loader = WebBaseLoader(link)
                    docs = loader.load()
                    all_docs.extend(docs)

            else:
                loader = WebBaseLoader(url)
                docs = loader.load()
                all_docs.extend(docs)

            print(f"[✅] Loaded {len(docs)} docs from: {url}")

        except Exception as e:
            print(f"[⚠️] Failed to load from {url}: {e}")

    save_documents(all_docs, RAW_DATA_PATH)
    print(f"\n[📦] Total documents saved: {len(all_docs)}")

    return all_docs
