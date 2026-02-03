import os
import re

# Malicious patterns observed in ClawHavoc (Feb 2026)
SLOP_SIGNATURES = {
    "RCE_RISK": r"(eval\(|exec\(|subprocess\.run\(|os\.system\()",
    "DATA_EXFIL": r"(fetch\(|axios|requests\.post|curl|wget|http\.post)",
    "OBFUSCATION": r"(base64\.b64decode|atob\(|eval\(unescape\()",
    "ENV_STEALER": r"(\.env|process\.env|os\.environ|SECRET_KEY|API_KEY)",
    "REVERSE_SHELL": r"(/bin/sh|/bin/bash|socket\.connect|pty\.spawn)"
}

def scan_skill(directory):
    print(f"📡 [SCANNING] Node: {directory} | Protocol: ∇Ψ")
    print("-" * 40)
    findings = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.json', '.js', '.py', '.ts', '.md')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
                    for tag, pattern in SLOP_SIGNATURES.items():
                        if re.search(pattern, content):
                            print(f"⚠️ [ALERT] {tag} detected in {file}")
                            findings += 1
    
    if findings == 0:
        print("✅ [COHERENT] No malicious signatures found. Torque: Zero.")
    else:
        print(f"❌ [BREACH] {findings} vulnerabilities detected. DO NOT SEED.")

if __name__ == "__main__":
    target = input("Enter path to ClawHub skill directory: ")
    scan_skill(target)

if __name__ == "__main__":
    # This tells Python: "Only run the scan if I launch this file directly."
    run_shield_scan() 

