# Aternos Discord Bot

A simple Discord bot that lets users start and stop an Aternos Minecraft server using commands like `?server_start` and `?server_stop`.

> ⚠️ **Warning: Using unofficial methods to control Aternos may violate their Terms of Service and result in account suspension or ban. Use this tool at your own risk.**

---

## 🔧 Features

- ✅ Start and stop your Aternos server from Discord
- ✅ Server status detection using `mcstatus`
- ✅ Beautiful Discord embed messages
- ✅ Easy to configure and extend
- ⚠️ Runs using the `python_aternos` unofficial API wrapper

---

## ⚠️ Disclaimer

This bot uses **unofficial** methods (reverse-engineering) to interact with the Aternos platform via the `python_aternos` library.  
Aternos **does not offer a public API**, and they may ban accounts that use automated tools.

> **Use this bot at your own risk.**  
> This project is for educational and personal-use purposes only.

---

## 🔧 Requirements

- Python 3.8+
- Dependencies:
  - `discord.py`
  - `python_aternos`
  - `mcstatus`

Install them with:

```bash
pip install -r requirements.txt
