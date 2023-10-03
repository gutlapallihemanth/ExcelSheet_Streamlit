####
# Activate python env =  source .venv/bin/activate     


### Links

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/




# ******* DASHBOARD *******

# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #

# ---------Basic Dashboard ---------#
# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #




# import pandas as pd  # pip install pandas openpyxl
# import plotly.express as px  # pip install plotly-express
# import streamlit as st  # pip install streamlit

# # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# # ---- READ EXCEL ----
# @st.cache_data
# def get_data_from_excel():
#     df = pd.read_excel(
#         io="supermarkt_sales.xlsx",
#         engine="openpyxl",
#         sheet_name="Sales",
#         skiprows=3,
#         usecols="B:R",
#         nrows=1000,
#     )
#     # Add 'hour' column to dataframe
#     df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
#     return df

# df = get_data_from_excel()

# # ---- SIDEBAR ----
# st.sidebar.header("Please Filter Here:")
# city = st.sidebar.multiselect(
#     "Select the City:",
#     options=df["City"].unique(),
#     default=df["City"].unique()
# )

# customer_type = st.sidebar.multiselect(
#     "Select the Customer Type:",
#     options=df["Customer_type"].unique(),
#     default=df["Customer_type"].unique(),
# )

# gender = st.sidebar.multiselect(
#     "Select the Gender:",
#     options=df["Gender"].unique(),
#     default=df["Gender"].unique()
# )

# df_selection = df.query(
#     "City == @city & Customer_type ==@customer_type & Gender == @gender"
# )

# # Check if the dataframe is empty:
# if df_selection.empty:
#     st.warning("No data available based on the current filter settings!")
#     st.stop() # This will halt the app from further execution.

# # ---- MAINPAGE ----
# st.title(":bar_chart: Sales Dashboard")
# st.markdown("##")

# # TOP KPI's
# total_sales = int(df_selection["Total"].sum())
# average_rating = round(df_selection["Rating"].mean(), 1)
# star_rating = ":star:" * int(round(average_rating, 0))
# average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

# left_column, middle_column, right_column = st.columns(3)
# with left_column:
#     st.subheader("Total Sales:")
#     st.subheader(f"US $ {total_sales:,}")
# with middle_column:
#     st.subheader("Average Rating:")
#     st.subheader(f"{average_rating} {star_rating}")
# with right_column:
#     st.subheader("Average Sales Per Transaction:")
#     st.subheader(f"US $ {average_sale_by_transaction}")

# st.markdown("""---""")

# # SALES BY PRODUCT LINE [BAR CHART]
# sales_by_product_line = df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total")
# fig_product_sales = px.bar(
#     sales_by_product_line,
#     x="Total",
#     y=sales_by_product_line.index,
#     orientation="h",
#     title="<b>Sales by Product Line</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
#     template="plotly_white",
# )
# fig_product_sales.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )

# # SALES BY HOUR [BAR CHART]
# sales_by_hour = df_selection.groupby(by=["hour"])[["Total"]].sum()
# fig_hourly_sales = px.bar(
#     sales_by_hour,
#     x=sales_by_hour.index,
#     y="Total",
#     title="<b>Sales by hour</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#     template="plotly_white",
# )
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )


# left_column, right_column = st.columns(2)
# left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
# right_column.plotly_chart(fig_product_sales, use_container_width=True)

# st.dataframe(df)

# # ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)



# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #
# --------------------------- #

import streamlit as st
import plotly.express as px

import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore!!!",page_icon= ":bar_chart:", layout="wide" )

# Set the title and button using markdown for custom layout
st.markdown(
    """
    ## :bar_chart: Sample Superstore EDA 
    <span style="float: right; padding: 0.25rem 0.75rem; background-color: #0083B8; color: white; border-radius: 5px; font-size: 0.8rem; cursor: pointer;">
        <a href="#email-subheader" style="color: white; text-decoration: none;">✉️ Email Filtered Data</a>
    </span>
    """,
    unsafe_allow_html=True
)

# Adjust space after the title
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)



fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]),help="You can find Sample file here. https://github.com/gutlapallihemanth/ExcelSheet_Streamlit/blob/main/Sample_Superstore.csv" )

if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding= "ISO-8859-1")
else:
    # os.chdir(r"/Users/hemanthkumar/Desktop/Projects/Streamlit/")
    df = pd.read_csv("Sample_Superstore.csv")


col1, col2 = st.columns((2))

df["Order Date"] = pd.to_datetime(df["Order Date"])

## Getting min and max dates

startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()   

with col1:
    date1 = pd.to_datetime(st.date_input("Start date",startDate))


with col2:
    date2 = pd.to_datetime(st.date_input("End date",endDate))


df = df[(df["Order Date"] >=  date1) & (df["Order Date"] <= date2)].copy()


st.sidebar.header("Choose your filter: ")

# Pick your region

region = st.sidebar.multiselect("Pick your region ", df["Region"].unique())

if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]


# create for state

state = st.sidebar.multiselect("Pick your State ", df2["State"].unique())


if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]

# create for City

city = st.sidebar.multiselect("Pick your City ", df3["City"].unique())

# filter based on Region, State and City


if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df = df[df["State"].isin(state)]
elif state and city:
    filtered_df = df3[(df2["State"].isin(state)) & (df3["City"].isin(city))]
elif region and city:
    filtered_df = df3[(df["Region"].isin(region)) & (df3["City"].isin(city))]
elif state and region:
    filtered_df = df3[(df2["State"].isin(state)) & (df["Region"].isin(region))]
elif city:
    filtered_df = df3[df3["City"].isin(city)]
else:
    filtered_df = df3[(df3["State"].isin(state))&(df3["Region"].isin(region))&(df3["City"].isin(city))]

## Column Chart for category

category_df = filtered_df.groupby(by = ["Category"], as_index= False)["Sales"].sum()


with col1:
    st.subheader("Category wise Sales")
    fig = px.bar(category_df,x = "Category", y = "Sales", text=['${:,.2f}'.format(x) for x in category_df["Sales"]],
                 template= "seaborn")
    st.plotly_chart(fig, use_container_width= True, height= 200 )

with col2:
    st.subheader("Region wise Sales")
    fig = px.pie(filtered_df, values = "Sales", names = "Region", hole=0.5)
    fig.update_traces(text = filtered_df["Region"], textposition = "outside")
    st.plotly_chart(fig, use_container_width=True)


### Download the Data 

cl1,cl2 = st.columns((2))

with cl1:
    with st.expander("Category_ViewData"):
        st.write(category_df.style.background_gradient(cmap= "Blues"))
        csv = category_df.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Category.csv",mime="text/csv",
                           help = "Click here to download the data as a CSV file")

with cl2:
    with st.expander("Region_ViewData"):
        region = filtered_df.groupby(by = "Region", as_index = False)["Sales"].sum()
        st.write(region.style.background_gradient(cmap= "Oranges"))
        csv = region.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Region.csv",mime="text/csv",
                           help = "Click here to download the data as a CSV file")
        



filtered_df['month_year'] = filtered_df["Order Date"].dt.to_period("M")
st.subheader('Time Series Analysis :chart_with_upwards_trend:')

linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x = "month_year", y = "Sales", labels= {"Sales":"Amount"}, height=500, width= 1000, template="gridon" )
st.plotly_chart(fig2,use_container_width=True)



with st.expander("View Data of Timeseries: "):
        st.write(linechart.T.style.background_gradient(cmap= "Blues"))
        csv = linechart.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Timeseries.csv",mime="text/csv",
                           help = "Click here to download the data as a CSV file")


# Create a Tree Map based on Region, Category, sub-category

st.subheader("Hierarchical view of Sales using Tree Map")
st.caption(":information_source: Zoom into respective Region/Category/Sub Category to have a better View")

fig3 = px.treemap(filtered_df, path=["Region", "Category", "Sub-Category"], values= "Sales", hover_data=["Sales"],
                  color= "Sub-Category")

fig3.update_layout(width = 800, height = 600)

st.plotly_chart(fig3,use_container_width=True)


chart1, chart2 = st.columns((2))

with chart1:
    st.subheader("Segment wise Sales")
    fig = px.pie(filtered_df, values = "Sales", names = "Segment", template="plotly_dark")
    fig.update_traces(text = filtered_df["Segment"], textposition = "inside")
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader("Category wise Sales")
    fig = px.pie(filtered_df, values = "Sales", names = "Category", template="gridon")
    fig.update_traces(text = filtered_df["Category"], textposition = "inside")
    st.plotly_chart(fig, use_container_width=True)


import plotly.figure_factory as ff

st.subheader(":point_down: Month Wise Sub-Category Sales Summary")

with st.expander("Summary Table"):
    df_sample = df[0:5][["Region","State","City","Category","Sales","Profit","Quantity"]]
    fig = ff.create_table(df_sample, colorscale="cividis")
    st.plotly_chart(fig,use_container_width=True)  

    st.markdown("Month Wise sub-Cateogory Table")

    filtered_df["month"] = filtered_df["Order Date"].dt.month_name()

    sub_category_Year = pd.pivot_table(data=filtered_df, values="Sales", index= ["Sub-Category"], columns="month")
    st.write(sub_category_Year.style.background_gradient(cmap="Blues"))


# Create a Scatter Plot

data1 = px.scatter(filtered_df, x= "Sales", y = "Profit", size= "Quantity" )
data1['layout'].update(title = "Relationship between Sales and Profit using Scatter Plot",
                       titlefont= dict(size= 20), xaxis = dict(title = "Sales", titlefont = dict(size = 19)),
                       yaxis = dict(title = "Profit", titlefont = dict(size = 19)))

st.plotly_chart(data1,use_container_width=True)


## Download overall dataset

with st.expander("View Data"):
    st.write(filtered_df.iloc[:20,:].style.background_gradient(cmap= "Oranges",subset=['Sales', 'Profit', 'Quantity','Discount']))


## Download Original Dataset

csv = filtered_df.to_csv(index = False).encode('utf-8')
st.download_button("Download Data", data = csv, file_name = "FilteredDataset.csv",mime="text/csv",
                           help = "Click here to download the data as a CSV file")


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



# The subheader with the anchor for navigation
st.markdown("<a name='email-subheader'></a>", unsafe_allow_html=True)
st.subheader(":point_down: Send Data Via Email :e-mail:")

# Taking inputs
email_sender = st.text_input('From')
email_receiver = st.text_input('To')
subject = st.text_input('Subject')
body = st.text_area('Body')
password = st.text_input('Password', type="password",help="You Should create Google App Passsword and then use it here.") 
# Create an expander with help info
with st.expander("Password requirements"):
    st.markdown("""
    Your password should:
    - You Should create Google App Passsword and then use it here.
    - For more details, [click here](https://support.google.com/accounts/answer/185833?visit_id=638317921238722936-2497796308&p=InvalidSecondFactor&rd=1)
    """)

if st.button("Send Email"):
    csv = filtered_df.to_csv(index=False)
    csv_bytes = csv.encode()

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
            

    # Attach CSV to the email
    mime_base = MIMEBase('application', 'octet-stream')
    mime_base.set_payload(csv_bytes)
    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', 'attachment; filename="filtereddf.csv"')
    msg.attach(mime_base)    

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f":no_entry: Error occured please try again : {e}")



# Add the follow buttons at the end
# st.markdown("""
# ### Follow me on:
# <a href="https://medium.com/@hemanthgutlapalli0301" target="_blank"><img src="https://img.icons8.com/ios-filled/50/000000/medium-logo.png" width=30></a>
# <a href="https://www.linkedin.com/in/hemanthgutlapalli/" target="_blank"><img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" width=30></a>
# <a href="https://github.com/gutlapallihemanth" target="_blank"><img src="https://img.icons8.com/ios-filled/50/000000/github.png" width=30></a>
# """, unsafe_allow_html=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

