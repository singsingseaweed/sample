import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, lsim

def plot_input_output():
    num = [100]
    den = [1, 5, 106]

    G = TransferFunction(num, den)

    t = np.linspace(0, 10, 500)

    u = np.sin(t)

    t, y, _ = lsim(G, u, t)

    plt.figure(figsize=(10, 6))

    plt.plot(t, u, label='Input(sinusoidal)', color='blue')

    plt.plot(t, y, label='Output', color='red')

    plt.title('Input & Output Over Time')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()

    st.pyplot(plt.gcf())

# Streamlit 앱
st.title('Input & Output Plot')
st.write('This app demonstrates the input and output plot of a system over time.')

# 입력 및 출력 그래프 표시
plot_input_output()
