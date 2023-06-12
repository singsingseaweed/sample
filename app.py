import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def main():
    st.title("202021024_임동휘")
    st.header("202021024_임동휘")
    st.subheader("step and bode plot")
    
    # 폐루프 전달함수
    num = [100]
    den = [1, 5, 106]
    L = signal.TransferFunction(num, den)

    # 시간 영역에서의 응답
    t, y = signal.step(L)
    fig1, ax1 = plt.subplots()
    ax1.plot(t, y)
    ax1.set(xlabel='Time', ylabel='Output', title='Step Response')
    ax1.grid(True)
    st.pyplot(fig1)

    # 주파수 응답의 보드선도
    w, mag, phase = signal.bode(L)
    fig2, (ax2, ax3) = plt.subplots(2, 1, figsize=(8, 6))
    ax2.semilogx(w, mag)
    ax2.set(xlabel='Frequency [rad/s]', ylabel='Magnitude [dB]', title='Bode Plot - Magnitude')
    ax2.grid(True)
    ax3.semilogx(w, phase)
    ax3.set(xlabel='Frequency [rad/s]', ylabel='Phase [degrees]', title='Bode Plot - Phase')
    ax3.grid(True)
    plt.tight_layout()
    st.pyplot(fig2)

if __name__ == '__main__':
    main()
