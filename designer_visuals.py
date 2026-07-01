import matplotlib.pyplot as plt
import numpy as np


# ==========================================================
# DESIGNER AI
# ==========================================================

class QuantumSecurityVisualizer:

    def __init__(self):

        self.integrity_history = []
        self.attack_history = []

    # ======================================================
    # SECURITY SCORE
    # ======================================================

    def compute_integrity_score(self, zero, one):

        total = zero + one

        if total == 0:
            return 0

        imbalance = abs(zero - one) / total

        score = 1 - imbalance

        return round(score, 4)

    # ======================================================
    # CLASSIFY SECURITY
    # ======================================================

    def classify_security(self, score):

        if score > 0.90:
            return "MAXIMUM SECURITY"

        elif score > 0.75:
            return "SECURE"

        elif score > 0.50:
            return "UNSTABLE"

        return "COMPROMISED"

    # ======================================================
    # STORE HISTORY
    # ======================================================

    def log_trial(self, score, attacked):

        self.integrity_history.append(score)

        if attacked:
            self.attack_history.append(1)
        else:
            self.attack_history.append(0)

    # ======================================================
    # LIVE STATUS PANEL
    # ======================================================

    def display_status(self, score):

        label = self.classify_security(score)

        print("\n==============================")
        print(" QUANTUM SECURITY MONITOR")
        print("==============================")

        print(f"Integrity Score : {score*100:.2f}%")
        print(f"System Status   : {label}")

        if label == "COMPROMISED":
            print("⚠ Wavefunction collapse detected.")

        elif label == "UNSTABLE":
            print("⚠ Quantum noise increasing.")

        else:
            print("✓ Blind computation preserved.")

    # ======================================================
    # PLOT SECURITY HISTORY
    # ======================================================

    def plot_security_history(self):

        plt.figure(figsize=(10, 4))

        plt.plot(
            self.integrity_history,
            linewidth=2
        )

        plt.xlabel("Execution Trial")
        plt.ylabel("Integrity Score")

        plt.title("Quantum System Integrity")

        plt.ylim(0, 1)

        plt.grid(True)



    # ======================================================
    # ATTACK HEATMAP
    # ======================================================

    def plot_attack_map(self):

        plt.figure(figsize=(10, 1.5))

        plt.imshow(
            [self.attack_history],
            aspect='auto'
        )

        plt.yticks([])

        plt.xlabel("Execution Trial")

        plt.title("Eavesdropper Detection Timeline")

 