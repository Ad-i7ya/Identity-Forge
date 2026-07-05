<p align="center">
  <img src="https://i.pinimg.com/736x/08/fd/13/08fd1318df57327d038d873baab766a9.jpg" width="100%" alt="IdentityForge Banner"/>
</p>

<h1 align="center">IdentityForge</h1>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/Ad-i7ya/IdentityForge?style=for-the-badge">
  </a>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/Ad-i7ya/IdentityForge?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/Ad-i7ya/IdentityForge?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/REST-API-02569B?style=for-the-badge">
  <img src="https://img.shields.io/badge/Cloudflare-Workers-F38020?style=for-the-badge&logo=cloudflare">
  <img src="https://img.shields.io/badge/JSON-Data-black?style=for-the-badge&logo=json">
  <img src="https://img.shields.io/badge/Privacy-OPSEC-blueviolet?style=for-the-badge">
</p>

<p align="center">
  <b>A developer-friendly API & CLI for generating synthetic identities</b><br>
  Built for testing, mock data, privacy-focused workflows, and OPSEC training.
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3500&pause=1000&color=58A6FF&center=true&vCenter=true&width=900&lines=Developer-friendly+REST+API;Synthetic+Identity+Generation;Testing+%7C+Mock+Data+%7C+OPSEC+Training;Cloudflare+Workers+Powered;CLI+Coming+Soon" alt="Typing SVG" />
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-example-response">Example</a> •
  <a href="#-usage--feedback">Feedback</a> •
  <a href="#-license">License</a>
</p>

## 📖 Overview

IdentityForge is a developer-friendly REST API and upcoming CLI that generates realistic **synthetic identities** for testing, mock data generation, privacy-focused workflows, demonstrations, automation, and OPSEC training.

Designed with simplicity in mind, IdentityForge provides consistent JSON responses, broad country support, and an easy-to-integrate API suitable for developers, cybersecurity enthusiasts, QA engineers, and researchers.
---
## ✨ Features

- 🌍 Generate synthetic identities for multiple countries
- ⚡ Fast REST API
- 💻 CLI support (coming soon)
- 📚 Developer-friendly documentation (coming soon)

- ## 🚀 Quick Start

### Base URL

```text
https://identity-forge.adi7ya.workers.dev
```

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/countries` | List all supported countries |
| GET | `/generate?country=<code>` | Generate a synthetic identity |

### Example

```http
GET /generate?country=us
```
---

### Example Response

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
