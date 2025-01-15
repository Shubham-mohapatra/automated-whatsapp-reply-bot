# Automated WhatsApp Reply Bot

A Selenium-based Python bot that automatically replies to unread messages on WhatsApp Web. The bot monitors specified contacts and sends a predefined or randomly chosen automated response.

## Features

- Automatically detects unread messages.
- Sends customized auto-replies to predefined contacts.
- Reads contact list and message templates from a configuration file (`config.json`).
- Includes retry logic for transient errors.
- Logs all activities for tracking and debugging.
- Avoids being flagged by implementing random delays between actions.
- Supports multiple message templates for variety.
- Easily configurable via JSON files.

## Requirements

1. Python 3.8 or above
2. Google Chrome (latest version)
3. ChromeDriver (compatible with your Chrome version)
4. Required Python libraries:
   - selenium
   - json
   - random
   - logging

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/automated-whatsapp-reply-bot.git
   cd automated-whatsapp-reply-bot
