import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

st.set_page_config(page_title="Previsão do Petróleo Brent", layout="centered")

st.title("Previsão do Preço do Petróleo Brent (USD)")

uploaded_file = st.file_uploader("Faça upload do arquivo CSV com colunas 'Date' e 'Preço (USD)'", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
    df = df.rename(columns={"Date": "ds", "Preço (USD)": "y"})
    df["ds"] = pd.to_datetime(df["ds"], format="%b %d, %Y")
    df = df.dropna()

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    st.subheader("Previsão Completa")
    fig1 = model.plot(forecast)
    st.pyplot(fig1)

    st.subheader("Previsão dos Próximos 30 Dias")
    forecast_only = forecast[forecast['ds'] > df['ds'].max()]
    fig2, ax = plt.subplots()
    ax.plot(forecast_only['ds'], forecast_only['yhat'], label='Previsão', color='blue')
    ax.fill_between(forecast_only['ds'], forecast_only['yhat_lower'], forecast_only['yhat_upper'], alpha=0.3, color='skyblue')
    ax.set_title('Previsão de 30 Dias do Preço do Petróleo')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço (USD)')
    ax.grid(True)
    st.pyplot(fig2)

    st.subheader("Métricas de Erro")
    df_merge = forecast[['ds', 'yhat']].merge(df, on='ds')
    mae = abs(df_merge['y'] - df_merge['yhat']).mean()
    rmse = ((df_merge['y'] - df_merge['yhat']) ** 2).mean() ** 0.5
    st.write(f"**MAE:** {mae:.2f}")
    st.write(f"**RMSE:** {rmse:.2f}")
   
    st.subheader("Componentes da Previsão (Tendência e Sazonalidade)")
    try:
        from prophet.plot import plot_components_plotly
        fig3 = plot_components_plotly(model, forecast)
        st.plotly_chart(fig3)
    except:
        fig3 = model.plot_components(forecast)
        st.pyplot(fig3)

    
    st.subheader("Tabela com os Próximos 30 Dias de Previsão")
    st.dataframe(
        forecast_only[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].reset_index(drop=True).head(30)
    )
