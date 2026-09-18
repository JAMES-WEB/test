import streamlit as st

from mongo_database import create_person, delete_person, get_people, update_person


st.set_page_config(page_title="Community App", page_icon="👥", layout="wide")
st.title("Community App")
st.caption("Simple Streamlit + MongoDB community member management")


def show_add_person():
    st.subheader("Add Person")
    with st.form("add_person_form", clear_on_submit=True):
        name = st.text_input("Name", max_chars=100)
        phone = st.text_input("Phone", max_chars=30)
        email = st.text_input("Email", max_chars=254)
        submitted = st.form_submit_button("Add Person", type="primary")

        if submitted:
            if not name.strip():
                st.error("Name is required.")
                return
            try:
                create_person(name, phone, email)
                st.success("Person added successfully.")
                st.rerun()
            except ValueError as error:
                st.error(str(error))
            except Exception as error:
                st.error(f"Database error: {error}")


def show_people_list():
    st.subheader("People List")

    if st.button("Refresh List"):
        st.rerun()

    try:
        people = get_people()
    except Exception as error:
        st.error(f"Could not connect to MongoDB: {error}")
        return

    if not people:
        st.info("No people have been added yet.")
        return

    st.write(f"Total people: **{len(people)}**")

    for person in people:
        person_id = person["id"]
        with st.expander(f"{person['name']} — {person_id}"):
            with st.form(f"edit_{person_id}"):
                new_name = st.text_input("Name", value=person.get("name", ""), key=f"name_{person_id}")
                new_phone = st.text_input("Phone", value=person.get("phone", ""), key=f"phone_{person_id}")
                new_email = st.text_input("Email", value=person.get("email", ""), key=f"email_{person_id}")

                col1, col2 = st.columns(2)
                update_clicked = col1.form_submit_button("Update", type="primary")
                delete_clicked = col2.form_submit_button("Delete")

                if update_clicked:
                    if not new_name.strip():
                        st.error("Name is required.")
                    else:
                        try:
                            update_person(person_id, new_name, new_phone, new_email)
                            st.success("Person updated successfully.")
                            st.rerun()
                        except ValueError as error:
                            st.error(str(error))
                        except Exception as error:
                            st.error(f"Database error: {error}")

                if delete_clicked:
                    try:
                        if delete_person(person_id):
                            st.success("Person deleted successfully.")
                            st.rerun()
                        else:
                            st.error("Person was not found.")
                    except Exception as error:
                        st.error(f"Database error: {error}")


show_add_person()
st.divider()
show_people_list()
