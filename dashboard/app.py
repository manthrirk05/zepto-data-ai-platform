import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Zepto Data & AI Dashboard",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Zepto Data & AI Dashboard")
st.write("Book data analytics dashboard")

# Load data
df = pd.read_csv("data_pipeline/books_clean.csv")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Books", len(df))

with col2:
    st.metric("Categories", df["category"].nunique())

with col3:
    st.metric("Average Price", f"₹{df['price_inr'].mean():.2f}")

with col4:
    st.metric("Average Rating", f"{df['rating'].mean():.2f}")

st.divider()

# Category analysis
st.subheader("📊 Books by Category")

category_count = df["category"].value_counts()

st.bar_chart(category_count)

st.subheader("💰 Average Price by Category")

avg_price = (
    df.groupby("category")["price_inr"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(avg_price)

st.subheader("📚 Book Data")

st.dataframe(
    df[["title", "price_inr", "rating", "in_stock", "category"]],
    use_container_width=True
)