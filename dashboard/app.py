"""
IBM Data Analyst Capstone: Executive Technology Trends Dashboard
Author: Raghavendra Golla
Role: Associate Data Analyst
Organization: Global IT & Management Consulting Practice
"""

import os
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# -----------------------------------------------------------------------------
# Configuration & Theming
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Technology Trends & Skills Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom enterprise styling
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .metric-card {
        background-color: white;
        border-radius: 8px;
        padding: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 5px solid #1f77b4;
    }
    .metric-value { font-size: 28px; font-weight: 700; color: #1a202c; }
    .metric-label { font-size: 13px; color: #718096; text-transform: uppercase; letter-spacing: 0.5px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Database Connection
# -----------------------------------------------------------------------------
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "capstone.db")
if not os.path.exists(DB_PATH):
    DB_PATH = "data/processed/capstone.db"


@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df_resp = pd.read_sql_query("SELECT * FROM respondents", conn)
    df_lang = pd.read_sql_query("SELECT * FROM respondent_languages", conn)
    df_db = pd.read_sql_query("SELECT * FROM respondent_databases", conn)
    df_ide = pd.read_sql_query("SELECT * FROM respondent_dev_environments", conn)
    df_demand = pd.read_sql_query("SELECT * FROM job_postings_demand", conn)
    conn.close()
    return df_resp, df_lang, df_db, df_ide, df_demand


df_resp, df_lang, df_db, df_ide, df_demand = load_data()

# -----------------------------------------------------------------------------
# Sidebar Controls
# -----------------------------------------------------------------------------
st.sidebar.title("🔍 Strategic Filters")
st.sidebar.markdown("Filter developer demographics across global consulting engagements.")

# Country Filter
top_countries = ["All"] + list(df_resp["Country"].value_counts().head(10).index)
selected_country = st.sidebar.selectbox("Geographic Market (Country)", top_countries)

# Work Location Filter
work_locations = ["All"] + list(df_resp["WorkLoc"].dropna().unique())
selected_loc = st.sidebar.selectbox("Working Model", work_locations)

# Apply Filters
filtered_resp = df_resp.copy()
if selected_country != "All":
    filtered_resp = filtered_resp[filtered_resp["Country"] == selected_country]
if selected_loc != "All":
    filtered_resp = filtered_resp[filtered_resp["WorkLoc"] == selected_loc]

filtered_respondent_ids = set(filtered_resp["Respondent"])
filtered_lang = df_lang[df_lang["Respondent"].isin(filtered_respondent_ids)]
filtered_db = df_db[df_db["Respondent"].isin(filtered_respondent_ids)]
filtered_ide = df_ide[df_ide["Respondent"].isin(filtered_respondent_ids)]

# -----------------------------------------------------------------------------
# Header & KPI Cards
# -----------------------------------------------------------------------------
st.title("🌐 Technology Trends & Skills Intelligence Dashboard")
st.markdown("**IBM Data Analyst Professional Certificate Capstone** | Executive Workforce Strategy")

col1, col2, col3, col4, col5 = st.columns(5)

total_devs = len(filtered_resp)
median_comp = filtered_resp["ConvertedComp"].median()
top_lang = filtered_lang[filtered_lang["Usage_Status"] == "Current"]["Language"].mode()
top_lang_str = top_lang.iloc[0] if not top_lang.empty else "N/A"
top_desired_db = filtered_db[filtered_db["Usage_Status"] == "Desired"]["Database"].mode()
top_db_str = top_desired_db.iloc[0] if not top_desired_db.empty else "N/A"
top_ide = filtered_ide["IDE"].mode()
top_ide_str = top_ide.iloc[0] if not top_ide.empty else "N/A"

with col1:
    st.metric("Total Developers", f"{total_devs:,}")
with col2:
    st.metric("Median Salary (USD)", f"${median_comp:,.0f}" if pd.notna(median_comp) else "N/A")
with col3:
    st.metric("Top Current Language", top_lang_str)
with col4:
    st.metric("Top Desired Database", top_db_str)
with col5:
    st.metric("Top Development Tool", top_ide_str)

st.markdown("---")

# -----------------------------------------------------------------------------
# Multi-Tab Layout
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Programming Languages",
    "🗄️ Database Migrations",
    "💼 Supply vs. Demand Gap",
    "🛠️ IDEs & Demographics",
    "💡 Executive Insights & Actions"
])

# -----------------------------------------------------------------------------
# Tab 1: Programming Languages
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("Programming Language Momentum: Current Adoption vs. Future Desire")
    col_l1, col_l2 = st.columns(2)
    
    curr_counts = filtered_lang[filtered_lang["Usage_Status"] == "Current"]["Language"].value_counts().head(10).reset_index()
    curr_counts.columns = ["Language", "Current_Count"]
    
    des_counts = filtered_lang[filtered_lang["Usage_Status"] == "Desired"]["Language"].value_counts().head(10).reset_index()
    des_counts.columns = ["Language", "Desired_Count"]
    
    with col_l1:
        fig_curr = px.bar(
            curr_counts, x="Current_Count", y="Language", orientation="h",
            title="Top 10 Currently Used Languages", color="Current_Count",
            color_continuous_scale="Blues", text="Current_Count"
        )
        fig_curr.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_curr, use_container_width=True)
        
    with col_l2:
        fig_des = px.bar(
            des_counts, x="Desired_Count", y="Language", orientation="h",
            title="Top 10 Desired Languages for Next Year", color="Desired_Count",
            color_continuous_scale="Oranges", text="Desired_Count"
        )
        fig_des.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_des, use_container_width=True)

# -----------------------------------------------------------------------------
# Tab 2: Databases
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("Enterprise Database Architectures: Production Deployments vs. Migration Intent")
    
    curr_db = filtered_db[filtered_db["Usage_Status"] == "Current"]["Database"].value_counts().head(10).reset_index()
    curr_db.columns = ["Database", "Count"]
    curr_db["Status"] = "Currently Deployed"
    
    des_db = filtered_db[filtered_db["Usage_Status"] == "Desired"]["Database"].value_counts().head(10).reset_index()
    des_db.columns = ["Database", "Count"]
    des_db["Status"] = "Aspirational (Desired)"
    
    db_combined = pd.concat([curr_db, des_db], ignore_index=True)
    
    fig_db = px.bar(
        db_combined, x="Count", y="Database", color="Status", barmode="group",
        title="Top 10 Databases: Current Production Share vs. Future Demand Shift",
        color_discrete_map={"Currently Deployed": "#2ca02c", "Aspirational (Desired)": "#d62728"},
        orientation="h"
    )
    fig_db.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig_db, use_container_width=True)
    
    st.info("💡 **Architectural Migration Finding**: While MySQL leads current production deployments, **PostgreSQL** surpasses all databases in future developer desire (38.0%), followed by MongoDB and Redis.")

# -----------------------------------------------------------------------------
# Tab 3: Supply vs. Demand Gap
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Labor Market Reality: Developer Skills vs. Employer Requisitions")
    st.markdown("Comparing developer survey skill share against **27,005 actual tech job postings**.")
    
    # Calculate developer supply share
    dev_skill_share = filtered_lang[filtered_lang["Usage_Status"] == "Current"]["Language"].value_counts(normalize=True) * 100
    df_dev_share = dev_skill_share.reset_index()
    df_dev_share.columns = ["Technology", "Developer_Supply_Pct"]

    # Case-insensitive join key so labels like "SQL" (survey) and "sql" (job
    # postings) still match, matching the LOWER()-normalized join in sql/analysis.sql.
    df_dev_share["_join_key"] = df_dev_share["Technology"].str.lower()
    df_demand_keyed = df_demand.copy()
    df_demand_keyed["_join_key"] = df_demand_keyed["Technology"].str.lower()
    gap_df = pd.merge(
        df_dev_share, df_demand_keyed, on="_join_key", how="inner", suffixes=("", "_job")
    ).drop(columns=["_join_key", "Technology_job"])
    gap_melt = gap_df.melt(id_vars="Technology", value_vars=["Developer_Supply_Pct", "Market_Demand_Share_Pct"],
                           var_name="Metric", value_name="Share_Pct")
    gap_melt["Metric"] = gap_melt["Metric"].map({"Developer_Supply_Pct": "Developer Skill Share (%)",
                                                 "Market_Demand_Share_Pct": "Employer Hiring Demand (%)"})
    
    fig_gap = px.bar(
        gap_melt, x="Share_Pct", y="Technology", color="Metric", barmode="group",
        title="Skills Gap Comparison (Developer Supply vs. Employer Requisitions)",
        color_discrete_map={"Developer Skill Share (%)": "#1f77b4", "Employer Hiring Demand (%)": "#e377c2"},
        orientation="h"
    )
    fig_gap.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig_gap, use_container_width=True)

# -----------------------------------------------------------------------------
# Tab 4: IDEs & Demographics
# -----------------------------------------------------------------------------
with tab4:
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        st.subheader("Development Environment (IDE) Adoption")
        ide_counts = filtered_ide["IDE"].value_counts().head(8).reset_index()
        ide_counts.columns = ["IDE", "Count"]
        fig_ide = px.pie(
            ide_counts, names="IDE", values="Count", title="Top Development Tooling Share",
            hole=0.4, color_discrete_sequence=px.colors.sequential.Blues_r
        )
        st.plotly_chart(fig_ide, use_container_width=True)
        
    with col_d2:
        st.subheader("Compensation by Educational Attainment")
        edu_comp = filtered_resp[filtered_resp["ConvertedComp"].between(5000, 250000)].dropna(subset=["EdLevel"])
        edu_comp["EdLevel_Clean"] = edu_comp["EdLevel"].str.split("(").str[0].str.strip()
        fig_edu = px.box(
            edu_comp, x="ConvertedComp", y="EdLevel_Clean", color="EdLevel_Clean",
            title="Compensation Range (USD) by Education Level",
            labels={"ConvertedComp": "Annual Salary (USD)", "EdLevel_Clean": "Degree Level"}
        )
        fig_edu.update_layout(showlegend=False)
        st.plotly_chart(fig_edu, use_container_width=True)

# -----------------------------------------------------------------------------
# Tab 5: Executive Recommendations
# -----------------------------------------------------------------------------
with tab5:
    st.subheader("🎯 Executive Talent & Technology Strategy Recommendations")
    
    st.markdown("""
    ### Key Strategic Pillars for Consulting Leadership:
    
    1. **Prioritize Full-Stack Polyglots (Python + JavaScript + SQL)**:
       - **Evidence**: JavaScript and SQL dominate employer job requisitions (>8% of all tech job postings each), while Python is the only one of the five most-used languages whose desired users exceed its current users (+15.3%).
       - **Action**: Align hiring rubrics to test relational SQL and Python scripting. Avoid niche language requirements unless project-specific.
    
    2. **Modernize Client Database Architecture (PostgreSQL & Redis)**:
       - **Evidence**: Developer desire for PostgreSQL (38.0%) and Redis (29.2%) dramatically surpasses legacy commercial RDBMS interest.
       - **Action**: Form an internal *Data Modernization Practice* helping enterprise clients migrate from legacy proprietary engines to cloud-managed PostgreSQL.
    
    3. **Skill-First Hiring Over Academic Credentialism**:
       - **Evidence**: Mann-Whitney U test confirmed that Master's degrees do NOT confer a statistically significant pay premium over Bachelor's degrees ($p = 0.068$).
       - **Action**: Remove mandatory Master's degree filters from job postings to expand the talent pool by over 200%.
    
    4. **Embrace Hybrid & Remote Work Retention**:
       - **Evidence**: Welch's t-test demonstrated that remote workers put in identical weekly hours (41.1 hrs) to in-office employees (40.9 hrs, $p = 0.272$), while dissatisfied developers are 5x more likely to seek external jobs ($p < 0.0001$).
       - **Action**: Offer flexible remote arrangements to safeguard critical engineering talent against attrition.
    """)
