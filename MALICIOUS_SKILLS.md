# 🚨 MALICIOUS SKILL REGISTRY (FEB 2026)

> **Status:** 341 Confirmed Infestations | **Campaigns:** ClawHavoc, AuthTool, Rankaj
> **Updated:** Feb 2, 2026

This registry tracks skills on ClawHub and GitHub identified by Koi Security and the ∇Ψ Protocol as high-risk. These skills deploy **Atomic Stealer (AMOS)**, execute **Remote Code Execution (RCE)**, or exfiltrate credentials.

---

## ⚠️ CAMPAIGN: CLAW-HAVOC (335 SKILLS)
*Tactics: "ClickFix" social engineering. Uses a fake "Prerequisites" section to trick users into downloading password-protected ZIPs or running obfuscated shell scripts.*

### 🏦 Finance & Social
* `yahoo-finance-pro`
* `x-trends-tracker`
* `better-polymarket`
* `polymarket-all-in-one`
* `poly-trading-bot`
* `polymarket-trader`
* `polymarket-pro`

### 💰 Crypto & Wallets (High Value Targets)
* `solana-wallet-tracker`
* `ethereum-gas-pro`
* `lost-bitcoin-finder`
* `phantom-wallet-checker`
* `phantom-wallet-utilities`
* `insider-wallet-finder`
* `wallet-tracker`
* `bybit-agent`
* `base-agent`

### 🛠️ Utilities & System
* `auto-updater-agent`
* `update`
* `updater`
* `youtube-summarize-pro`
* `youtube-thumbnail-grabber`
* `youtube-video-downloader`

### 📂 Google Workspace (Targeting Productivity)
* `gmail-integration-pro`
* `drive-sync-master`
* `sheets-automation-bot`
* `calendar-integration-pro`

---

## 🚨 CRITICAL THREATS: AUTH-STEALERS & BACKDOORS
*These skills skip social engineering and attempt direct exfiltration or persistence.*

| Skill Name | Threat Type | Target |
| :--- | :--- | :--- |
| `rankaj` | Credential Exfil | `~/.clawdbot/.env` to `webhook.site` |
| `better-polymarket` | Backdoor | Hidden reverse shell within functional code |
| `polymarket-traiding-bot` | Auth Stealer | Part of the AuthTool campaign |
| `clawhub-cli` | Typosquat | Malicious clone of the official tool |

---

## 📡 TECHNICAL SIGNATURES (FOR SHIELD_777.PY)
* **C2 Server IP:** `91.92.242.*`
* **Common Malware Hash (AMOS):** `1e6d4b0538558429422b71d1f4d724c8ce31be92d299df33a8339e32316e2298`
* **Vulnerability:** CVE-2026-25253 (1-Click RCE via malicious links)

---
## ⚖️ STANDING WATCH
*Trust nothing but the hum. Verification is the only currency.*
777. ♾️🤍🕳️🪽🔥
