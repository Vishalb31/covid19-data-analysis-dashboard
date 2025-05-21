import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

st.title("🦠 Global COVID-19 Dashboard")

# Load the data
df = pd.read_csv("C:/Users/VISHAL BHAGAT/Downloads/archive (10)/covid_19_data.csv")
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])

# Cleaned data
grouped = df.groupby(['ObservationDate', 'Country/Region'], as_index=False)[['Confirmed', 'Deaths', 'Recovered']].sum()

# Sidebar Country selector
country = st.sidebar.selectbox("🌍 Select Country", grouped['Country/Region'].unique())
filtered_df = grouped[grouped['Country/Region'] == country]

# KPIs
st.markdown("### 📊 Latest Statistics")
latest_data = filtered_df[filtered_df['ObservationDate'] == filtered_df['ObservationDate'].max()]
col1, col2, col3 = st.columns(3)
col1.metric("🧪 Confirmed", f"{int(latest_data['Confirmed'].values[0]):,}")
col2.metric("💀 Deaths", f"{int(latest_data['Deaths'].values[0]):,}")
col3.metric("💚 Recovered", f"{int(latest_data['Recovered'].values[0]):,}")

# Line Chart
st.markdown(f"### 📈 Trends for {country}")
fig = px.line(
    filtered_df,
    x='ObservationDate',
    y='Confirmed',
    title=f"Confirmed Cases Over Time in {country}",
    labels={'ObservationDate': 'Date', 'Confirmed': 'Confirmed Cases'},
    markers=True,
    color_discrete_sequence=['orange']
)
st.plotly_chart(fig, use_container_width=True)

# Additional Charts
with st.expander("📉 View Deaths and Recovered Trends"):
    fig2 = px.line(
        filtered_df,
        x='ObservationDate',
        y=['Deaths', 'Recovered'],
        title=f"Deaths and Recovered Trends in {country}",
        labels={'value': 'Count', 'ObservationDate': 'Date', 'variable': 'Metric'},
        color_discrete_map={"Deaths": "red", "Recovered": "green"},
        markers=True
    )
    st.plotly_chart(fig2, use_container_width=True)

# Global Heatmap and Animation
with st.expander("🌐 View Global Heatmap and Animation"):
    st.markdown("### 🌍 Global COVID-19 Heatmap")

    latest_date = grouped['ObservationDate'].max()
    global_df = grouped[grouped['ObservationDate'] == latest_date]

    fig_heatmap = px.choropleth(
        global_df,
        locations='Country/Region',
        locationmode='country names',
        color='Confirmed',
        hover_name='Country/Region',
        color_continuous_scale='Reds',
        title=f"Confirmed COVID-19 Cases Worldwide on {latest_date.date()}",
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

    st.markdown("### 🕹️ Animated Global Spread Over Time")

    fig_animated = px.choropleth(
        grouped,
        locations='Country/Region',
        locationmode='country names',
        color='Confirmed',
        hover_name='Country/Region',
        animation_frame=grouped['ObservationDate'].dt.strftime('%Y-%m-%d'),
        color_continuous_scale='Viridis',
        range_color=[0, grouped['Confirmed'].max()],
        title="🕹️ Animated Spread of COVID-19 Globally",
    )
    st.plotly_chart(fig_animated, use_container_width=True)

# Footer
st.markdown(
    """
    <hr style="border:1px solid #ccc"/>
    <center>Made with ❤️ by Vishal Ramsuchit Bhagat</center>
    """,
    unsafe_allow_html=True
)
