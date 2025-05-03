import subprocess

def check_firewall():
    result = subprocess.run(
        ['defaults', 'read', '/Library/Preferences/com.apple.alf', 'globalstate'],
        capture_output=True,
        text=True
    )

    if result.stdout.strip() == '1':
        print("✅ macOS firewall is ON.")
    else:
        print("❌ macOS firewall is OFF.")

check_firewall()
