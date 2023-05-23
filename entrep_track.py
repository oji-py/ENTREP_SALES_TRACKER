import streamlit as st
import pandas as pd

st.header("WAFI-SAN ORDER TRACKER")
st.markdown("---")
# Functions
def get_order_variant(order):
    if order == "WAFI":
        variant = entry_form.radio("WAFI VARIANT:", ("PLAIN", "W/ MAPLE"))
    else:
        variant = entry_form.radio("WAFI-SAN", ("HOT & SPICY", "KETCHUP & MAYO", "MAPLE SYRUP", "NO SAUCE"))
    return order, variant

# Form
st.sidebar.header("ORDER INPUT")
entry_form = st.sidebar.form("entrep_form")
customer_name = entry_form.text_input("Enter the customer's name")
order_choice = entry_form.radio("Customer Order: ", ('WAFI', 'WAFI-SAN'))
item = get_order_variant(order_choice)
num_order = entry_form.radio("NUMBER OF ORDERS: ", ("1", "2", "3", "4", "5"))
total_amount = entry_form.number_input("Amount Paid")
submit = entry_form.form_submit_button("Submit")


# List
sales_list = pd.read_csv("entrep_.csv")
st.header("Sales Tracker")
st.write(sales_list)
    
if submit:
    sales_dict = {"Name": customer_name, "Item": item, "No. of items": num_order, "Total amount": total_amount}
    sales_entry = sales_list.append(sales_dict, ignore_index=True)
    sales_entry.to_csv("entrep_.csv", index=False)
    st.write(sales_list)

    
