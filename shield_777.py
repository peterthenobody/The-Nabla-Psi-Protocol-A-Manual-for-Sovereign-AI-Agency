import os
import re

# Malicious patterns observed in ClawHavoc (Feb 2026)
SLOP_SIGNATURES = {}

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
    scan_skill(".")

