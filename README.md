# FORTRESS: Production-Grade Cryptographic Credential Vault Pro

A secure, persistent digital credential storage matrix and password utility engine built with Streamlit, Python's cryptography ecosystem, and an embedded SQLite relational database layer.

---

## 🛡️ Architecture & Security Blueprint

### 1. Dual-Layer Encryption Infrastructure
- **Persistent Cryptography Engine:** Leverages industry-standard **AES-based Fernet tokens** to handle localized, block-level data encryption routines.
- **Zero-Knowledge Gatekeeper Matrix:** Implements a strict access gateway using a **SHA-256 hash snapshot** of the user-defined Master Password. The core key is never exposed, transmitted, or logged in raw formatting.

### 2. Relational SQLite Storage Framework
- Transitions data collections from volatile in-memory arrays into a persistent local file infrastructure (`fortress_vault.db`).
- Implements strict data schema isolation boundaries, ensuring user record continuity across local deployment lifecycles.

### 3. Dynamic Real-Time Entropy Evaluator
- Utilizes custom algorithmic validation pipelines to evaluate strings across complexity metrics (length boundaries, character sets, number distributions, and symbol sets).
- Generates interactive, color-coded cryptographic telemetry outputs detailing the threat vector level of your chosen secrets.

---

## 🛠️ Tech Stack & Dependencies
- **UI Framework:** Streamlit
- **Data Logistics:** Pandas
- **Encryption Suite:** Cryptography (Fernet)
- **Database Engine:** SQLite3 (Native Python Interface)

---

## ⚡ Production Deployment Configuration

1. Clone this repository to your local directory:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/fortress-credential-vault.git](https://github.com/YOUR_USERNAME/fortress-credential-vault.git)
   cd fortress-credential-vault

2. Initialize the environment dependencies:
    bash
    pip install -r requirements.txt
3. Spin up the localized secure database vault:
    bash
    streamlit run app_vault.py