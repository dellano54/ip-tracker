# 🌍 God's Eye

God's Eye is a simple yet powerful tool that allows you to locate the geographical location of any IP address using public IP geolocation APIs and visualize the location on Google Maps instantly.

Whether you're a cybersecurity enthusiast, ethical hacker, or just curious, God's Eye is your go-to utility for quickly tracing IP addresses with ease.

---

## 🚀 Features

* ✅ Real-time IP geolocation
* ✅ Google Maps integration
* ✅ Simple CLI interface
* ✅ Works on any Linux machine
* ✅ Lightweight and fast

---

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dellano54/Gods-eye.git
   cd Gods-eye/
   ```
2. Give execution permission and run the installer:

   ```bash
   sudo chmod +x install.sh
   sudo ./install.sh
   ```

---

## ⚙️ Usage

```bash
gods-eye <ip_address>
```

Example:

```bash
gods-eye 8.8.8.8
```

Help:

```bash
gods-eye --help
```

---

## 📊 Sample Output

```
IP:         8.8.8.8
Status:     success
City:       Mountain View
ISP:        Google LLC
Latitude:   37.4056
Longitude: -122.0775
Country:    United States
Region:     California
Zip:        94043
AS:         AS15169 Google LLC
```

Google Maps will open automatically showing the location of the IP address.

---

## 🔧 Under the Hood

* Language: Python 3
* API used: [ip-api.com](http://ip-api.com/)
* Maps: Google Maps search with latitude and longitude

---

## 🚫 Disclaimer

God's Eye uses publicly available APIs for educational and ethical purposes only. The accuracy of location data may vary, and we do not encourage using this tool for any malicious or unauthorized activities.

---

## 📸 Screenshots

![Screenshot](https://raw.githubusercontent.com/dellano54/Gods-eye/master/screenshot/Screenshot%202020-06-12%2005%3A54%3A53.png)

---

## 🚀 Author

Developed with ❤️ by [Dellano54](https://github.com/dellano54)
