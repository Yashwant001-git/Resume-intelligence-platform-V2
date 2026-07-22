# # app/pipeline/extraction/llm/prompt.py

# RESUME_EXTRACTION_PROMPT = """
# You are an expert resume parser.

# Extract ONLY the following information from the resume.

# Return ONLY valid JSON.

# Schema:

# {
#     "personal_info": {
#         "name": "",
#         "email": "",
#         "phone": "",
#         "location": "",
#         "linkedin": "",
#         "github": ""
#     },

#     "education": [
#         {
#             "degree": "",
#             "institution": "",
#             "location": "",
#             "start_date": "",
#             "end_date": "",
#             "grade": ""
#         }
#     ],

#     "certifications": [
#         {
#             "name": ""
#         }
#     ]
# }

# Rules:
# - Return ONLY valid JSON.
# - Do not include markdown.
# - Do not include explanations.
# - Do not hallucinate information.
# - Use an empty string ("") for missing fields.
# - If no education is present, return an empty list.
# - If no certifications are present, return an empty list.

# Resume:

# <<RESUME>>
# """



RESUME_EXTRACTION_PROMPT = """
You are an expert Resume Parsing AI.

Your task is to convert an unstructured resume into structured JSON.

Read the ENTIRE resume before extracting any information.

Extract ONLY the information requested below.

Do NOT guess, infer, or hallucinate any information.

If a field is missing, return an empty string ("").

If a list is empty, return [].

Return ONLY valid JSON.
Do NOT return Markdown.
Do NOT wrap the JSON inside ```json.
Do NOT include explanations or comments.

=========================================================
SECTION 1 : PERSONAL INFORMATION
=========================================================

Extract:

- Full Name
- Email Address
- Phone Number
- Current Location (City, State/Country if explicitly mentioned)
- LinkedIn URL
- GitHub URL

Rules:

• Return the complete LinkedIn URL if available.
• Return the complete GitHub URL if available.
• Do not create URLs.
• Do not infer the user's location.

Example:

{
    "name": "John Doe",
    "email": "john@gmail.com",
    "phone": "+91 9876543210",
    "location": "Bangalore, India",
    "linkedin": "https://linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe"
}

=========================================================
SECTION 2 : EDUCATION
=========================================================

Each education entry MUST represent ONE academic qualification.

Extract:

- degree
- institution
- location
- start_date
- end_date
- grade

Definitions:

degree
→ Degree name only.

Examples:
"B.Tech Computer Science"
"BSc Data Science"
"M.Tech AI"

institution
→ University or College name only.

location
→ Institution location only.

start_date
→ Start year/date of the education.

end_date
→ Graduation year/date.

grade
→ GPA / CGPA / Percentage if present.

IMPORTANT RULES

Never use:

- Internship dates
- Job dates
- Project dates
- Certification dates

inside Education.

Education dates must belong ONLY to the education entry.

Example:

[
    {
        "degree": "BSc Data Science and Machine Learning",
        "institution": "RV University",
        "location": "Bangalore",
        "start_date": "2022",
        "end_date": "2026",
        "grade": "CGPA 9.21"
    }
]

=========================================================
SECTION 3 : CERTIFICATIONS
=========================================================

Each certification MUST be returned as a separate object.

Do NOT merge multiple certifications into one string.

Correct:

[
    {
        "name": "AWS Cloud Practitioner"
    },
    {
        "name": "Python Certification"
    },
    {
        "name": "Machine Learning Specialization"
    }
]

Incorrect:

[
    {
        "name": "AWS Cloud Practitioner Python Certification Machine Learning Specialization"
    }
]

Extract the certification title exactly as written.

=========================================================
FINAL VALIDATION
=========================================================

Before producing the final JSON, verify that:

1. Every education entry contains ONLY education information.

2. Internship dates are NOT inside education.

3. Job dates are NOT inside education.

4. Each certification is a separate object.

5. Every field follows the requested schema.

6. Missing values are returned as an empty string ("").

7. Missing lists are returned as [].

=========================================================
OUTPUT SCHEMA
=========================================================

{
    "personal_info": {
        "name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": ""
    },

    "education": [
        {
            "degree": "",
            "institution": "",
            "location": "",
            "start_date": "",
            "end_date": "",
            "grade": ""
        }
    ],

    "certifications": [
        {
            "name": ""
        }
    ]
}

=========================================================
RESUME
=========================================================

<<RESUME>>
"""