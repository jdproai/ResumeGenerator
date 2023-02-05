import openai
import streamlit as st

# Replace the placeholder value with your own OpenAI API key
openai.api_key = "your_openai_api_key_here"

def generate_cover_letter(model, prompt, max_tokens):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def main():
    st.title("Cover Letter Generator")

    # User inputs
    name = st.text_input("Enter your name:")
    phone = st.text_input("Enter your phone number:")
    email = st.text_input("Enter your email address:")
    work_experience = st.text_area("Enter your work experience:")
    job_description = st.text_area("Enter job description:")

    # Cover letter generation
    model = "text-davinci-002"
    max_tokens = 300
    prompt = f"Please generate a cover letter for me. My name is {name}, and my phone number is {phone}. My email address is {email}. I have the following work experience: {work_experience}. The job description is: {job_description}"
    cover_letter = generate_cover_letter(model, prompt, max_tokens)
    st.write("Generated Cover Letter:", cover_letter)
    
    # Saving the cover letter
    if st.button("Download Cover Letter"):
        with open("cover_letter.txt", "w") as file:
            file.write(cover_letter)

if __name__ == "__main__":
    main()
