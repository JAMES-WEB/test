import requests
import streamlit as st

API_URL = st.sidebar.text_input("API URL", "http://localhost:8000")

st.title("Community App")
st.subheader("People Management")

with st.form("add_person"):
    st.write("Add Person")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add Person")

    if submitted:
        response = requests.post(
            f"{API_URL}/people",
            json={"name": name, "phone": phone or None, "email": email or None},
        )
        if response.ok:
            st.success("Person added successfully")
        else:
            st.error(response.text)

st.divider()
st.subheader("People List")

if st.button("Refresh List"):
    st.rerun()

try:
    response = requests.get(f"{API_URL}/people", timeout=5)
    if response.ok:
        people = response.json()
        for person in people:
            with st.expander(f"{person['name']} — {person['id']}"):
                st.write(f"Phone: {person.get('phone') or '-'}")
                st.write(f"Email: {person.get('email') or '-'}")

                with st.form(f"edit_{person['id']}"):
                    new_name = st.text_input("Name", person["name"])
                    new_phone = st.text_input("Phone", person.get("phone") or "")
                    new_email = st.text_input("Email", person.get("email") or "")
                    col1, col2 = st.columns(2)
                    update_clicked = col1.form_submit_button("Update")
                    delete_clicked = col2.form_submit_button("Delete")

                    if update_clicked:
                        update_response = requests.put(
                            f"{API_URL}/people/{person['id']}",
                            json={
                                "name": new_name,
                                "phone": new_phone or None,
                                "email": new_email or None,
                            },
                        )
                        if update_response.ok:
                            st.success("Person updated. Refresh the list.")
                        else:
                            st.error(update_response.text)

                    if delete_clicked:
                        delete_response = requests.delete(
                            f"{API_URL}/people/{person['id']}"
                        )
                        if delete_response.ok:
                            st.success("Person deleted. Refresh the list.")
                        else:
                            st.error(delete_response.text)
    else:
        st.error(response.text)
except requests.RequestException:
    st.warning("Could not connect to the FastAPI server.")
