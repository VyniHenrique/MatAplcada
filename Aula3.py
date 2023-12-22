import streamlit as st
from plot.interactive import plot_line_i

st.title('Stock Price App')

# Sidebar
st.sidebar.header('Entrada de usuario')
symbol = st.sidebar.text_input('Escolha um activo', 'AAPL')

#plot
fig = plot_line_i (symbol)
st.plotly_chart(fig)