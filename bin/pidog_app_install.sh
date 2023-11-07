#!/bin/bash

VER="1.0.0"
echo "script version $VER"

# print colors
# ========================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
GRAY='\033[1;30m'
#
NC='\033[0m'

# ========================
READ_TIMEOUT=30

# check permission
# ========================
if [ $(id -u) -ne 0 ]; then
  printf "Script must be run as root. Try 'sudo bash pidog_app_install.sh'\n"
  exit 1
fi

# get username and userhome
# ========================
user=${SUDO_USER:-$(who -m | awk '{ print $1 }')}
user_home="$(eval echo ~$user)"
echo "User: "$user

# ================================ interactive commands ==============================
echo -e "${GREEN}install pidog_app interactive commands ...${NC}"
cp ./pidog_app /usr/local/bin/
chmod +x /usr/local/bin/pidog_app

# ==================================== auto-start ====================================
echo -e "${GREEN}install pidog_app auto-start service ...${NC}"
# https://www.raspberrypi.com/documentation/computers/configuration.html#software-install

# https://www.freedesktop.org/software/systemd/man/systemd.service.html

cat > /usr/lib/systemd/system/pidog_app.service << EOF
[Unit]
Description=pidog_app service
After=multi-user.target

[Service]
Type=simple
ExecStart=sudo python3 $user_home/pidog/examples/12_app_control.py &
PrivateTmp=True
User=$user
Group=$user

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable pidog_app.service
systemctl restart pidog_app.service
# sudo systemctl status pidog_app.service
# journalctl -u pidog_app.service
# journalctl -u pidog_app.service --lines=50

# =============================== AP mode =============================================
DEFAULT_WIFI_SSID="pidog"
DEFAULT_WIFI_PSK="12345678"

# install hostapd and dnsmasq
# ==========================================
if [ ! -n "$1" ] || [ "$1" != "--no-dep" ]; then
    echo -e "${GREEN}install hostapd and dnsmasq ...${NC}"
    apt-get update
    apt-get install hostapd dnsmasq -y
fi

# install netfilter-persistent iptables-persistent
# ==========================================
if [ ! -n "$1" ] || [ "$1" != "--no-dep" ]; then
    echo -e "${GREEN}install netfilter-persistent iptables-persistent ...${NC}"
    DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent
fi

# Create and backup files of the Wireless Interface IP Configuration
# ==========================================
echo -e "${GREEN}Create and backup the Wireless Interface IP Configuration ...${NC}"

if [ ! -e /etc/dhcpcd.conf.sta.bak ]; then
    cp /etc/dhcpcd.conf /etc/dhcpcd.conf.sta.bak
fi

cat >> /etc/dhcpcd.conf.ap.bak << EOF
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
EOF


# Create file of Routing and IP Masquerading
# ==========================================
echo -e "${GREEN}Enable Routing and IP Masquerading ...${NC}"

cat > /etc/sysctl.d/routed-ap.conf << EOF
# Enable IPv4 routing
net.ipv4.ip_forward=1
EOF

# iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
# sudo netfilter-persistent save

# # stop iptable
# sudo systemctl stop iptables.service 
# sudo systemctl disable iptables.service

# Configure the DHCP and DNS services for the wireless network
# ==========================================
echo -e "${GREEN}Configure the DHCP and DNS services for the wireless network ...${NC}"

# systemctl stop dnsmasq

if [ ! -e /etc/dnsmasq.conf.orig ]; then
    mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
fi

cat > /etc/dnsmasq.conf << EOF
interface=wlan0 # Listening interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
                # Pool of IP addresses served via DHCP
domain=wlan     # Local wireless DNS domain
address=/gw.wlan/192.168.4.1
                # Alias for this router
EOF

# systemctl start dnsmasq

# Ensure Wireless Operation
# ==========================================
echo -e "${GREEN}Ensure Wireless Operation ...${NC}"
sudo rfkill unblock wlan

# Configure the AP Software
# ==========================================
echo -e "${GREEN}Configure the AP Software ...${NC}"

cat > /etc/hostapd/hostapd.conf << EOF
country_code=GB
interface=wlan0
ssid=$DEFAULT_WIFI_SSID
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=$DEFAULT_WIFI_PSK
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOF

# # whether start hotspot
# # ==========================================
# echo -n -e "$(echo -e ${BLUE}Do you want to reboot to start hotspot?\(Y/N\): ${NC} )"
# count=0
# while true; do
#     # ((count++))
#     let count++

#     if ! read -t $READ_TIMEOUT choice; then
#         echo -e "\nTime is up, no password entered."
#         exit 1
#     fi

#     case "$choice" in
#         y|Y)
#             systemctl unmask hostapd
#             systemctl enable hostapd
#             systemctl start hostapd
#             echo "Rebooting now ..."
#             sudo reboot
#             break
#             ;;
#         n|N|"")
#             break
#             ;;
#         *)
#             if [ $count -lt 5 ]; then
#                 echo -n 'Invalid input, please enter again:'
#             else
#                 break
#             fi
#             ;;
#     esac
# done

exit 0
