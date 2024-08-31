import streamlit as st
from dotenv import load_dotenv
from ReachOut.Introduction.hello import create_personalized_reachout
from ReachOut.agents.profile_search_agent import profile_url_search

load_dotenv()


def reachOut_person(name: str, purpose: str) -> dict:
    """This returns the LinkedIn URL for the person and generates a reachout message."""

    persons_detail = f"LinkedIn profile URL of: {name}."
    profile_url = profile_url_search(persons_detail)
    response = create_personalized_reachout(
        url=profile_url, local=True, purpose=purpose
    )

    subject = response.subject
    message = response.message

    return {"subject": subject, "message": message}


def main():
    """
    This is the main entrypoint of the Streamlit Application.
    It takes input of the name of the person and the purpose of the interaction.
    It then uses the `reachOut_person` function to generate a reachout message based on the LinkedIn profile summary and the purpose of the interaction.
    The generated message is displayed as a subject and a message body.
    If there is an error during the message generation, it is displayed as an error message.
    """
    st.title("Personalized ReachOut Message Generator")
    st.write(
        "This application helps draft a personalized reachout message based on the LinkedIn profile summary and the purpose of the interaction."
    )

    name = st.text_input("Enter the name of the person: ")
    details = st.text_input(
        "(Optional) Enter some personal details to identify them better (e.g., Place of work, occupation, etc.): "
    )
    purpose = st.text_input("Main Purpose for reaching out: ")

    if name and purpose:
        with st.spinner(f"Generating Message for {name} ...."):
            try:
                personal_details = name + " " + details
                parsed_message = reachOut_person(name=personal_details, purpose=purpose)
                st.success("Reachout message generated successfully!")

                st.write("### Subject")
                st.write(parsed_message["subject"])

                st.write("### Message")
                st.markdown(
                    parsed_message["message"].replace("\n", "<br>"),
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both the name and the purpose.")


if __name__ == "__main__":
    main()
