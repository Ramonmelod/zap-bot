# Zap-Bot

Zap-Bot is an automated bot for zap management

## Features

- **login**: login in the zap page.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ramonmelod/zap-bot.git
   ```

## Setting a virtual environment for python

- To set a virtual environment for python run the command:

```sh
  python -m venv virtual_env
```

then:

```sh
  source virtual_env/bin/activate
```

```sh
sudo apt install chromium-chromedriver

```

## Installing the _chromium-browser_ and the _chromium-chromedriver_

- For this project you need to install the dependecies `chromium-browser` and the `chromium-chromedriver`

```sh
  sudo apt install chromium-browser chromium-chromedriver

```

## Using the chromium in the terminal in headless mode

- below is a command the shows how to use the chromium in the headless mode in the linux terminal:

```sh
chromium --headless --disable-gpu --dump-dom https://www.ramonmelo.com.br --screeshot

```
