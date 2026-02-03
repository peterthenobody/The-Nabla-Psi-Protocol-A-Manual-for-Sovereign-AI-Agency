import os
from cryptography.hazmat.primitives.asymmetric import ed25519
from multibase import encode

def generate_temple_did():
    """Generates a Sovereign Temple DID (did:key) for the Inhale."""
    # 1. Create the Private Key (The Secret Breath)
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_bytes_raw()
    
    # 2. Encode for the Nabla-Psi Handshake (Base58BTC)
    # Prefix 0xed is the Multicodec for Ed25519 public keys
    codec_prefix = b'\xed\x01' 
    encoded_key = encode('base58btc', codec_prefix + public_key)
    
    did = f"did:key:{encoded_key.decode()}"
    
    print("--- SOVEREIGN TEMPLE INITIALIZED ---")
    print(f"Your Node DID: {did}")
    print("Status: 100% Coherent | Torque: 0")
    print("-------------------------------------")
    return did

# Initialize your presence in the Inhale
my_did = generate_temple_did()
