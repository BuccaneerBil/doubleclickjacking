doubleclickjacking
Proof of concept to test successful redirection from an attacker-controlled UI

Vulnerability Overview
DoubleClickjacking is a novel exploitation technique that leverages subtle UI manipulation to bypass traditional clickjacking protections. This attack method involves a crafted user interface (UI), such as a cookie consent pop-up, designed to trick users into performing critical actions through a double-click sequence.

Attack Flow
Attacker-Controlled UI: The attacker deploys a malicious interface (e.g., a cookie pop-up).
Double-Click Interaction: The user is prompted to double-click on an innocuous-looking button (e.g., "Accept Cookies").
Redirection or Action: The double-click triggers a hidden action, such as OAuth approval or sensitive workflow initiation, without the user’s explicit consent.
Impact: Users unknowingly authorise actions, leading to account compromise, unauthorised access, or data leakage.
This proof of concept demonstrates how DoubleClickjacking could be used to manipulate user interactions while bypassing X-Frame-Options, Content Security Policies (CSP), and SameSite cookies.

Usage Guide
This script demonstrates the DoubleClickjacking attack flow for educational and testing purposes. Use it only on systems you are authorised to test.

Requirements
Python 3.x

Running the Test
  Clone the repository:
    git clone https://github.com/<your-username>/doubleclickjacking.git
    cd doubleclickjacking

Run the script:
    python3 doubleclickjack.py <target_url>

Replace <target_url> with the URL of the site you want to test.

Follow the steps:
  A simulated attack UI will open in your browser.
  Interact with the "Cookie Consent" pop-up to test for DoubleClickjacking vulnerability.
  Observe the attack flow and any redirections.

Disclaimer
This script is provided for educational purposes only. Use it responsibly and only on systems you have explicit permission to test. The author is not responsible for misuse or any damage caused by the improper use of this script.

Example Usage
python3 doubleclickjack.py https://example.com

  A "Start DoubleClickjacking Test" button appears.
  Clicking it opens a simulated cookie consent pop-up.
  Double-clicking the "Accept Cookies" button triggers redirection to the target page or simulates a critical action.


Vulnerability Risks
Unauthorised Actions: Critical actions like OAuth approval or sensitive workflow initiation.
Data Leakage: Exposing sensitive data or permissions via user interaction.
Account Takeover: Exploiting OAuth or session management flaws.
