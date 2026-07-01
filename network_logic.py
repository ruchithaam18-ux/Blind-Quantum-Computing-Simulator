# -*- coding: utf-8 -*-
"""
network_logic.py -- The Virtual Quantum Channel
Role: Networker / Tunnel Builder
"""

import time
import json
import os

MAILBOX_FILE = "quantum_mailbox.json"

STATUS_EMPTY     = "Channel: Empty"
STATUS_TRANSIT   = "Channel: Qubits in Transit"
STATUS_COMPUTING = "Channel: Computing..."


def send_circuit(circuit_data):
    print("[Networker] Routing qubits through Virtual Quantum Channel...")
    time.sleep(1)
    payload = {
        "status": "in_transit",
        "data": circuit_data,
        "timestamp": time.time()
    }
    with open(MAILBOX_FILE, "w") as f:
        json.dump(payload, f)
    print("[Networker] OK - Qubits delivered to mailbox.")


def receive_circuit():
    if not os.path.exists(MAILBOX_FILE):
        return None
    with open(MAILBOX_FILE, "r") as f:
        payload = json.load(f)
    if payload.get("status") == "in_transit":
        payload["status"] = "computing"
        with open(MAILBOX_FILE, "w") as f:
            json.dump(payload, f)
        print("[Networker] Bob has picked up the circuit. Channel: Computing...")
        return payload["data"]
    return None


def clear_mailbox():
    if os.path.exists(MAILBOX_FILE):
        os.remove(MAILBOX_FILE)
    print("[Networker] Mailbox cleared. Channel reset to Empty.")


def get_channel_status():
    if not os.path.exists(MAILBOX_FILE):
        return {"label": STATUS_EMPTY, "color": "#9E9E9E", "blink": False}
    with open(MAILBOX_FILE, "r") as f:
        payload = json.load(f)
    if payload.get("status") == "in_transit":
        return {"label": STATUS_TRANSIT, "color": "#FFC107", "blink": True}
    if payload.get("status") == "computing":
        return {"label": STATUS_COMPUTING, "color": "#4CAF50", "blink": False}
    return {"label": STATUS_EMPTY, "color": "#9E9E9E", "blink": False}


def render_status_sidebar():
    try:
        import streamlit as st
    except ImportError:
        print("[Networker] Streamlit not installed.")
        return
    status = get_channel_status()
    blink_css = ""
    if status["blink"]:
        blink_css = """
        <style>
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }
        .status-dot { animation: blink 1s infinite; }
        </style>"""
    st.sidebar.markdown(
        f"""{blink_css}
        <div style="display:flex;align-items:center;gap:10px;padding:8px 0;">
            <div class="status-dot" style="width:14px;height:14px;border-radius:50%;
                background:{status['color']};box-shadow:0 0 6px {status['color']};"></div>
            <span style="font-size:14px;font-weight:600;">{status['label']}</span>
        </div>""",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    print("=== Virtual Quantum Channel - Self Test ===\n")

    s = get_channel_status()
    print("Initial status : " + s["label"])

    sample_circuit = {"qubits": 2, "gates": ["H", "CNOT"], "shots": 1024}
    send_circuit(sample_circuit)

    s = get_channel_status()
    print("After Alice sends: " + s["label"] + " (blink=" + str(s["blink"]) + ")")

    data = receive_circuit()
    print("Bob received   : " + str(data))

    s = get_channel_status()
    print("While computing: " + s["label"])

    clear_mailbox()

    s = get_channel_status()
    print("After clear    : " + s["label"])

    print("\nAll systems nominal. Virtual Quantum Channel is ready!")
