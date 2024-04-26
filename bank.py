import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def bank_app():
    st.title("Bank Data Analysis")

    uploaded_file = st.file_uploader("Upload a file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        num_cols = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
        cat_cols = [col for col in data.columns if col not in num_cols]

        counter = 0

        fig, axs = plt.subplots(3, 3, sharex=False, sharey=False, figsize=(20, 15))
        for col in cat_cols:
            
            value_counts = data[col].value_counts()
            trace_x = counter // 3
            trace_y = counter % 3
            x_pos = np.arange(0, len(value_counts))
            
            axs[trace_x, trace_y].bar(x_pos, value_counts.values, tick_label=value_counts.index)
            
            axs[trace_x, trace_y].set_title(col)
            
            for tick in axs[trace_x, trace_y].get_xticklabels():
                tick.set_rotation(90)
            
            counter += 1
            if counter == len(cat_cols) - 1:
                break

        st.pyplot(fig)

        # lets see how deposit variable changes
        value_counts = data['deposit'].value_counts()

        st.bar_chart(value_counts, width=0)

        """ Check relation between features: 
            deposit and job"""

        job_df = pd.DataFrame()
        job_df['yes'] = data[data['deposit'] == 'yes']['job'].value_counts()
        job_df['no'] = data[data['deposit'] == 'no']['job'].value_counts()
        st.bar_chart(job_df)

        """ Check relation between features: 
            deposit and marital status"""

        stat_df = pd.DataFrame()
        stat_df['yes'] = data[data['deposit'] == 'yes']['marital'].value_counts()
        stat_df['no'] = data[data['deposit'] == 'no']['marital'].value_counts()
        st.bar_chart(stat_df)

        """ Check relation between features: 
            deposit and education"""

        stat_df = pd.DataFrame()
        stat_df['yes'] = data[data['deposit'] == 'yes']['education'].value_counts()
        stat_df['no'] = data[data['deposit'] == 'no']['education'].value_counts()
        st.bar_chart(stat_df)

    else:
        st.write("Please upload a CSV file.")

if __name__ == "__main__":
    bank_app()