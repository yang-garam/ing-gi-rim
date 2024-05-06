import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import plotly.express as px

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(page_title="MAIN")
    st.title("TOPIC: Spnish Influenza")
    st.header("What factors made US state-specific mortality different in the 1918 Influenza pandemic?")
    st.subheader("     ")
    st.subheader("     ")

# 사망률 지도
def death():
    st.subheader('USA Death Rate from influenza by State (per one hundred thousand people)')
    data = {
    'State': ['CA', 'CO', 'CT', 'IL', 'IN', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 
              'MN', 'MO', 'MT', 'NH', 'NJ', 'NY', 'NC', 'OH', 'OR', 'PA', 'RI', 'SC', 
              'TN', 'UT', 'VT', 'VA', 'WA', 'WI'],
    'Death Rate': [324.3, 412.2, 411, 253.2, 200.9, 235.6, 321.1, 287, 326.6, 373.3, 
                   337, 214.6, 249.3, 207.5, 551.4, 452.1, 301, 214.4, 325.4, 275.1, 
                   180.1, 452, 343.9, 379.6, 271.7, 313.5, 381.2, 424, 191.9, 245.6]
    }

    df = pd.DataFrame(data)

    # 지도 표시
    fig = px.choropleth(df, 
                        locations='State',
                        locationmode='USA-states',
                        color='Death Rate',
                        scope="usa",
                        hover_name='State',
                        color_continuous_scale='Reds',
                        hover_data={'Death Rate': True})
    
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    run()
    death()
