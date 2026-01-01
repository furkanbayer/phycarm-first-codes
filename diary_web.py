import streamlit as st
import datetime
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="My Personal Diary", page_icon="📘", layout="centered")

# --- HEADER ---
st.title("📘 My Personal Diary")
st.write("Capture your thoughts, memories, and ideas.")

# --- SECTION 1: WRITE ENTRY ---
st.subheader("✍️ New Entry")

# Text area for user input
entry = st.text_area("Dear Diary:", height=150, placeholder="Today I learned about Python web apps...")

# Save Button
if st.button("Save Memory"):
    if entry:
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M")

        # Save to file
        with open("my_diary.txt", "a", encoding="utf-8") as file:
            file.write(f"\n--- {timestamp} ---\n")
            file.write(f"{entry}\n")
            file.write("-" * 30)

        st.success(f"✅ Saved successfully at {timestamp}!")
    else:
        st.error("⚠️ Please write something before saving.")

# --- SECTION 2: READ HISTORY ---
st.markdown("---")
st.subheader("📖 Past Memories")

if st.checkbox("Show History"):
    if os.path.exists("my_diary.txt"):
        with open("my_diary.txt", "r", encoding="utf-8") as file:
            content = file.read()
            st.text(content)
    else:
        st.info("No entries found yet. Write your first one above!")