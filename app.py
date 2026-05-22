import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='IRR Dashboard', layout='wide')

st.title('Bank Interest Rate Risk Dashboard')
st.write('UBPR-style balance sheet sensitivity analysis')

# Load data
file_path = 'data/sample_bank_data.csv'
df = pd.read_csv(file_path)

# Convert to dictionary
values = dict(zip(df['Category'], df['Amount']))

rsa = values['Rate Sensitive Assets']
rsl = values['Rate Sensitive Liabilities']
assets = values['Total Assets']
liabilities = values['Total Liabilities']
nii = values['Net Interest Income']

gap = rsa - rsl
gap_ratio = gap / assets

# Determine sensitivity
if gap > 0:
    sensitivity = 'Asset Sensitive'
elif gap < 0:
    sensitivity = 'Liability Sensitive'
else:
    sensitivity = 'Neutral'

# Rate shock assumptions
up_200bp = gap * 0.02
down_200bp = gap * -0.02

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric('GAP', f'${gap:,.0f}')
col2.metric('GAP Ratio', f'{gap_ratio:.2%}')
col3.metric('Sensitivity', sensitivity)

st.subheader('Balance Sheet Composition')

chart_df = pd.DataFrame({
    'Category': ['RSA', 'RSL'],
    'Amount': [rsa, rsl]
})

fig = px.bar(chart_df, x='Category', y='Amount', title='Rate Sensitive Position')
st.plotly_chart(fig, use_container_width=True)

st.subheader('Estimated NII Impact')

scenario_df = pd.DataFrame({
    'Scenario': ['+200bp Shock', '-200bp Shock'],
    'Estimated Impact': [up_200bp, down_200bp]
})

scenario_fig = px.bar(
    scenario_df,
    x='Scenario',
    y='Estimated Impact',
    title='Estimated Net Interest Income Impact'
)

st.plotly_chart(scenario_fig, use_container_width=True)

st.subheader('Interpretation')

if sensitivity == 'Asset Sensitive':
    st.success('The bank appears asset sensitive. Rising rates may improve net interest income.')
elif sensitivity == 'Liability Sensitive':
    st.warning('The bank appears liability sensitive. Rising rates may pressure net interest income.')
else:
    st.info('The bank appears relatively balanced from a repricing perspective.')
