import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

st.set_page_config(
    page_title="제어공학기말",
)

st.header("응답곡선")

num = [100]
den = [1, 5, 106]

ltf = signal.TransferFunction(num, den)

t = np.linspace(0, 5, 1000)
u = np.ones_like(t)

t, y, _ = signal.lsim(ltf, u, t)

fig, ax = plt.subplots()
ax.plot(t, y)
ax.set(xlabel='Time', ylabel='Output', title='Step Response')
ax.grid(True)

st.pyplot(fig)
