<p align="center">
  <img src="https://i.pinimg.com/736x/08/fd/13/08fd1318df57327d038d873baab766a9.jpg" width="100%" alt="IdentityForge Banner"/>
</p>

<h1 align="center">IdentityForge</h1>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/Ad-i7ya/Identity-Forge?style=for-the-badge">
  </a>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/Ad-i7ya/Identity-Forge?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/Ad-i7ya/Identity-Forge?style=for-the-badge">
</p>

<p align="center"> 
 
  <p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/REST-API-02569B?style=for-the-badge">
  <img src="https://img.shields.io/badge/Cloudflare-Workers-F38020?style=for-the-badge&logo=cloudflare">
  <img src="https://img.shields.io/badge/JSON-Data-black?style=for-the-badge&logo=json">
  <img src="https://img.shields.io/badge/Privacy-OPSEC-blueviolet?style=for-the-badge">
</p>

<p align="center">
  <b>A developer-friendly API & CLI for generating synthetic identities</b><br>
  Built for testing, mock data, privacy-focused workflows, and OPSEC training.
</p>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3500&pause=1000&color=58A6FF&center=true&vCenter=true&width=900&lines=Developer-friendly+REST+API;Synthetic+Identity+Generation;Python+Module+%7C+CLI+%7C+REST+API;Testing+%7C+Mock+Data+%7C+OPSEC+Training;Cloudflare+Workers+Powered" alt="Typing SVG" />
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-example-response">Example</a> •
  <a href="#-usage--feedback">Feedback</a> •
  <a href="#-license">License</a>
</p>

## 📖 Overview

IdentityForge is an open-source toolkit for generating realistic **synthetic identities** for development, testing, automation, cybersecurity labs, privacy-focused workflows, demonstrations, and OPSEC training.

Unlike traditional identity generators, IdentityForge provides **three different ways** to access the same service, allowing developers to integrate it into any workflow:

- 💻 Command Line Interface (CLI)
- 🐍 Python Module
- 🌐 REST API

Whether you're writing automation scripts, testing applications, building demos, or experimenting with APIs, IdentityForge offers a simple and consistent developer experience.

---

# ✨ Features

- 🌍 Generate realistic synthetic identities for multiple countries
- ⚡ Fast REST API
- 💻 Cross-platform Command Line Interface (CLI)
- 🐍 Python package support
- 📦 Easy installation
- ☁️ Powered by Cloudflare Workers
- 📚 Comprehensive documentation
- 🔒 Uses synthetic data only

---

# 🚀 Installation

IdentityForge can be used in multiple ways depending on your workflow.

## Option 1 — Install from GitHub (Recommended)

Clone the repository and install IdentityForge locally.

```bash
git clone https://github.com/Ad-i7ya/Identity-Forge.git
cd Identity-Forge
pip install -r requirements.txt
pip install -e .
```

After installation, verify that the CLI is available:

```bash
identityforge --help
```

List all supported countries:

```bash
identityforge countries
```

Generate a synthetic identity:

```bash
identityforge generate us
```
---

## Option 2 — Install from PyPI


```bash
pip install identityforge-cli
```

Verify the installation:

```bash
identityforge --help
```

List all supported countries:

```bash
identityforge countries
```

Generate a synthetic identity:

```bash
identityforge generate us
```
---

# 🐍 Option 3 — Python Module

IdentityForge can also be used directly inside your Python applications.

Import the package:

```python
from identityforge import get_countries, generate_identity
```

List all supported countries:

```python
from identityforge import get_countries

countries = get_countries()
print(countries)
```

Generate a synthetic identity:

```python
from identityforge import generate_identity

identity = generate_identity("us")
print(identity)
```



---

# 🌐 Option 4 — REST API

Use IdentityForge directly through HTTP requests.

### Base URL

```text
https://identity-forge.adi7ya.workers.dev
```

### Available Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| GET | `/countries` | List supported countries |
| GET | `/generate?country=<code>` | Generate a synthetic identity |

### Example Request

```http
GET /generate?country=us
```

---

## 🧬 Example Response

```json
{
  "success": true,
  "data": [
    {
      "Full Name": "Michael Walker",
      "Gender": "Female",
      "Birthday": "1967-08-08",
      "Age": 55,
      "Email": "gregoryking@example.net",
      "Phone Number": "+1 640229935",
      "Country": "United States",
      "Country Code": "US",
      "Country Flag": "https://flagcdn.com/w320/us.png",
      "Flag Emoji": "🇺🇸",
      "State": "Illinois",
      "City": "West Elizabethton",
      "Street": "979 Kyle Well Apt. 289",
      "Pin Code": "56292",
      "Time Zone": "UTC-05:00",
      "Currency": "US Dollar (USD) - $",
      "Blood Group": "B+"
    }
  ],
  "metadata": {
    "version": "1.0.0"
  }
}
```

---

# 📚 Documentation

Additional documentation is available in the repository.

- 📖 **CLI Guide:** `docs/cli.md`
- 🌐 **API Documentation:** `docs/api.md`
- 💡 **cURL Examples:** `examples/curl.md`

---

# 🤝 Feedback

If you find IdentityForge useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐞 Report bugs by opening an Issue
- 💡 Suggest new features or improvements

Contributions and constructive feedback are always welcome.

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](https://github.com/Ad-i7ya/Identity-Forge?tab=License-1-ov-file) file for more information.

