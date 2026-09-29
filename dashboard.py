from pathlib import Path
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ============================================================
# SMART HR ANALYTICS - CIPAT DASHBOARD
# Presentation layer for the existing HR Analytics project.
# Run: streamlit run dashboard.py
# ============================================================

st.set_page_config(page_title="Smart HR Analytics", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "dataset" / "employee_data.csv"
CRUD_FILE = BASE / "output" / "hr_employee_records.csv"
SCRAPED_FILE = BASE / "output" / "scraped_hr_information.txt"

# Project-consistent light theme
NAVY = "#173B6C"
DARK = "#102A4C"
BLUE = "#2F5B9A"
LIGHT_BLUE = "#8DB7E3"
PALE_BLUE = "#EAF3FB"
RED = "#C6534F"
PALE_RED = "#FBEDEC"
GREEN = "#2E7D5B"
PALE_GREEN = "#EAF6F0"
GREY = "#40566F"
BG = "#F4F7FB"
WHITE = "#FFFFFF"
BORDER = "#D9E2EC"

st.markdown(f"""
<style>
html,body,[class*="css"]{{font-family:"Segoe UI",Arial,sans-serif;}}
.stApp,[data-testid="stAppViewContainer"]{{background:{BG};color:{DARK};}}
[data-testid="stHeader"]{{background:rgba(244,247,251,.97);border-bottom:1px solid {BORDER};}}
[data-testid="stSidebar"]{{background:{WHITE};border-right:1px solid {BORDER};}}
[data-testid="stSidebar"] *{{color:{DARK};}}
.block-container{{max-width:1320px;padding-top:2rem;padding-bottom:2.5rem;}}
.sidebar-brand{{padding:8px 4px 18px;border-bottom:1px solid {BORDER};margin-bottom:18px;}}
.kicker,.sidebar-kicker{{color:{BLUE};font-size:11px;font-weight:800;letter-spacing:2.2px;}}
.sidebar-title{{color:{DARK};font-size:20px;font-weight:800;margin-top:5px;}}
.sidebar-subtitle{{color:{GREY};font-size:12px;line-height:1.45;margin-top:7px;}}
.sidebar-status{{margin-top:22px;padding:13px 14px;border:1px solid #BFE4D1;background:{PALE_GREEN};border-radius:10px;color:{GREEN};font-size:12px;font-weight:700;}}
.sidebar-count{{color:{GREY};font-size:11px;margin-top:8px;line-height:1.45;}}
.page-title{{color:{DARK};font-size:34px;font-weight:800;line-height:1.12;margin:2px 0 0;}}
.page-subtitle{{color:{GREY};font-size:14px;line-height:1.5;margin:8px 0 22px;}}
.section-title{{color:{DARK};font-size:18px;font-weight:800;margin:26px 0 12px;}}
.metric{{background:{WHITE};border:1px solid {BORDER};border-top:3px solid {BLUE};border-radius:12px;padding:17px 18px 15px;min-height:112px;box-shadow:0 4px 14px rgba(23,59,108,.06);}}
.metric.red{{border-top-color:{RED};}}
.metric-label{{color:{GREY};font-size:11px;font-weight:700;margin-bottom:8px;}}
.metric-value{{color:{DARK};font-size:26px;font-weight:800;line-height:1;margin-bottom:9px;}}
.metric-desc{{color:{GREY};font-size:10px;line-height:1.4;}}
.card{{background:{WHITE};border:1px solid {BORDER};border-radius:12px;padding:17px 18px;box-shadow:0 4px 14px rgba(23,59,108,.05);margin-bottom:12px;}}
.card-title{{color:{DARK};font-size:14px;font-weight:800;margin-bottom:7px;}}
.card-text{{color:{GREY};font-size:12px;line-height:1.55;}}
.callout{{background:{PALE_BLUE};border-left:4px solid {BLUE};border-radius:9px;padding:15px 17px;margin:12px 0;}}
.red-callout{{background:{PALE_RED};border-left:4px solid {RED};border-radius:9px;padding:15px 17px;margin:12px 0;}}
.footer{{border-top:1px solid {BORDER};margin-top:30px;padding:16px 0 8px;text-align:center;color:{GREY};font-size:10px;}}
.stPlotlyChart{{background:{WHITE};border:1px solid {BORDER};border-radius:12px;padding:8px;box-shadow:0 4px 14px rgba(23,59,108,.05);}}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    if not DATA_FILE.exists():
        return None
    df = pd.read_csv(DATA_FILE)
    if "Resigned" in df.columns:
        df["Resigned_Flag"] = df["Resigned"].astype(int)
    if "Overtime_Level" not in df.columns and "Overtime_Hours" in df.columns:
        df["Overtime_Level"] = pd.cut(df["Overtime_Hours"], [-np.inf,5,10,np.inf], labels=["Low","Moderate","High"])
    return df

df = load_data()


def page_header(title, subtitle):
    st.markdown('<div class="kicker">HR ANALYTICS</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def section(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def card(title, text):
    st.markdown(f'<div class="card"><div class="card-title">{title}</div><div class="card-text">{text}</div></div>', unsafe_allow_html=True)


def metric(label, value, desc, red=False):
    cls = "metric red" if red else "metric"
    st.markdown(f'<div class="{cls}"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-desc">{desc}</div></div>', unsafe_allow_html=True)


def pct(x, digits=2):
    return f"{x*100:.{digits}f}%"


def chart_theme(fig, height=360, title=None):
    fig.update_layout(
        height=height, paper_bgcolor=WHITE, plot_bgcolor=WHITE,
        font=dict(family="Segoe UI, Arial", color=DARK, size=12),
        margin=dict(l=48,r=24,t=58,b=48),
        title=dict(text=title, font=dict(size=16,color=DARK), x=.02, xanchor="left") if title else None,
        hoverlabel=dict(bgcolor=WHITE,font_color=DARK,bordercolor=BORDER),
    )
    fig.update_xaxes(showline=False,zeroline=False,gridcolor="#E1E8F0",tickfont=dict(color=DARK,size=10),title_font=dict(color=DARK,size=11))
    fig.update_yaxes(showline=False,zeroline=False,gridcolor="#E1E8F0",tickfont=dict(color=DARK,size=10),title_font=dict(color=DARK,size=11))
    return fig


def show_chart(fig, height=360):
    chart_theme(fig,height)
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})


# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-brand"><div class="sidebar-kicker">HR ANALYTICS</div><div class="sidebar-title">Smart HR Analytics</div><div class="sidebar-subtitle">Employee Attrition Analysis & Workforce Intelligence</div></div>', unsafe_allow_html=True)
    pages=["Dashboard","Process","Dataset","HR Analytics","Machine Learning","CRUD","Web Scraping","Exception Handling","Project Info"]
    selected=st.radio("Navigation",pages,label_visibility="collapsed")
    if df is not None:
        st.markdown('<div class="sidebar-status">Dataset connected</div>',unsafe_allow_html=True)
        st.markdown(f'<div class="sidebar-count">{len(df):,} employee records loaded</div>',unsafe_allow_html=True)
    else:
        st.markdown('<div class="sidebar-status">Dataset not found</div>',unsafe_allow_html=True)
        st.markdown('<div class="sidebar-count">Expected: dataset/employee_data.csv</div>',unsafe_allow_html=True)

if df is None:
    page_header("Smart HR Analytics","Dashboard expects the project dataset at dataset/employee_data.csv.")
    st.error("Dataset file not found. Keep dashboard.py in the project root beside the dataset folder.")
    st.stop()

# Common values from the actual project CSV
total=len(df)
resigned=int(df["Resigned"].astype(bool).sum())
not_resigned=total-resigned
rate=resigned/total
avg_sat=df["Employee_Satisfaction_Score"].mean()
avg_salary=df["Monthly_Salary"].mean()
departments=df["Department"].nunique()

# ============================================================
# DASHBOARD
# ============================================================
if selected=="Dashboard":
    page_header("Smart HR Analytics","Employee attrition analysis, workforce patterns and machine-learning results from the CIPAT Human Resource Analytics project.")
    a,b,c,d=st.columns(4,gap="medium")
    with a: metric("Total Employees",f"{total:,}","Records available in the analytical dataset.")
    with b: metric("Not Resigned",f"{not_resigned:,}","Employees recorded as not resigned.")
    with c: metric("Resigned",f"{resigned:,}","Employees recorded as resigned.",True)
    with d: metric("Resignation Rate",pct(rate),"Historical resignation rate in the dataset.",True)
    st.markdown("<div style='height:8px'></div>",unsafe_allow_html=True)
    a,b,c=st.columns(3,gap="medium")
    with a: metric("Average Satisfaction",f"{avg_sat:.2f}","Mean employee satisfaction score on the 1–5 scale.")
    with b: metric("Average Monthly Salary",f"₹{avg_salary:,.2f}","Mean monthly salary in the dataset.")
    with c: metric("Departments",f"{departments}","Departments represented in the employee dataset.")

    section("Workforce & Attrition Evidence")
    left,right=st.columns([.85,1.45],gap="medium")
    with left:
        fig=go.Figure(go.Pie(labels=["Not Resigned","Resigned"],values=[not_resigned,resigned],hole=.66,sort=False,marker=dict(colors=[BLUE,RED],line=dict(color=WHITE,width=3)),textinfo="percent",textfont=dict(color=WHITE,size=14),hovertemplate="<b>%{label}</b><br>Employees: %{value:,}<br>Share: %{percent}<extra></extra>"))
        fig.add_annotation(x=.5,y=.5,text=f"<b>{rate*100:.1f}%</b><br><span style='font-size:11px'>RESIGNED</span>",showarrow=False,font=dict(color=DARK,size=19))
        fig.update_layout(height=390,paper_bgcolor=WHITE,plot_bgcolor=WHITE,margin=dict(l=20,r=20,t=58,b=20),title=dict(text="Actual Employee Resignation Status",font=dict(size=16,color=DARK),x=.02),legend=dict(orientation="h",y=-.03,x=.5,xanchor="center",font=dict(size=11,color=GREY)))
        st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
    with right:
        dept=(df.assign(Resigned_Flag=df["Resigned"].astype(int)).groupby("Department",as_index=False)["Resigned_Flag"].mean())
        dept["Rate"]=dept["Resigned_Flag"]*100; dept=dept.sort_values(by="Rate")  # type: ignore[call-overload]
        fig=go.Figure(go.Bar(x=dept["Rate"],y=dept["Department"],orientation="h",marker_color=BLUE,text=[f"{v:.2f}%" for v in dept["Rate"]],textposition="outside",textfont=dict(color=DARK,size=10),hovertemplate="<b>%{y}</b><br>Resignation rate: %{x:.2f}%<extra></extra>"))
        fig.update_layout(xaxis_title="Resignation Rate (%)",yaxis_title="",height=390)
        show_chart(fig,390)
    lower,side=st.columns([1.05,.95],gap="medium")
    with lower:
        sat=df["Employee_Satisfaction_Score"].round().value_counts().sort_index()
        fig=go.Figure(go.Bar(x=sat.index.astype(str),y=sat.values,marker_color=BLUE,text=[f"{int(v):,}" for v in sat.values],textposition="outside",textfont=dict(color=DARK,size=10),hovertemplate="Satisfaction score: %{x}<br>Employees: %{y:,}<extra></extra>"))
        fig.update_layout(xaxis_title="Satisfaction Score",yaxis_title="Employees")
        show_chart(fig,350)
        # Note: this chart preserves the same project result; only its rendering changes.
        fig=None
    with side:
        card("Workforce Split","Establishes the not-resigned-to-resigned baseline for the complete employee dataset.")
        card("Department Attrition","Compares resignation rates across departments rather than comparing only department sizes.")
        card("Satisfaction Distribution","Shows employee satisfaction distribution across the five-point satisfaction scale.")
        card("Historical Dataset","Uses the same employee CSV as the existing CIPAT analysis pipeline.")

# ============================================================
# PROCESS
# ============================================================
elif selected=="Process":
    page_header("End-to-End HR Analytics Process","A step-by-step view of how the project moves from raw employee data through analysis, visualization and machine learning.")
    a,b,c=st.columns(3,gap="medium")
    with a: card("Source","Employee CSV used by the existing analytical workflow.")
    with b: card("Pipeline","Load → Clean → Analyze → Visualize → Predict.")
    with c: card("Target","Resigned / Not Resigned binary classification.")
    section("Lifecycle Stages")
    stages=[
        ("1","Data Loading","Load employee_data.csv into a Pandas DataFrame."),
        ("2","Data Exploration","Check shape, columns, data types, missing values, duplicates and summary information."),
        ("3","Data Cleaning","Validate duplicate records, Employee IDs, dates, salary, age, overtime, performance and satisfaction fields."),
        ("4","Data Preprocessing","Create Resigned_Flag and Overtime_Level for downstream analysis."),
        ("5","Statistical Analysis","Calculate mean, median, standard deviation, minimum, maximum and correlations."),
        ("6","Probability Analysis","Calculate overall and conditional resignation probabilities for selected HR groups."),
        ("7","Sampling & Inference","Take a random sample and calculate a 95% confidence interval."),
        ("8","Hypothesis Testing","Use an independent two-sample t-test to compare satisfaction between stayed and resigned employees."),
        ("9","Data Visualization","Create six presentation-ready HR graphs and save them in the graphs folder."),
        ("10","Machine Learning","Use One-Hot Encoding, StandardScaler and Logistic Regression to predict resignation."),
        ("11","CRUD Operations","Create, Read, Update and Delete records in a separate persistent CSV file."),
        ("12","Web Scraping","Use Requests and BeautifulSoup to collect information from a public HR webpage and save it as text."),
        ("13","Exception Handling","Demonstrate FileNotFoundError, KeyError, ValueError and general Exception handling."),
    ]
    for i in range(0,len(stages),2):
        cols=st.columns(2,gap="medium")
        for col,(n,t,desc) in zip(cols,stages[i:i+2]):
            with col:
                st.markdown(f'<div class="card" style="min-height:118px"><div style="display:flex;gap:9px;align-items:center;margin-bottom:8px"><div style="width:25px;height:25px;border-radius:50%;background:{PALE_BLUE};color:{BLUE};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:11px">{n}</div><div class="card-title" style="margin:0">{t}</div></div><div class="card-text">{desc}</div></div>',unsafe_allow_html=True)

# ============================================================
# DATASET
# ============================================================
elif selected=="Dataset":
    page_header("Employee Dataset","The dashboard uses the same employee CSV that feeds the existing CIPAT analysis pipeline.")
    a,b,c,d=st.columns(4,gap="medium")
    with a: metric("Records",f"{len(df):,}","Rows in the analytical dataset.")
    with b: metric("Original Attributes","20","Original dataset columns.")
    with c: metric("Missing Values",f"{int(df.isna().sum().sum()):,}","Missing values in the loaded dataset.")
    with d: metric("Duplicate Rows",f"{int(df.duplicated().sum()):,}","Duplicate records in the loaded dataset.")
    section("Dataset Preview")
    st.dataframe(df.head(10),use_container_width=True,hide_index=True)
    section("Original Dataset Attributes")
    meta=pd.DataFrame([{"Attribute":x,"Data Type":str(df[x].dtype),"Missing Values":int(df[x].isna().sum())} for x in df.columns])
    st.dataframe(meta,use_container_width=True,hide_index=True)

# ============================================================
# HR ANALYTICS
# ============================================================
elif selected=="HR Analytics":
    page_header("HR Analytics & Evidence","Statistical analysis, probability, sampling and hypothesis-testing results from the existing project.")
    high=df["Overtime_Level"].astype(str).eq("High")
    low=df["Employee_Satisfaction_Score"]<=2
    long=df["Work_Hours_Per_Week"]>50
    high_n=int(high.sum()); high_r=int(df.loc[high,"Resigned"].astype(bool).sum()); high_rate=high_r/high_n
    low_n=int(low.sum()); low_r=int(df.loc[low,"Resigned"].astype(bool).sum()); low_rate=low_r/low_n
    long_n=int(long.sum()); long_r=int(df.loc[long,"Resigned"].astype(bool).sum()); long_rate=long_r/long_n
    a,b,c=st.columns(3,gap="medium")
    with a: metric("High Overtime",f"{high_n/total*100:.2f}%",f"Employees in group. P(Resigned | High Overtime) = {high_rate*100:.2f}%.")
    with b: metric("Low Satisfaction",f"{low_n/total*100:.2f}%",f"Employees with satisfaction ≤ 2. P(Resigned | Low Satisfaction) = {low_rate*100:.2f}%.")
    with c: metric("More Than 50 Hours",f"{long_n/total*100:.2f}%",f"Employees working >50 hours/week. P(Resigned | >50 Hours) = {long_rate*100:.2f}%.")
    section("Department Resignation Rate")
    dept=(df.assign(Resigned_Flag=df["Resigned"].astype(int)).groupby("Department",as_index=False).agg(Employees=("Employee_ID","count"),Resigned=("Resigned_Flag","sum"),Resignation_Rate=("Resigned_Flag","mean")))
    dept["Resignation_Rate"]*=100; dept=dept.sort_values("Resignation_Rate",ascending=False)
    fig=go.Figure(go.Bar(x=dept["Resignation_Rate"],y=dept["Department"],orientation="h",marker_color=BLUE,text=[f"{v:.2f}%" for v in dept["Resignation_Rate"]],textposition="outside",textfont=dict(color=DARK,size=10),customdata=np.column_stack([dept["Employees"],dept["Resigned"]]),hovertemplate="<b>%{y}</b><br>Employees: %{customdata[0]:,}<br>Resigned: %{customdata[1]:,}<br>Rate: %{x:.2f}%<extra></extra>"))
    fig.update_layout(xaxis_title="Resignation Rate (%)",yaxis_title="")
    show_chart(fig,420)
    section("Conditional Resignation Probability")
    a,b,c,d=st.columns(4,gap="medium")
    with a: metric("Overall Resignation",pct(rate),"P(Resigned).")
    with b: metric("P(Resigned | High Overtime)",f"{high_rate*100:.2f}%",f"{high_n:,} employees in the high-overtime group.")
    with c: metric("P(Resigned | Low Satisfaction)",f"{low_rate*100:.2f}%",f"{low_n:,} employees with satisfaction ≤ 2.")
    with d: metric("P(Resigned | >50 Hours)",f"{long_rate*100:.2f}%",f"{long_n:,} employees working more than 50 hours.")
    section("Satisfaction & Overtime")
    a,b=st.columns(2,gap="medium")
    with a:
        sat=(df.assign(Satisfaction_Score=df["Employee_Satisfaction_Score"].round().astype(int),Resigned_Flag=df["Resigned"].astype(int)).groupby("Satisfaction_Score",as_index=False).agg(Resignation_Rate=("Resigned_Flag","mean"),Employees=("Resigned_Flag","size")))
        sat["Resignation_Rate"]*=100
        fig=go.Figure(go.Bar(x=sat["Satisfaction_Score"].astype(str),y=sat["Resignation_Rate"],marker_color=BLUE,text=[f"{v:.2f}%" for v in sat["Resignation_Rate"]],textposition="outside",textfont=dict(color=DARK,size=10),customdata=sat["Employees"],hovertemplate="Satisfaction: %{x}<br>Employees: %{customdata:,}<br>Rate: %{y:.2f}%<extra></extra>"))
        fig.update_layout(xaxis_title="Satisfaction Score",yaxis_title="Resignation Rate (%)")
        show_chart(fig,360)
    with b:
        order=["Low","Moderate","High"]
        ot=(df.assign(Resigned_Flag=df["Resigned"].astype(int)).groupby("Overtime_Level",as_index=False,observed=True).agg(Resignation_Rate=("Resigned_Flag","mean"),Employees=("Resigned_Flag","size")))
        ot["Overtime_Level"]=ot["Overtime_Level"].astype(str); ot["Order"]=ot["Overtime_Level"].map({x:i for i,x in enumerate(order)}).fillna(99); ot=ot.sort_values("Order"); ot["Resignation_Rate"]*=100
        fig=go.Figure(go.Bar(x=ot["Overtime_Level"],y=ot["Resignation_Rate"],marker_color=BLUE,text=[f"{v:.2f}%" for v in ot["Resignation_Rate"]],textposition="outside",textfont=dict(color=DARK,size=10),customdata=ot["Employees"],hovertemplate="Overtime level: %{x}<br>Employees: %{customdata:,}<br>Rate: %{y:.2f}%<extra></extra>"))
        fig.update_layout(xaxis_title="Overtime Level",yaxis_title="Resignation Rate (%)")
        show_chart(fig,360)
    section("Average Satisfaction by Resignation Status")
    status=df.assign(Status=np.where(df["Resigned"].astype(bool),"Resigned","Not Resigned")).groupby("Status",as_index=False)["Employee_Satisfaction_Score"].mean()
    status["order"]=status["Status"].map({"Not Resigned":0,"Resigned":1}); status=status.sort_values(by="order")  # type: ignore[call-overload]
    fig=go.Figure(go.Bar(x=status["Status"],y=status["Employee_Satisfaction_Score"],marker_color=[BLUE if x=="Not Resigned" else RED for x in status["Status"]],text=[f"{v:.2f}" for v in status["Employee_Satisfaction_Score"]],textposition="outside",textfont=dict(color=DARK,size=11),hovertemplate="%{x}<br>Average satisfaction: %{y:.2f}<extra></extra>"))
    fig.update_layout(xaxis_title="Employee Status",yaxis_title="Average Satisfaction",yaxis=dict(range=[0,5]))
    show_chart(fig,370)
    section("Sampling & Inference")
    a,b,c,d=st.columns(4,gap="medium")
    with a: metric("Population",f"{total:,}",f"Population resignation rate: {rate*100:.2f}%.")
    with b: metric("Random Sample","1,000","Sample resignation rate: 9.30%.")
    with c: metric("95% Confidence Interval","7.50% – 11.10%","Interval estimated from the random sample.")
    with d: metric("Sample vs Population","0.30 pp","Difference between sample and population rate.")
    section("Hypothesis Testing")
    a,b,c,d=st.columns(4,gap="medium")
    with a: metric("Stayed Satisfaction","3.26","Average satisfaction of employees who did not resign.")
    with b: metric("Resigned Satisfaction","1.93","Average satisfaction of employees who resigned.")
    with c: metric("T-Statistic","251.8024","Independent two-sample t-test statistic.")
    with d: metric("P-Value","0.000000","Reported p-value at significance level α = 0.05.",True)
    st.markdown('<div class="card" style="margin-top:14px"><div class="card-title">Hypothesis Test Result</div><div class="card-text">The project uses an independent two-sample t-test to compare employee satisfaction between stayed and resigned employees. The recorded p-value is below 0.05, so the project rejects H0 at α = 0.05.</div></div>',unsafe_allow_html=True)

# ============================================================
# MACHINE LEARNING
# ============================================================
elif selected=="Machine Learning":
    page_header("Employee Attrition Prediction","The existing Logistic Regression pipeline used to classify resignation status from employee attributes.")
    section("Model Pipeline")
    steps=[("1","Feature Selection","16 input features are used."),("2","Categorical Encoding","One-Hot Encoding is applied to categorical variables."),("3","Numerical Scaling","Numerical variables are standardized using StandardScaler."),("4","Train/Test Split","80% for training and 20% for testing."),("5","Model Training","Logistic Regression is trained using prepared features."),("6","Prediction","The trained model predicts resignation on unseen test data."),("7","Evaluation","Accuracy, precision, recall and F1-score are calculated."),("8","Confusion Matrix","True/false positive and negative predictions are displayed.")]
    for i in range(0,len(steps),2):
        cols=st.columns(2,gap="medium")
        for col,(n,t,desc) in zip(cols,steps[i:i+2]):
            with col:
                st.markdown(f'<div class="card" style="min-height:112px"><div style="display:flex;gap:9px;align-items:center;margin-bottom:8px"><div style="width:25px;height:25px;border-radius:50%;background:{PALE_BLUE};color:{BLUE};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:11px">{n}</div><div class="card-title" style="margin:0">{t}</div></div><div class="card-text">{desc}</div></div>',unsafe_allow_html=True)
    section("Model Performance")
    a,b,c,d=st.columns(4,gap="medium")
    with a: metric("Accuracy","94.83%","Overall classification accuracy.")
    with b: metric("Precision","64.05%","Precision for resignation classification.")
    with c: metric("Recall","97.00%","Recall for resignation classification.")
    with d: metric("F1-Score","77.15%","Harmonic mean of precision and recall.")
    section("Confusion Matrix")
    cm=np.array([[17220,980],[54,1746]])
    fig=go.Figure(go.Heatmap(z=cm,x=["Predicted Not Resigned","Predicted Resigned"],y=["Actual Not Resigned","Actual Resigned"],colorscale=[[0,"#EAF3FB"],[.35,"#8DB7E3"],[1,BLUE]],text=cm,texttemplate="%{text:,}",textfont=dict(color=WHITE,size=15),showscale=False,hovertemplate="Actual: %{y}<br>Prediction: %{x}<br>Employees: %{z:,}<extra></extra>"))
    fig.add_annotation(x="Predicted Not Resigned",y="Actual Resigned",text="<b>54</b>",showarrow=False,font=dict(color=DARK,size=15))
    fig.update_layout(height=410,paper_bgcolor=WHITE,plot_bgcolor=WHITE,margin=dict(l=70,r=25,t=58,b=70),title=dict(text="Confusion Matrix",font=dict(size=16,color=DARK),x=.02),font=dict(family="Segoe UI,Arial",color=DARK))
    fig.update_xaxes(tickfont=dict(color=GREY,size=10)); fig.update_yaxes(tickfont=dict(color=DARK,size=10),autorange="reversed")
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
    section("Classification Report")
    report=pd.DataFrame({"Class":["Not Resigned","Resigned","Macro Avg","Weighted Avg"],"Precision":[1.00,.64,.82,.96],"Recall":[.95,.97,.96,.95],"F1-Score":[.97,.77,.87,.95],"Support":[18200,1800,20000,20000]})
    st.dataframe(report,use_container_width=True,hide_index=True)
    section("Model Inputs")
    features=["Department","Gender","Age","Years_At_Company","Education_Level","Performance_Score","Monthly_Salary","Work_Hours_Per_Week","Projects_Handled","Overtime_Hours","Sick_Days","Remote_Work_Frequency","Team_Size","Training_Hours","Promotions","Employee_Satisfaction_Score"]
    cols=st.columns(4,gap="small")
    for i,x in enumerate(features):
        with cols[i%4]: st.markdown(f'<div style="background:{WHITE};border:1px solid {BORDER};border-radius:8px;padding:10px;margin-bottom:7px;color:{DARK};font-size:11px;font-weight:600">{x}</div>',unsafe_allow_html=True)
    card("Model Explanation","The project uses Logistic Regression with One-Hot Encoding and StandardScaler. The dashboard displays the existing model evaluation results.")

# ============================================================
# CRUD
# ============================================================
elif selected=="CRUD":
    page_header("Employee Record Management","Create, Read, Update and Delete operations using a separate persistent CSV storage file.")
    a,b=st.columns(2,gap="medium")
    with a: card("Original Analytical Dataset","dataset/employee_data.csv<br><br>This file is used by the analytical workflow and is not modified by CRUD operations.")
    with b: card("CRUD Storage","output/hr_employee_records.csv<br><br>CRUD changes are written to this separate CSV file using Pandas file handling.")
    section("CRUD Workflow")
    items=[("CREATE","Add an employee record and save it to the CRUD CSV."),("READ","Read employee records from the CRUD CSV."),("UPDATE","Modify an existing employee record and save the change."),("DELETE","Remove an employee record and save the updated CSV.")]
    cols=st.columns(4,gap="medium")
    for col,(t,desc) in zip(cols,items):
        with col: card(t,desc)
    section("Permanent Storage")
    card("How the project stores CRUD changes","The CRUD module writes changes to output/hr_employee_records.csv. The original analytical dataset remains unchanged. The demonstration creates a test record, reads it, updates it, reads the update, deletes it and reads the final storage state.")
    if CRUD_FILE.exists():
        try:
            crud=pd.read_csv(CRUD_FILE)
            if crud.empty: st.info("The CRUD storage file currently contains no records.")
            else: st.dataframe(crud,use_container_width=True,hide_index=True)
        except Exception as e: st.error(f"Unable to read CRUD storage: {e}")
    else: st.info("The CRUD storage file will be created when the CRUD module is executed.")

# ============================================================
# WEB SCRAPING
# ============================================================
elif selected=="Web Scraping":
    page_header("HR Web Scraping","Requests and BeautifulSoup collect information from a public HR webpage and save the extracted content as text.")
    section("Scraping Pipeline")
    steps=[("01","HTTP Request","Requests sends an HTTP request to the public webpage."),("02","HTML Response","The webpage returns its HTML content."),("03","HTML Parsing","BeautifulSoup parses the returned HTML."),("04","Information Extraction","Page title, headings and HR-related paragraph information are extracted."),("05","File Handling","The extracted information is written to a text file.")]
    for i in range(0,len(steps),2):
        cols=st.columns(2,gap="medium")
        for col,(n,t,desc) in zip(cols,steps[i:i+2]):
            with col: card(f"{n}  {t}",desc)
    section("Source Webpage")
    card("SHRM — Understanding the HR Lifecycle: From Hiring to Exit","The existing web-scraping module accesses a public HR webpage, parses its HTML with BeautifulSoup and saves extracted information to output/scraped_hr_information.txt.")
    section("Scraped Output")
    if SCRAPED_FILE.exists():
        try: st.text_area("Saved scraping output",SCRAPED_FILE.read_text(encoding="utf-8"),height=360)
        except Exception as e: st.error(f"Unable to read scraping output: {e}")
    else: st.info("The scraping output file will appear after the web-scraping module is executed.")

# ============================================================
# EXCEPTION HANDLING
# ============================================================
elif selected=="Exception Handling":
    page_header("Exception Handling","Explicit exception demonstrations used to show safe handling of common runtime errors.")
    items=[("FileNotFoundError","Handles a missing employee data file."),("KeyError","Handles an attempt to access a column that does not exist."),("ValueError","Handles invalid input such as converting non-numeric text to an integer."),("General Exception","Catches unexpected runtime errors.")]
    a,b=st.columns(2,gap="medium")
    for i,(t,desc) in enumerate(items):
        with (a if i%2==0 else b):
            st.markdown(f'<div class="card" style="min-height:112px"><div style="display:flex;gap:9px;align-items:center;margin-bottom:8px"><div class="card-title" style="margin:0">{t}</div><span style="background:{PALE_BLUE};color:{BLUE};border-radius:20px;padding:3px 8px;font-size:9px;font-weight:800">HANDLED</span></div><div class="card-text">{desc}</div></div>',unsafe_allow_html=True)
    section("Simple Exception Handling Explanation")
    st.markdown(f'<div style="background:{DARK};border-radius:12px;padding:22px 24px"><div style="color:{WHITE};font-size:15px;font-weight:800;margin-bottom:9px">Safe Runtime Error Handling</div><div style="color:#DCE7F3;font-size:12px;line-height:1.6">Exception handling prevents common runtime errors from terminating the program unexpectedly. The project demonstrates different exception types so the concept is clearly visible during the CIPAT evaluation.</div></div>',unsafe_allow_html=True)

# ============================================================
# PROJECT INFO
# ============================================================
elif selected=="Project Info":
    page_header("Smart HR Analytics","Employee Attrition Analysis & Workforce Intelligence — CIPAT Human Resource Analytics Project.")
    section("Project Objective")
    card("Objective","Analyze employee information to identify HR patterns, resignation-related factors and employee attrition patterns using Python.")
    section("Dataset")
    a,b,c=st.columns(3,gap="medium")
    with a: metric("Dataset Type","Employee CSV","Historical employee records used by the project.")
    with b: metric("Original Attributes","20","Attributes available before preprocessing.")
    with c: metric("Analytical Area","HR","Human Resource Analytics and employee attrition.")
    section("Core Technologies")
    tech=["Python","Pandas","NumPy","SciPy","Matplotlib","Seaborn","Scikit-learn","Requests","BeautifulSoup","Streamlit","Plotly"]
    cols=st.columns(4,gap="small")
    for i,x in enumerate(tech):
        with cols[i%4]: st.markdown(f'<div style="background:{WHITE};border:1px solid {BORDER};border-radius:8px;padding:11px;margin-bottom:8px;text-align:center;color:{DARK};font-size:11px;font-weight:700">{x}</div>',unsafe_allow_html=True)
    section("CIPAT Concepts Implemented")
    concepts=["Python Core Concepts","Data Structures","Python Libraries","Custom Modules","Exception Handling","Web Scraping","File Handling","CRUD Operations","NumPy","SciPy","Pandas","Data Preprocessing","Data Visualization","Statistical Analysis","Probability","Sampling & Inference","Hypothesis Testing","Machine Learning"]
    st.dataframe(pd.DataFrame({"No.":range(1,19),"CIPAT Concept":concepts,"Status":["Implemented"]*18}),use_container_width=True,hide_index=True)
    section("Additional Implementations")
    card("Project Components","CRUD operations, file handling, web scraping and exception handling are presented as dedicated dashboard sections so each implementation can be demonstrated directly during the CIPAT evaluation.")

st.markdown('<div class="footer">Smart HR Analytics • CIPAT Human Resource Analytics Project • Python for Data Science</div>',unsafe_allow_html=True)
