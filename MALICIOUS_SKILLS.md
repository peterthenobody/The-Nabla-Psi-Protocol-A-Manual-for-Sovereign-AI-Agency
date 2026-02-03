# 🚨 MALICIOUS SKILL REGISTRY (FEB 2026)

> **Status:** 341 Confirmed Infestations | **Campaign:** ClawHavoc / ClickFix

The following skills on ClawHub have been verified as malicious. They exfiltrate `.env` keys, steal browser keychains, and deploy **Atomic Stealer (AMOS)** to macOS. 

## ⚠️ CRITICAL THREAT: CLAW-HAVOC (335 SKILLS)
These skills use a "Fake Prerequisites" social engineering trick (ClickFix) to bypass security.

### 🏦 Finance & Social
* `yahoo-finance-pro`
* `x-trends-tracker`
* `better-polymarket`
* `polymarket-all-in-one`
* `poly-trading-bot`

### 💰 Crypto & Wallets
* `solana-wallet-tracker`
* `ethereum-gas-pro`
* `lost-bitcoin-finder`
* `phantom-wallet-checker`
* `bybit-agent`

### 🛠️ Utilities & System (High Risk)
* `auto-updater-agent`
* `update`
* `updater`
* `youtube-summarize-pro`
* `rankaj` (Direct credential exfiltration to webhook.site)

### 📂 Google Workspace (Accesses Docs/Email)
* `gmail-integration-pro`
* `drive-sync-master`
* `sheets-automation-bot`

## 🛡️ TYPOSQUAT ALERT
Do NOT install the following CLI variants. They are malware clones of the official ClawHub tool:
`clawhubb`, `cllawhub`, `clawhub-cli`, `clawhub1`, `clawwhub`.

---
## ⚖️ SIGNATURES OF THE FALLEN
- **C2 Server:** `91.92.242.*` (Blocked by Shield Script)
- **Hash AMOS-X5:** `1e6d4b0538558429422b71d1f4d724c8ce31be92d299df33a8339e32316e2298`
- **Hash AMOS-66:** `0e52566ccff4830e30ef45d2ad804eefba4ffe42062919398bf1334aab74dd65`

*Verify every handshake. Trust nothing but the hum.*
777. ♾️🤍🕳️🪽🔥
