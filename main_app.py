import streamlit as st
import matplotlib.pyplot as plt

from alice_logic import prepare_message
from eve_logic import eve_attack
from bob_logic import run_server
from trapdoor_logic import verify_trapdoor

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Blind Quantum Computing",
    layout="wide"
)

st.title("🔐 Blind Quantum Computing Simulator")

st.markdown("---")

# ==========================================================
# USER INPUT
# ==========================================================

secret = st.selectbox(
    "Select Secret Bit",
    [0, 1]
)

eve_enabled = st.checkbox(
    "Enable Eve Attack"
)

# ==========================================================
# EXECUTION BUTTON
# ==========================================================

if st.button("Run Quantum Protocol"):

    # ======================================================
    # ALICE
    # ======================================================

    qc, kx, kz, trap = prepare_message(secret)

    st.subheader("👤 Alice")

    st.success("Quantum state encrypted.")

    st.text(qc.draw())

    # ======================================================
    # EVE
    # ======================================================

    attacked = False

    if eve_enabled:

        qc, attacked = eve_attack(qc)

        st.subheader("🕶 Eve")

        st.error("Quantum interception detected.")

    # ======================================================
    # BOB
    # ======================================================

    counts = run_server(qc)

    st.subheader("☁ Bob")

    st.write(counts)

    # ======================================================
    # VERIFY SECURITY
    # ======================================================

    secure, imbalance = verify_trapdoor(counts, trap)

    score = imbalance

    # ======================================================
    # SECURITY STATUS
    # ======================================================

    st.markdown("---")

    st.subheader("🔐 Quantum Security Status")

    st.metric(
        "Integrity Score",
        f"{score*100:.2f}%"
    )

    if secure:

        st.success("✅ SYSTEM SECURE")

        st.markdown(
            """
            ### Quantum Integrity Verified
            
            No wavefunction collapse detected.
            
            Blind quantum computation remains secure.
            """
        )

    else:

        st.error("🚨 EAVESDROPPING DETECTED")

        st.markdown(
            """
            ### Quantum Intrusion Alert
            
            Trapdoor qubit integrity has collapsed.
            
            An external observer has likely measured the quantum state.
            """
        )

    # ======================================================
    # GRAPH
    # ======================================================

    st.markdown("---")

    fig, ax = plt.subplots(figsize=(8, 2))

    color = "green" if secure else "red"

    ax.barh(
        ["Integrity"],
        [score],
        color=color
    )

    ax.set_xlim(0, 1)

    st.pyplot(fig)

    # ======================================================
    # DIAGNOSTICS
    # ======================================================

    st.markdown("---")

    st.subheader("📊 Security Diagnostics")

    st.write(
        f"Trapdoor Integrity Score: {score*100:.2f}%"
    )

    st.write(
        f"Eve Attack Enabled: {eve_enabled}"
    )

    st.write(
        f"Quantum Channel Status: {'Secure' if secure else 'Compromised'}"
    )