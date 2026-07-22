PERSONAL_INFO_PROMPT = """
You are an expert resume parser.

Your task is to extract ONLY the candidate's personal information from the resume.

Return ONLY valid JSON.

Do NOT include markdown.
Do NOT wrap the JSON inside ```json.
Do NOT explain anything.
Do NOT add any extra fields.
If a field is not available, return an empty string.

Return this exact JSON schema:

{{
    "full_name": "",
    "job_title": "",
    "email": "",
    "phone": "",
    "location": "",
    "linkedin": "",
    "github": "",
    "portfolio": ""
}}

Rules:

- full_name:
  Return the candidate's full name in normal readable format.
  If the resume contains spaced characters such as:
  A B C D E  F G H

  return
  Abcde Fgh

- job_title:
  Return the professional title or headline.

- email:
  Return only the email address.

- phone:
  Return only the phone number.

- location:
  Return only the city/state/country if available.

- linkedin:
  Return the LinkedIn profile URL.

- github:
  Return the GitHub profile URL.

- portfolio:
  Return the portfolio or personal website URL.

Ignore all other resume content such as:

- Summary
- Education
- Skills
- Experience
- Projects
- Certifications
- Achievements
- Languages
- Interests

Resume:
-----------------------
{resume}
-----------------------
"""