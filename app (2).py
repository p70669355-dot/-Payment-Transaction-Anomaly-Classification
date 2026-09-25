
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Payment Transaction Risk Intelligence",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.metric-card {
    background: linear-gradient(135deg, #151a23, #1b2230);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #303744;
    text-align: center;
}

.metric-title {
    color: #9ca3af;
    font-size: 14px;
}

.metric-value {
    color: white;
    font-size: 30px;
    font-weight: 700;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 15px;
}

.small-text {
    color: #9ca3af;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_data():

    file_path = "payment_transactions_cleaned.csv"

    if os.path.exists(file_path):
        return pd.read_csv(file_path)

    return None


# ============================================================
# LOAD DATA
# ============================================================

import os

df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    "# 💳 Payment Risk\n## Intelligence Platform"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Command Center",
        "📊 Executive Dashboard",
        "💳 Transaction Risk Studio",
        "🔍 Transaction Explorer",
        "🚨 Anomaly Investigation",
        "🧠 Explainable AI",
        "📈 Model Intelligence",
        "🔔 Alert Center",
        "📑 Reports",
        "🕘 Prediction History",
        "⚙️ About System"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **System Status**

    🟢 Application Online

    🟢 Dataset Connected

    🟡 ML Model Integration
    """
)


# ============================================================
# DATA CHECK
# ============================================================

if df is None:

    st.error(
        "Dataset not found. Please keep "
        "`payment_transactions_cleaned.csv` in the same folder as `app.py`."
    )

    st.stop()


# ============================================================
# BASIC DATA PREPARATION
# ============================================================

total_transactions = len(df)

anomalous_transactions = int(
    df["isFraud"].sum()
) if "isFraud" in df.columns else 0

routine_transactions = (
    total_transactions - anomalous_transactions
)

anomaly_rate = (
    anomalous_transactions / total_transactions * 100
    if total_transactions > 0
    else 0
)

average_amount = (
    df["amount"].mean()
    if "amount" in df.columns
    else 0
)


# ============================================================
# COMMAND CENTER
# ============================================================

if page == "🏠 Command Center":

    st.title("💳 Payment Transaction Risk Intelligence")

    st.markdown(
        "### AI-powered payment transaction monitoring and anomaly analysis"
    )

    st.markdown(
        "Analyze transaction behaviour, identify anomalous patterns, "
        "explore transaction characteristics and evaluate machine-learning models."
    )

    st.markdown("---")

    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Transactions",
            f"{total_transactions:,}"
        )

    with col2:
        st.metric(
            "Routine Transactions",
            f"{routine_transactions:,}"
        )

    with col3:
        st.metric(
            "Anomalous Transactions",
            f"{anomalous_transactions:,}"
        )

    with col4:
        st.metric(
            "Anomaly Rate",
            f"{anomaly_rate:.2f}%"
        )

    st.markdown("---")

    # SECOND ROW

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Transaction Classification")

        chart_data = pd.DataFrame({
            "Category": [
                "Routine",
                "Anomalous"
            ],
            "Count": [
                routine_transactions,
                anomalous_transactions
            ]
        })

        fig = px.pie(
            chart_data,
            names="Category",
            values="Count",
            hole=0.55,
            title="Routine vs Anomalous Transactions"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("Transaction Types")

        if "type" in df.columns:

            type_counts = (
                df["type"]
                .value_counts()
                .reset_index()
            )

            type_counts.columns = [
                "Transaction Type",
                "Count"
            ]

            fig = px.bar(
                type_counts,
                x="Transaction Type",
                y="Count",
                title="Transaction Volume by Type"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # AMOUNT ANALYSIS

    st.subheader("💰 Transaction Amount Analysis")

    if "amount" in df.columns:

        fig = px.histogram(
            df,
            x="amount",
            nbins=50,
            title="Distribution of Transaction Amounts"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# EXECUTIVE DASHBOARD
# ============================================================

elif page == "📊 Executive Dashboard":

    st.title("📊 Executive Dashboard")

    st.write(
        "High-level analytical view of payment transaction behaviour."
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Transactions",
            f"{total_transactions:,}"
        )

    with col2:
        st.metric(
            "Average Amount",
            f"{average_amount:,.2f}"
        )

    with col3:
        st.metric(
            "Anomalous",
            f"{anomalous_transactions:,}"
        )

    with col4:
        st.metric(
            "Anomaly %",
            f"{anomaly_rate:.2f}%"
        )

    st.markdown("---")

    if "type" in df.columns and "isFraud" in df.columns:

        type_analysis = (
            df.groupby("type")["isFraud"]
            .agg(["count", "sum", "mean"])
            .reset_index()
        )

        type_analysis.columns = [
            "Transaction Type",
            "Transactions",
            "Anomalies",
            "Anomaly Rate"
        ]

        type_analysis["Anomaly Rate"] *= 100

        st.subheader("Anomaly Rate by Transaction Type")

        fig = px.bar(
            type_analysis,
            x="Transaction Type",
            y="Anomaly Rate",
            text="Anomaly Rate",
            title="Anomaly Rate by Transaction Type"
        )

        fig.update_traces(
            texttemplate="%{text:.2f}%",
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.dataframe(
            type_analysis,
            use_container_width=True
        )


# ============================================================
# TRANSACTION RISK STUDIO
# ============================================================

elif page == "💳 Transaction Risk Studio":

    st.title("💳 Transaction Risk Studio")

    st.write(
        "Analyze an individual payment transaction."
    )

    st.markdown("---")

    st.subheader("Transaction Information")

    col1, col2 = st.columns(2)

    with col1:

        transaction_type = st.selectbox(
            "Transaction Type",
            ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
        )

        amount = st.number_input(
            "Transaction Amount",
            min_value=0.0,
            value=1000.0
        )

        old_balance_org = st.number_input(
            "Sender Previous Balance",
            min_value=0.0,
            value=5000.0
        )

        new_balance_org = st.number_input(
            "Sender New Balance",
            min_value=0.0,
            value=4000.0
        )

    with col2:

        step = st.number_input(
            "Transaction Step",
            min_value=0,
            value=1
        )

        old_balance_dest = st.number_input(
            "Receiver Previous Balance",
            min_value=0.0,
            value=2000.0
        )

        new_balance_dest = st.number_input(
            "Receiver New Balance",
            min_value=0.0,
            value=3000.0
        )

    st.markdown("---")

    if st.button(
        "🔍 Analyze Transaction",
        use_container_width=True
    ):

        st.info(
            "ML prediction will be connected here after the final trained model is selected and saved."
        )

        st.subheader("Transaction Summary")

        result = pd.DataFrame({
            "Feature": [
                "Transaction Type",
                "Amount",
                "Sender Previous Balance",
                "Sender New Balance",
                "Receiver Previous Balance",
                "Receiver New Balance"
            ],
            "Value": [
                transaction_type,
                amount,
                old_balance_org,
                new_balance_org,
                old_balance_dest,
                new_balance_dest
            ]
        })

        st.dataframe(
            result,
            use_container_width=True
        )


# ============================================================
# TRANSACTION EXPLORER
# ============================================================

elif page == "🔍 Transaction Explorer":

    st.title("🔍 Transaction Explorer")

    st.write(
        "Search, filter and investigate transactions from the dataset."
    )

    st.markdown("---")

    display_df = df.copy()

    col1, col2 = st.columns(2)

    with col1:

        if "type" in df.columns:

            selected_type = st.multiselect(
                "Transaction Type",
                sorted(df["type"].dropna().unique())
            )

            if selected_type:

                display_df = display_df[
                    display_df["type"].isin(selected_type)
                ]

    with col2:

        if "isFraud" in df.columns:

            classification = st.selectbox(
                "Classification",
                [
                    "All",
                    "Routine",
                    "Anomalous"
                ]
            )

            if classification == "Routine":

                display_df = display_df[
                    display_df["isFraud"] == 0
                ]

            elif classification == "Anomalous":

                display_df = display_df[
                    display_df["isFraud"] == 1
                ]

    st.markdown("---")

    st.write(
        f"Showing **{len(display_df):,}** transactions"
    )

    st.dataframe(
        display_df.head(1000),
        use_container_width=True
    )


# ============================================================
# ANOMALY INVESTIGATION
# ============================================================

elif page == "🚨 Anomaly Investigation":

    st.title("🚨 Anomaly Investigation")

    st.write(
        "Detailed investigation of anomalous transaction records."
    )

    if "isFraud" in df.columns:

        anomaly_df = df[
            df["isFraud"] == 1
        ].copy()

        st.metric(
            "Anomalous Records",
            f"{len(anomaly_df):,}"
        )

        st.markdown("---")

        if len(anomaly_df) > 0:

            st.subheader(
                "Anomalous Transaction Records"
            )

            st.dataframe(
                anomaly_df.head(500),
                use_container_width=True
            )

            if "amount" in anomaly_df.columns:

                fig = px.histogram(
                    anomaly_df,
                    x="amount",
                    nbins=40,
                    title="Amount Distribution of Anomalous Transactions"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


# ============================================================
# EXPLAINABLE AI
# ============================================================

elif page == "🧠 Explainable AI":

    st.title("🧠 Explainable AI")

    st.write(
        "Understand which transaction characteristics are important "
        "for anomaly classification."
    )

    st.markdown("---")

    st.info(
        "Feature-level model explanations such as SHAP will be connected "
        "after the final model is selected."
    )

    if "isFraud" in df.columns:

        st.subheader(
            "Transaction Feature Relationships"
        )

        numeric_df = df.select_dtypes(
            include=np.number
        )

        if not numeric_df.empty:

            correlation = numeric_df.corr()

            fig = px.imshow(
                correlation,
                text_auto=True,
                title="Feature Correlation Matrix"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# ============================================================
# MODEL INTELLIGENCE
# ============================================================

elif page == "📈 Model Intelligence":

    st.title("📈 Model Intelligence")

    st.write(
        "Performance comparison of machine-learning models."
    )

    st.markdown("---")

    st.info(
        "Your actual Logistic Regression, KNN and Decision Tree "
        "evaluation results will be displayed here."
    )

    st.subheader("Models Used")

    model_info = pd.DataFrame({
        "Model": [
            "Logistic Regression",
            "K-Nearest Neighbors",
            "Decision Tree"
        ],
        "Purpose": [
            "Baseline classification model",
            "Distance-based classification",
            "Tree-based classification"
        ]
    })

    st.dataframe(
        model_info,
        use_container_width=True
    )

    st.subheader("Evaluation Metrics")

    metrics = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ]

    for metric in metrics:

        st.write(f"• {metric}")


# ============================================================
# ALERT CENTER
# ============================================================

elif page == "🔔 Alert Center":

    st.title("🔔 Alert Center")

    st.write(
        "Monitor transactions requiring attention."
    )

    st.markdown("---")

    if "isFraud" in df.columns:

        alert_count = int(
            df["isFraud"].sum()
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Alerts",
                f"{alert_count:,}"
            )

        with col2:
            st.metric(
                "Dataset Transactions",
                f"{len(df):,}"
            )

        with col3:
            st.metric(
                "Alert Rate",
                f"{anomaly_rate:.2f}%"
            )

        st.markdown("---")

        alerts = df[
            df["isFraud"] == 1
        ].copy()

        st.subheader("Recent Anomalous Transactions")

        st.dataframe(
            alerts.head(100),
            use_container_width=True
        )


# ============================================================
# REPORTS
# ============================================================

elif page == "📑 Reports":

    st.title("📑 Reports & Downloads")

    st.write(
        "Download analytical results generated from the transaction dataset."
    )

    st.markdown("---")

    csv_data = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Transaction Dataset",
        data=csv_data,
        file_name="payment_transaction_analysis.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.subheader("Dataset Summary")

    st.write(
        f"Total Records: **{len(df):,}**"
    )

    st.write(
        f"Total Columns: **{len(df.columns)}**"
    )


# ============================================================
# HISTORY
# ============================================================

elif page == "🕘 Prediction History":

    st.title("🕘 Prediction History")

    st.write(
        "Transactions analyzed during the current application session."
    )

    if "history" not in st.session_state:

        st.session_state.history = []

    if len(st.session_state.history) == 0:

        st.info(
            "No transactions have been analyzed yet."
        )

    else:

        history_df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            history_df,
            use_container_width=True
        )


# ============================================================
# ABOUT
# ============================================================

elif page == "⚙️ About System":

    st.title("⚙️ About Payment Risk Intelligence")

    st.markdown("""
    ### Project Overview

    **Payment Transaction Anomaly Classification**

    This project uses machine-learning techniques to classify
    payment transactions into routine and anomalous categories.

    ### Machine Learning Models

    - Logistic Regression
    - K-Nearest Neighbors
    - Decision Tree

    ### Analytical Components

    - Data Cleaning
    - Exploratory Data Analysis
    - Feature Analysis
    - Classification
    - Model Evaluation
    - Error Analysis
    - Transaction Investigation
    - Explainable AI
    - Interactive Dashboard

    ### Technology Stack

    - Python
    - Pandas
    - NumPy
    - Scikit-learn
    - Plotly
    - Streamlit

    ### Project Domain

    FinTech / Payment Security
    """)

    st.success(
        "Payment Transaction Risk Intelligence Platform"
    )
