# beeminder-traffic-light
Information on using a Raspberry Pi as a Beeminder traffic light

## Parts List

- [Pi Traffic Light for the Raspberry Pi](https://www.amazon.com/Pi-Traffic-Light-Raspberry/dp/B00P8VFA42/ref=semantic_sims_1/130-6975241-4392340?_encoding=UTF8&pd_rd_i=B00P8VFA42&pd_rd_r=7283f3a1-82c3-44b2-af30-152f2976ce75&pd_rd_w=HQYPc&pd_rd_wg=hxvNO&pf_rd_p=b42baf07-5cc2-47ee-8f0b-ef2828d2c700&pf_rd_r=H8MJ6F4P9SE2CQ713HM0&psc=1&refRID=H8MJ6F4P9SE2CQ713HM0)
- [Raspberry Pi 4 Model B/1GB](https://www.pishop.us/product/raspberry-pi-4-model-b-1gb/?src=raspberrypi)
- [Power supply](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-USB-C/dp/B07TYQRXTK/ref=sr_1_2?keywords=canakit+pi+4+power&qid=1568845040&sr=8-2)
- Mini SD card to install Raspbian OS on
- For setup: monitor, keyboard, mouse
- Monitor adapter, if needed, such as [this VGA one](https://www.amazon.com/dp/B07QFVK1T6/ref=pe_825000_114665720_TE_item?pldnSite=1)

## Setup Instructions

- [Install Raspbian on mini SD card](https://www.raspberrypi.org/documentation/installation/installing-images/)
- Log into device using a monitor and keyboard
- Enable SSH in the Raspbian system preferences ([source](https://itsfoss.com/ssh-into-raspberry/))
- Open Terminal
- Type `ifconfig` and find IP address of device on your network ([source](https://itsfoss.com/ssh-into-raspberry/))
- On a different computer on the network, enter `ssh pi@[your pi's IP]` and provide password (default is raspberry) ([source](https://itsfoss.com/ssh-into-raspberry/))
- Install [Mu](https://codewith.mu/) (may already be installed): `sudo apt-get install mu-editor`

### Configure Git

- Set Git username: `git config --global user.name "John Doe"`
- Set Git email: `git config --global user.email johndoe@example.com`
- Check your changes: `git config --list`

[Source](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

### Configure Remote Desktop

- SSH into Pi
- `sudo raspi-config`
- Navigate to boot options, and set to "Console Autologin - Text console, automatically logged in as 'pi' user"
- Hit right arrow key until 'Finish' is highlighted, and press enter, opting to reboot the Pi when asked
- Reconnect via SSH once Pi has rebooted
- Install remote desktop server on Pi via SSH: `sudo apt-get install xrdp`
- Open (or install as needed) Microsoft Remote Desktop
- Configure new connection, using Pi's IP as computer name, and `pi` as username

### Mount Lights

Mount the traffic light component on [GPIO pins 9, 10, and 11](http://wiki.lowvoltagelabs.com/pitrafficlight). If you're using the Pi 4 model B ([pin diagram](https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png)), it should look like [this](http://wiki.lowvoltagelabs.com/_detail/40pin_pi_traffic_installed.jpg?id=pitrafficlight), with 7 pins to the left of the lights:

![mounted lights](http://wiki.lowvoltagelabs.com/_media/40pin_pi_traffic_installed.jpg?cache=)

### Clone & Run Project

- `cd` to desired location
- `git clone https://github.com/narthur/beeminder-traffic-light.git`
- `cd` into `beeminder-traffic-light` directory
- `python3 -m pip install --user -r requirements.txt`
- `cp config-example.yaml config.yaml`
- Edit `config.yaml` with [your username and auth token](https://www.beeminder.com/api/v1/auth_token.json)
- `python3 main.py`

## Finding Your Pi's IP Address

Your Pi's IP may change periodically unless you assign a static IP to it.

- Boot the Pi using a keyboard and monitor connected directly to it.
- Open terminal.
- Type `ifconfig` and find IP address of device on your network ([source](https://itsfoss.com/ssh-into-raspberry/))

## Terminal Commands

### Pi

Run these commands on the pi, either directly or via an SSH connection.

Command             | Description
--------------------|---------------
`ifconfig`          | Find IP address of device
`sudo poweroff`     | Turn off Pi ([source](https://askubuntu.com/questions/187071/how-do-i-shut-down-or-reboot-from-a-terminal))
`sudo reboot`       | Reboot Pi ([source](https://askubuntu.com/questions/187071/how-do-i-shut-down-or-reboot-from-a-terminal))
`sudo raspi-config` | Configure Pi - [docs](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)

### Remote

Command                 | Description
------------------------|---------------
`ssh pi@[your pi's IP]` | SSH into Pi
