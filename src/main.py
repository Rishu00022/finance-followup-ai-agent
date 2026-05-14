import pandas as pd
from datetime import datetime
import os

# Read invoice data
df = pd.read_csv("data/invoices.csv")

today = datetime.today()

def get_stage(days_overdue):
    if days_overdue <= 7:
        return "Stage 1 - Friendly"
    elif days_overdue <= 14:
        return "Stage 2 - Polite"
    elif days_overdue <= 21:
        return "Stage 3 - Serious"
    elif days_overdue <= 30:
        return "Stage 4 - Urgent"
    else:
        return "Escalate to Legal Team"

for index, row in df.iterrows():

    due_date = datetime.strptime(row["due_date"], "%Y-%m-%d")
    days_overdue = (today - due_date).days

    stage = get_stage(days_overdue)

    print("\n========================")
    print(f"Client: {row['client_name']}")
    print(f"Invoice: {row['invoice_no']}")
    print(f"Amount: ₹{row['amount']}")
    print(f"Days Overdue: {days_overdue}")
    print(f"Stage: {stage}")

    if "Stage 1" in stage:
        email = f"""
Subject: Friendly Payment Reminder

Hi {row['client_name']},

This is a friendly reminder that invoice {row['invoice_no']}
for ₹{row['amount']} is overdue.

Please make the payment at your earliest convenience.

Thank you.
"""

    elif "Stage 2" in stage:
        email = f"""
Subject: Payment Pending Reminder

Dear {row['client_name']},

Our records show invoice {row['invoice_no']}
for ₹{row['amount']} is still unpaid.

Kindly confirm the payment date.

Regards.
"""

    elif "Stage 3" in stage:
        email = f"""
Subject: Important Outstanding Payment Notice

Dear {row['client_name']},

Despite previous reminders,
invoice {row['invoice_no']} remains unpaid.

Please respond within 48 hours.

Regards.
"""

    elif "Stage 4" in stage:
        email = f"""
Subject: FINAL PAYMENT NOTICE

Dear {row['client_name']},

This is the final reminder for invoice
{row['invoice_no']} amount ₹{row['amount']}.

Immediate action is required.

Finance Team
"""

    else:
        email = "Escalate to legal team."

    print(email)
with open("logs/audit_log.txt", "a") as log:

    log.write(f"""
Timestamp: {datetime.now()}
Client: {row['client_name']}
Invoice: {row['invoice_no']}
Amount: ₹{row['amount']}
Days Overdue: {days_overdue}
Stage: {stage}
Status: GENERATED
-----------------------------------
""")
