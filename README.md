# doubleclickjacking

**Proof of concept to test successful redirection from an attacker-controlled UI**

---

## Vulnerability Overview

DoubleClickjacking is a novel exploitation technique that leverages subtle UI manipulation to bypass traditional clickjacking protections. This attack method involves a crafted user interface (UI), such as a cookie consent pop-up, designed to trick users into performing critical actions through a double-click sequence.

### Attack Flow

1. **Attacker-Controlled UI**: The attacker deploys a malicious interface (e.g., a cookie pop-up).
2. **Double-Click Interaction**: The user is prompted to double-click on an innocuous-looking button (e.g., "Accept Cookies").
3. **Redirection or Action**: The double-click triggers a hidden action, such as OAuth approval or sensitive workflow initiation, without the user’s explicit consent.
4. **Impact**: Users unknowingly authorise actions, leading to account compromise, unauthorised access, or data leakage.

This proof of concept demonstrates how DoubleClickjacking could be used to manipulate user interactions while bypassing X-Frame-Options, Content Security Policies (CSP), and SameSite cookies.

---

## Usage Guide

This script demonstrates the DoubleClickjacking attack flow for educational and testing purposes. Use it only on systems you are authorised to test.

### Requirements

- Python 3.x

### Running the Test

1. Clone the repository:
   ```bash
   git clone https://github.com/BuccaneerBil/doubleclickjacking.git
   cd doubleclickjacking


### Disclaimer

This script is provided for educational purposes only. Use it responsibly and only on systems you have explicit permission to test. The author is not responsible for misuse or any damage caused by the improper use of this script.

### Example Usage

1. Clone the repository:
   ```bash
   python3 doubleclickjack.py https://example.com
1. A "Start DoubleClickjacking Test" button appears.
2. Clicking it opens a simulated cookie consent pop-up.
3. Double-clicking the "Accept Cookies" button triggers redirection to the target page or simulates a critical action.
