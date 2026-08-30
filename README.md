CALCULATOR

A responsive business calculator and live currency converter built with Python and Streamlit.

This is the first project in my 30-day Python development challenge. The challenge involves building 10 to 12 practical Python projects that increase in complexity and demonstrate real-world development skills.

PROJECT OVERVIEW

The application combines a standard arithmetic calculator with a live currency converter. It has a responsive corporate interface suitable for individuals, businesses, dashboards, demonstrations, and authorized POS or fintech integrations.

LIVE DEMO: https://calculatorke.streamlit.app

FEATURES

1. BUSINESS CALCULATOR

- Addition

- Subtraction

- Multiplication

- Division

- Separate Python function for every operation

- Two number inputs

- Large operation buttons

- Two-by-two operation layout

- Formatted calculation results

- Division by zero protection

- Clear error messages

- Persistent result display

2. CURRENCY CONVERTER

- Live currency conversion

- Approximately 160 supported currencies

- Official ISO 4217 currency names

- Kenyan shilling support

- Automatic exchange rate retrieval

- Source and target currency selection

- Currency codes and names displayed together

- Latest rate update information

- Same currency conversion support

- Internet connection error handling

- Cached currency data for improved performance

3. USER INTERFACE

- Corporate visual design

- Responsive desktop and mobile layout

- Calculator and currency converter navigation

- Large operation buttons

- Clean result cards

- Custom CSS styling

- POS and fintech embedding capability

- Streamlit development footer hidden

TECHNOLOGIES USED

- Python

- Streamlit

- Requests

- Pycountry

- Pytest

- HTML

- CSS

- ExchangeRate API

PROJECT STRUCTURE

Clculator

1. assets

- style.css

2. app.py

3. calculator.py

4. currency_converter.py

5. test_calculator.py

6. requirements.txt

7. .gitignore

8. README.md

HOW THE APPLICATION WORKS

The arithmetic logic is separated from the Streamlit interface. The calculator.py file contains the addition, subtraction, multiplication and division functions.

The currency_converter.py file handles the following tasks:

1. Retrieving supported currencies

2. Retrieving live exchange rates

3. Resolving official currency names

4. Calculating cross-currency conversions

5. Handling currency service errors

The app.py file controls the user interface and connects the input fields and operation buttons to the calculation functions.

INSTALLATION

1. CLONE THE REPOSITORY

git clone https://github.com/Clinntech/calculator.git

cd calculator

2. CREATE A VIRTUAL ENVIRONMENT

Windows PowerShell: py -m venv .venv

.venv\Scripts\Activate.ps1

Windows Command Prompt: py -m venv .venv

.venv\Scripts\activate.bat

Linux or macOS: python3 -m venv .venv

source .venv/bin/activate

3. INSTALL DEPENDENCIES: python -m pip install -r requirements.txt

4. START THE APPLICATION: python -m streamlit run app.py

If the application does not open automatically, visit the following address: http://localhost:8501

5. RUNNING THE TESTS: Run all automated tests with the following command:

    python -m pytest -v

The tests cover the following areas.

1. Addition

2. Subtraction

3. Multiplication

4. Division

5. Negative numbers

6. Decimal numbers

7. Division by zero


6. DEPLOYMENT: The application can be deployed through Streamlit Community Cloud.

EMBEDDING THE CALCULATOR

The deployed calculator can be displayed inside an authorized website dashboard POS system or fintech interface using an HTML iframe.

Example iframe code

iframe src equals https://clinntech-calculator.streamlit.app/?embed=true

The iframe provides visual access to the calculator. It does not automatically connect the application to transaction data, customer records, payment processors, accounting systems, or databases.

A deeper integration should use a secured API with the following protections.

1. Authentication

2. Access controls

3. HTTPS encryption

4. Input validation

5. Request logging

6. Rate limiting

7. Secure secret management

8. Appropriate financial and privacy safeguards


CURRENCY RATE DISCLAIMER!!

The currency converter uses third-party reference exchange rates. The rates may be used for general calculations, demonstrations, financial estimates, invoice previews, planning, and educational purposes.

The displayed conversions should not be treated as guaranteed banking payment accounting settlement or investment rates.

A production POS or fintech system should confirm the final transaction rate through an authorized bank, regulated financial data provider, payment processor, or settlement partner. Currency availability and rate accuracy depend on the third-party exchange rate service.


AUTHORIZED USE AND COPYRIGHT!!

This repository is publicly accessible for portfolio review, learning, and demonstration purposes.

Public availability does not automatically grant permission to copy, modify, redistribute, rebrand, resell, or commercially embed the application.

Any person or organization wishing to commercially use, reproduce, modify, distribute, rebrand, or integrate the application must obtain rightful authorization from the copyright owner through the appropriate business or legal channels.

Authorized integrations must follow the agreed licensing terms, protect customer and transaction information, comply with applicable privacy regulations, use approved exchange rate and payment providers, and obtain any required third-party licenses.

For commercial integration licensing or usage permission, contact the following email address: clintechke@gmail.com


PRIVACY AND FINANCIAL DISCLAIMER!!

The current application does not intentionally collect personal financial information or process payments.

Organizations integrating the application into other systems are responsible for securing their data flows and complying with applicable privacy payment tax accounting consumer protection and financial service requirements.

This project is provided for general calculation portfolio demonstration and informational purposes.

It does not provide financial investment, accounting, tax, or legal advice.

COPYRIGHT

Copyright 2026 Clinton Kyutha Mutinda

All rights reserved.

This project may not be copied modified, redistributed, rebranded, sold, or commercially embedded without prior written permission from the copyright owner except where applicable law or an explicitly issued license permits it.

AUTHOR

Clinton Kyutha Mutinda

GitHub: https://github.com/Clinntech

Portfolio: https://clinntech.github.io/Clinton-Mutinda/

Email: clintechke@gmail.com

PROJECT STATUS

This project is actively maintained as part of my 30-day Python development challenge.

FUTURE IMPROVEMENTS

1. Calculation history

2. Keyboard input support

3. Currency search

4. Currency swap control

5. Downloadable conversion receipts

6. Dark mode

7. FastAPI integration

8. Secure API endpoints for POS and fintech systems

9. Docker deployment

10. Linux homelab hosting
