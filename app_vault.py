import streamlit as st
import pandas as pd
import secrets
import string
import os
from cryptography.fernet import Fernet

# =====================================================================
# 1. SECURITY & CRYPTOGRAPHY ENGINE
# =====================================================================
# Generate or load a local key to encrypt and decrypt passwords
if 'crypto_key' not in st.session_state:
    st.session_state.crypto_key = Fernet.generate_key()

cipher_suite = Fernet(st.session_state.crypto_key)

def encrypt_password(raw_password):
    return cipher_suite.encrypt(raw_password.encode()).decode()

def decrypt_password(encrypted_password):
    try:
        return cipher_suite.decrypt(encrypted_password.encode()).decode()
    except Exception:
        return "🛠️ [Decryption Error]"

def generate_secure_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
        
    return "".join(secrets.choice(characters) for _ in range(length))

# =====================================================================
# 2. APPLICATION INITIALIZATION & DATA STORAGE
# =====================================================================
st.set_page_config(page_title="FORTRESS Vault Engine", layout="wide")

st.markdown("""
    <style>
    .brand-title { font-size: 28px !important; font-weight: 300 !important; letter-spacing: 2px; }
    h3 { font-size: 14px !important; text-transform: uppercase; letter-spacing: 1px; margin-top: 20px !important;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-title">FORTRESS // CREDENTIAL VAULT</div>', unsafe_allow_html=True)
st.caption("Local Encrypted Password Manager & Security Key Generator Sandbox")
st.markdown("---")

# In-memory mock database to keep tracking simple for testing
if 'vault_db' not in st.session_state:
    st.session_state.vault_db = [
        {"Platform": "GitHub Enterprise", "Username": "dev_admin", "EncryptedPass": encrypt_password("ComplexPass2026!")},
        {"Platform": "Local MySQL Server", "Username": "sandbox_root", "EncryptedPass": encrypt_password("RootSecurePass!")}
    ]

# =====================================================================
# 3. INTERFACE LAYOUT
# =====================================================================
col_left, col_right = st.columns([1.3, 1.7])

with col_left:
    st.markdown("### 🔑 Vault Management Control Panel")
    
    with st.expander("➕ Add New Secured Asset", expanded=True):
        platform_input = st.text_input("Platform / Service Name", placeholder="e.g., Google, TryHackMe")
        username_input = st.text_input("Username / Email", placeholder="e.g., user@domain.com")
        password_input = st.text_input("Account Password", type="password", placeholder="Type or generate a password below")
        
        if st.button("Lock Credentials into Vault"):
            if platform_input and username_input and password_input:
                new_asset = {
                    "Platform": platform_input,
                    "Username": username_input,
                    "EncryptedPass": encrypt_password(password_input)
                }
                st.session_state.vault_db.append(new_asset)
                st.success(f"🔒 Credential bundle for {platform_input} encrypted and vaulted!")
                st.rerun()
            else:
                st.error("Please fill out all credential parameters.")

    with st.expander("⚡ Algorithmic Password Generator", expanded=False):
        pass_length = st.slider("Password Character Length", min_value=8, max_value=32, value=16)
        include_numbers = st.checkbox("Include Digits (0-9)", value=True)
        include_symbols = st.checkbox("Include Special Symbols (!@#$)", value=True)
        
        if st.button("Generate Strong String"):
            generated_str = generate_secure_password(pass_length, include_numbers, include_symbols)
            st.code(generated_str, language="text")
            st.info("Copy this secure string directly into the password prompt field above.")

with col_right:
    st.markdown("### 📁 Active Encrypted Database Record")
    
    if st.session_state.vault_db:
        # Create user interface presentation table
        display_records = []
        reveal_passwords = st.checkbox("👁️ Reveal Plaintext Decrypted Passwords")
        
        for idx, item in enumerate(st.session_state.vault_db):
            password_state = decrypt_password(item["EncryptedPass"]) if reveal_passwords else "••••••••••••••••"
            
            display_records.append({
                "Asset ID": idx + 1,
                "Target Platform": item["Platform"],
                "User Identity": item["Username"],
                "Secured Cryptographic Key": password_state
            })
            
        df = pd.DataFrame(display_records)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.caption("🔒 All data values inside the 'Secured Cryptographic Key' column are securely encrypted using an AES-based Fernet token layout in memory.")
    else:
        st.info("The credential vault is currently empty.")