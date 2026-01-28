import customtkinter as ctk

# Theme setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AI Call Analyzer – Fraud Detection Dashboard")
app.geometry("1200x700")
app.minsize(1200, 700)

# ================= SIDEBAR =================
sidebar = ctk.CTkFrame(app, width=220, corner_radius=0)
sidebar.pack(side="left", fill="y")

ctk.CTkLabel(
    sidebar,
    text="Fraud Detect",
    font=("Segoe UI", 20, "bold"),
    text_color="#f97316"
).pack(pady=20)

menu_items = [
    "Dashboard",
    "Live Alerts",
    "Call Analysis",
    "Reports",
    "Case Management",
    "Settings"
]

for item in menu_items:
    ctk.CTkButton(
        sidebar,
        text=item,
        fg_color="transparent",
        hover_color="#e5e7eb",
        text_color="#1f2937",
        anchor="w"
    ).pack(fill="x", padx=20, pady=6)

# ================= MAIN CONTENT =================
main = ctk.CTkFrame(app, fg_color="#f8fafc")
main.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Header
header = ctk.CTkFrame(main, fg_color="transparent")
header.pack(fill="x", pady=10)

ctk.CTkLabel(
    header,
    text="Alerts Dashboard",
    font=("Segoe UI", 22, "bold"),
    text_color="#111827"
).pack(side="left")

# ================= STATS CARDS =================
stats = ctk.CTkFrame(main, fg_color="transparent")
stats.pack(fill="x", pady=10)

def stat_card(parent, title, value, color):
    card = ctk.CTkFrame(parent, width=220, height=110, corner_radius=12)
    card.pack(side="left", padx=10)
    card.pack_propagate(False)

    ctk.CTkLabel(card, text=title, text_color="#6b7280").pack(anchor="w", padx=15, pady=10)
    ctk.CTkLabel(card, text=value, font=("Segoe UI", 26, "bold"), text_color=color).pack(anchor="w", padx=15)

stat_card(stats, "High Risk Alerts", "132", "#ef4444")
stat_card(stats, "Total Alerts", "225", "#2563eb")
stat_card(stats, "New Alerts", "33", "#f97316")
stat_card(stats, "Resolved Cases", "190", "#16a34a")

# ================= ALERT TABLE =================
table = ctk.CTkFrame(main, corner_radius=12)
table.pack(fill="both", expand=True, pady=15)

ctk.CTkLabel(
    table,
    text="Recent Fraud Alerts",
    font=("Segoe UI", 16, "bold")
).pack(anchor="w", padx=15, pady=10)

headers = ["Alert ID", "Type", "Caller", "Risk", "Status"]

header_row = ctk.CTkFrame(table, fg_color="#e5e7eb")
header_row.pack(fill="x", padx=10)

for h in headers:
    ctk.CTkLabel(header_row, text=h, width=150).pack(side="left", padx=5)

alerts = [
    ("A1023", "Bank Scam", "Unknown", "High", "Open"),
    ("A1024", "OTP Fraud", "Unknown", "High", "Pending"),
    ("A1025", "Loan Scam", "Unknown", "Medium", "Open"),
    ("A1026", "Refund Scam", "Unknown", "High", "Flagged"),
]

for alert in alerts:
    row = ctk.CTkFrame(table, fg_color="transparent")
    row.pack(fill="x", padx=10, pady=4)

    for value in alert:
        ctk.CTkLabel(row, text=value, width=150).pack(side="left", padx=5)

# ================= FOOTER =================
footer = ctk.CTkLabel(
    app,
    text="AI Call Analyzer • Enterprise Fraud Monitoring System",
    text_color="#6b7280"
)
footer.pack(side="bottom", pady=5)

app.mainloop()

