# Zap-Bot

Zap-Bot is an automated bot for zap management

## Used technologies

<div style="display: flex; align-items: center;">
  <img src="https://user-images.githubusercontent.com/25181517/184103699-d1b83c07-2d83-4d99-9a1e-83bd89e08117.png"  style="width: 100px; height: auto; margin: 0 25px">
  <img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" style="width: 100px; height: auto; margin: 0 25px;">
</div>

## Features

- **login**: login in the zap page.
- **Update**: Update the adds in zap

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
