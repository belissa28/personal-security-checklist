import subprocess
#checks local computer's firewalll
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


def check_site_url(url):
    
#checks if the url contains https
    if "https" in url:
        print("SAFE")
    else:
        print("NOT SAFE")

check_site_url("https://example.com")
