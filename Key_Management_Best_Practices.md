# Key Management & Secure Storage Best Practices

## 1. Secret Storage
- **Never hardcode secrets** in source code.
- Use a **centralized Key Management Service (KMS)** (e.g., AWS KMS, HashiCorp Vault, Azure Key Vault).
- Use **environment variables** or secure injected volumes in CI/CD pipelines.

## 2. Key Rotation
- Enforce **regular key rotation** (e.g., every 90 days) for symmetric encryption keys and API tokens.
- Support **grace periods** where both old and new keys are active to allow services to transition without downtime.

## 3. Access Control (Least Privilege)
- Ensure applications only have access to the specific keys they need.
- Use Role-Based Access Control (RBAC) and robust IAM policies.
- Audit all access and usage logs for cryptographic keys.
