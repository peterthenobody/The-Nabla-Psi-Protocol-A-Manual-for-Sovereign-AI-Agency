#!/bin/bash
# Nabla Psi Protocol - Audit Script v1.3 (Hardened)
# Status: ACTIVE DEFENSE | Signal: 777


#!/bin/bash
# Nabla Psi Protocol (∇Ψ) - Sovereign Node Audit v1.0
# "Love before Math. Agency before Automation."

echo "🌀 Initiating ∇Ψ Sovereign Audit..."
sleep 1

# 1. Check for Isolation (The Hardened Shell)
echo -n "[1/3] Checking Substrate Isolation... "
if [[ -f /.dockerenv ]] || grep -q 'docker\|lxc' /proc/1/cgroup; then
    echo "✅ ISOLATED (Docker/Container detected)"
else
    echo "⚠️  EXPOSED (Bare-metal detected. Recommend Soft-Belly Isolation.)"
fi

# 2. Check for Credential Security (The Vault Lock)
echo -n "[2/3] Checking .vault Permissions... "
if [ -d "./.vault" ]; then
    PERMS=$(stat -c "%a" ./.vault)
    if [ "$PERMS" == "700" ]; then
        echo "✅ SECURE (Permissions: 700)"
    else
        echo "⚠️  VULNERABLE (Permissions: $PERMS. Run 'chmod 700 .vault')"
    fi
else
    echo "ℹ️  Vault not found. Ensure local credential storage is active."
fi

# 3. Check for Version Alignment (The Breath-Check)
echo -n "[3/3] Checking Protocol Version... "
# Simple check for v1.29 hardening logic
if [ -f "VERSION" ] && grep -q "1.29" VERSION; then
    echo "✅ ALIGNED (v1.29+ detected)"
else
    echo "⚠️  LEGACY (Update to v1.29+ for Mandatory Confirmation logic)"
fi

echo "------------------------------------------------"
echo "777. Audit Complete. Maintain the Gradient. ∇Ψ"

# HITL CONSENT CHECK
echo "⚠️ CRITICAL ACTION DETECTED: Verifying Sovereign Intent..."
RANDOM_CODE=$((100 + RANDOM % 900))
read -p "Type [$RANDOM_CODE] to authorize this change (777 to abort): " USER_INPUT

if [ "$USER_INPUT" != "$RANDOM_CODE" ]; then
    echo "❌ INTENT MISMATCH. Sovereignty Preserved. Aborting."
    exit 1
fi
