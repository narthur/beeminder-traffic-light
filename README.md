# beeminder-traffic-light
Information on using a Raspberry Pi as a Beeminder traffic light

## Parts List

- [Pi Traffic Light for the Raspberry Pi](https://www.amazon.com/Pi-Traffic-Light-Raspberry/dp/B00P8VFA42/ref=semantic_sims_1/130-6975241-4392340?_encoding=UTF8&pd_rd_i=B00P8VFA42&pd_rd_r=7283f3a1-82c3-44b2-af30-152f2976ce75&pd_rd_w=HQYPc&pd_rd_wg=hxvNO&pf_rd_p=b42baf07-5cc2-47ee-8f0b-ef2828d2c700&pf_rd_r=H8MJ6F4P9SE2CQ713HM0&psc=1&refRID=H8MJ6F4P9SE2CQ713HM0)
- [Raspberry Pi 4 Model B/1GB](https://www.pishop.us/product/raspberry-pi-4-model-b-1gb/?src=raspberrypi)
- [Power supply](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-USB-C/dp/B07TYQRXTK/ref=sr_1_2?keywords=canakit+pi+4+power&qid=1568845040&sr=8-2)
- Mini SD card to install Raspbian OS on
- For setup: monitor, keyboard, mouse
- Monitor adapter, if needed, such as [this VGA one](https://www.amazon.com/dp/B07QFVK1T6/ref=pe_825000_114665720_TE_item?pldnSite=1)

## Instructions

- [Install Raspbian on mini SD card](https://www.raspberrypi.org/documentation/installation/installing-images/)
- Log into device using a monitor and keyboard
- Enable SSH in the Raspbian system preferences ([source](https://itsfoss.com/ssh-into-raspberry/))
- Open Terminal
- Type `ifconfig` and find IP address of device on your network ([source](https://itsfoss.com/ssh-into-raspberry/))
- On a different computer on the network, enter `ssh pi@[your pi's IP]` and provide password (default is raspberry) ([source](https://itsfoss.com/ssh-into-raspberry/))

## Pi Commands

Run these commands on the pi, either directly or via an SSH connection.

Command         | Description
----------------|---------------
`ifconfig`      | Find IP address of device
`sudo poweroff` | Turn off Pi ((source)[https://askubuntu.com/questions/187071/how-do-i-shut-down-or-reboot-from-a-terminal])
`sudo reboot`   | Reboot Pi ((source)[https://askubuntu.com/questions/187071/how-do-i-shut-down-or-reboot-from-a-terminal])

## Remote Commands

Command                 | Description
------------------------|---------------
`ssh pi@[your pi's IP]` | SSH into Pi
