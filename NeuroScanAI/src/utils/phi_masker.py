import re
def mask_phi(text):
    return re.sub(r"Patient\s+\w+", "[REDACTED]", text)
