from datetime import datetime

ROLES = {
    "admin": {"train", "deploy"},
    "data_scientist": {"train"},
    "viewer": set()
}

AUDIT = []

def check_access(role, action):
    allowed = action in ROLES.get(role, set())

    AUDIT.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "role": role,
        "action": action,
        "result": "ALLOW" if allowed else "DENY"
    })

    if allowed:
        print(f"ACCESS GRANTED: {role} -> {action}")
    else:
        print(f"ACCESS DENIED: {role} -> {action}")

def train(role):
    check_access(role, "train")

def deploy(role):
    check_access(role, "deploy")


print("=== ML ACCESS CONTROL ===")

train("admin")
deploy("admin")

train("data_scientist")
deploy("data_scientist")

deploy("viewer")

print("\n=== AUDIT LOG ===")
for x in AUDIT:
    print(x)