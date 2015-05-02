GFW
===
Wa11-Breaking Tools and Data

---

##OS X

###Shadowsocks Proxy Settings
1. Download [Shadowsocks-GUI](http://shadowsocks.org/en/download/clients.html) which is advocated by [Clowwindy](https://github.com/clowwindy), then install it on your Mac and keep it running;
2. Since the public server provided by this tool's developers seemed to have some trouble these days, you will have to get a tenable VPS or remote Virtual Host as the node for wall breaking, which has already running shadowsocks-server version 24/7;if had no trouble doing so, goto step 4 then;
3. Ask your friends for help or buying a DigitalOcean (or Linode, Vultr, etc) VPS is reasonable choices in fulfulling step 2, while you might need a Paypal account or Credit Card that supports paying in both RMB and Dollars; for server settings, simply refers to [Shadowsocks Wiki](https://github.com/shadowsocks/shadowsocks/wiki) on Github, which is quite clear as well as extended;
4. Configure Shadowsocks-GUI's local server settings that points to your remote server, and try enjoying surfing YouTube, Google or something now? (when AutoProxy mode does not work, switch to GlobalProxy mode)

###PAC Settings
>Due to the applying of Cocoa Network Library, the proxy setting on Shadowsocks-GUI will affect your Safari web browser if your current WiFi or LAN proxy setting is configured to "Auto" or "Socks" (to be specific, Socks5); 

>Yet the AutoProxy mode in Shadowsocks-GUI will, in further, intelligently avoid using remote routing for domestic sites request, and only use proxy when the request is send to website that might be in GFW-ban-list;

>To use it more efficiently, editing PAC by ourselves is recommended

1. Goto "~/.ShadowsocksX/" which is a hidden config directory;
2. Replace the original pac file in it with this **gfwlist.js**, which is provided by Clowwindy as a precise mode pac, and slightly improved by myself;
3. As for Firefox, goto Preference->Advanced->Network->Config How Firefox links to Internet, select Using PAC, and locate the file such as "file:///Users/Adward/Github/GFW/whitelist.pac"; I use a *whitelist* **whitelist.pac** for Firefox, which could also be downloaded here.

###Hosts Settings
>Stronger hosts provide a even more quick direct access to banned sites such as Google and Dropbox, etc

1. Download **Hosttools** and retrieve hosts files from Github, SourceForge, Seattle or anywhere else, backup your old hosts, apply the changes, and that is all;
2. If you had trouble doing so, download hosts(latest updated one) here and extract it to "/etc/"; better do not forget to backup as well!