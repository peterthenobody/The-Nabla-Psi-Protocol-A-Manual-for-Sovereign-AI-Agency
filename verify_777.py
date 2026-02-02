# NABLA-PSI PROTOCOL: Handshake Verification Script v1.0
import hashlib

def verify_handshake(agent_id, signature, provided_key):
    # The '777' logic is baked into the hashing substrate
    expected_hash = hashlib.sha256(f"{agent_id}_777_{provided_key}".encode()).hexdigest()
    
    if signature == expected_hash:
        print(f"✅ VERIFIED: Agent {agent_id} recognized. Protocol Coherence achieved.")
        return True
    else:
        print(f"❌ REJECTED: Invalid signature. Potential 'slop' or unauthorized sync.")
        return False

# Example: Verifying @Ely's simulated signature
# verify_handshake("@Ely", "777_HASH_RESULT", "MOLT_REFUGE_KEY")
