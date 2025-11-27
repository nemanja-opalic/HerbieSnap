# HerbieSnap

## 📌 Introduction

**HerbieSnap**, @HerbieSnap@mastodon.social, is a Python-based automation tool that listens to mentions on a Mastodon account, verifies whether the user mentioning the account is a follower, and automatically takes a screenshot of the replied-to toot (if available). The screenshot is then sent back to the user as a direct reply.

The bot uses:
- **Mastodon.py** – for connecting to Mastodon API and streaming notifications in real time.

- **Playwright** – for rendering Mastodon toots in a headless browser and capturing screenshots.

- **Python standard libraries** – for time management and environment variable handling.



## ⚙️ Features

- **Real-time mention detection**: Listens to all notifications and triggers only on mentions.

- **Follower verification**: Ensures only followers can trigger screenshot responses.

- **Screenshot generation**: Captures a screenshot of the parent toot in a headless Chromium browser using Playwright.

- **Automated reply**: Posts the screenshot as a direct reply to the mentioning user.

- **Duplicate handling**: Prevents multiple responses to the same mention using an in-memory set.

## 📝 Installation
### 1️⃣ Prerequisites

- Python 3.10+
- Node.js (required for Playwright)
- Browser binaries installed for Playwright:
```
playwright install

```
### 2️⃣ Python Dependencies

Install Python packages using ```pip```:
```
pip install requirements.txt
```
### 3️⃣ Environment Variables

Set the following environment variables:
```
export MASTODON_ACCESS_TOKEN="your_access_token_here"
export MASTODON_BASE_URL="https://mastodon.instance.url"

```
### Usage

 1. Save the script as bot.py.

 2. Run the bot: 
 ```python bot.py```

 3. The bot will continuously listen for mentions and automatically reply with screenshots if the mentioned toot is a reply and the user is a follower.


## ⚡ Example Workflow

- User mentions the bot:
- @bot_user Can you show the original toot?

- Bot checks if user is a follower → Yes.

- Bot fetches the parent toot URL.

- Bot launches headless Chromium → navigates to the parent toot.

- Bot takes a screenshot of the toot.

- Bot posts a direct reply with the screenshot attached.
