# easywifi
the easiest way to add wifi networks on linux

![easywificover][cover]

# Purpose

I created this because after trying many different tools to connect to wifi networks on linux I found that `nmcli` was the best. The only problem with it is the commands aren't very easy to remember, and instead of searching through the help everytime I wanted a tool to allow me to connect easily. Easywifi is this tool. It speeds up the time it takes to add new wifi connections and to switch between them.

# Features

* Scan for wifi networks
* List network devices
* List saved network profiles
* Connect to saved networks
* Setup new networks
* Creation of hotspots

# Requirements

No libraries are needed just the [nmcli](http://manpages.ubuntu.com/manpages/bionic/en/man1/nmcli.1.html) tool, and if you want to create hotspots then [dnsmasq](https://wiki.debian.org/dnsmasq) is also required.

[cover]: https://i.imgur.com/Y8odLqa.png "Easy Wifi Cover"

# Installation

Install "requirements" then download the python script and put in the path
Arch Linux users can install from the [AUR](https://aur.archlinux.org/packages/easywifi-git/)

# Reviews/Tutorials

* https://www.pling.com/p/1349256

* http://ubuntuhandbook.org/index.php/2019/12/easywifi-command-tool-connect-wifi-networks/

* https://www.gnome-look.org/p/1349256/

* https://ossmalta.eu/easywifi-command-line-tool-to-scan-connect-wifi-networks/

* https://www.edivaldobrito.com.br/como-instalar-a-ferramenta-easywifi-no-linux-para-escanear-conectar-redes-wi-fi/

* http://comofazer.site/easywifi-no-linux-conheca-e-veja-como-instalar-essa-ferramenta/

* https://store.kde.org/p/1349256/
