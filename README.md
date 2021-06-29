# JetBot

<!--[<img src="https://img.shields.io/discord/553852754058280961.svg">](https://discord.gg/Ady6NtF) -->

> Looking for a quick way to get started with JetBot?  Many third party kits are [now available](../../wiki/third-party-kits)!

<img src="../..//wiki/images/jetson-jetbot-illustration_1600x1260.png" height="256">

JetBot is an open-source robot based on NVIDIA Jetson Nano that is

* **Affordable** - Less than $150 add-on to Jetson Nano
* **Educational** - Tutorials from basic motion to AI based collision avoidance
* **Fun!** - Interactively programmed from your web browser

Building and using JetBot gives the hands on experience needed to create entirely new AI projects.

To get started, read the [JetBot Wiki](https://github.com/NVIDIA-AI-IOT/jetbot/wiki).

**To install any code updates run:**
sudo python3 setup.py install
 

## Jetson Nano with Romi 32U4
I2C pins on Nano ( see https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/ )
* I2C Bus 0 SDA is on Pin 27
* I2C Bus 0 SCL is on Pin 28
* I2C Bus 1 SDA is on Pin 3
* I2C Bus 1 SCL is on Pin 5


I2C pins on Romi (starting from screw)
* I2C Bus SDA is on Pin 37
* I2C Bus SCL is on Pin 35

Nano Pin|OLED Pin 
--------|--------
1|Vcc (3.3V)
25|GND
27|SDA
28|SCL

Nano Pin|Romi Pin|Description
--------|--------|-----------
39|36|GND
3|37|SDA
5|35|SCL

See [/images](images) for wiring examples.

## OLED System Status Display
python code (located in cron directory) is configured to run on reboot in the crontab for the jetson user\
```@reboot /home/jetson/jetbot/cron/stats-oled-display.sh```
