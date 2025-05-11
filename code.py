import requests

# 1. Send POST request to generate webhook
user_info = {
    "name": "Aman Rajput",  # Replace with your actual name
    "regNo": "0827IT221012",  # Replace with your regNo
    "email": "amanrajput220712@acropolis.in"  # Replace with your email
}

print("Sending request to generate webhook...")
response = requests.post(
    "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
    json=user_info
)

# Check response
if response.status_code != 200:
    print("Failed to generate webhook. Status Code:", response.status_code)
    print(response.text)
    exit()

# 2. Extract webhook URL and token
data = response.json()
webhook_url = data["webhook"]
access_token = data["accessToken"]

print("Webhook URL:", webhook_url)
print("Access Token:", access_token)

# 3. Choose SQL problem based on regNo
reg_no_last_digit = int(user_info["regNo"][-1])
if reg_no_last_digit % 2 == 1:
    print("You should solve SQL Question 1 (Odd RegNo)")
    print("Download: https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing")
else:
    print("You should solve SQL Question 2 (Even RegNo)")
    print("Download: https://drive.google.com/file/d/1PO1ZvmDqAZJv77XRYsVben11Wp2HVb/view?usp=sharing")

# 4. Replace this with your final SQL query after solving the problem
final_sql_query = """SELECT
        e1.EMP_ID,
        e1.FIRST_NAME,
        e1.LAST_NAME,
        d.DEPARTMENT_NAME,
        COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
    FROM
        EMPLOYEE e1
    JOIN
        DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
    LEFT JOIN
        EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT
                    AND e2.DOB > e1.DOB
    GROUP BY
        e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
    ORDER BY
        e1.EMP_ID DESC;"""  # Replace with your real SQL

# 5. Submit your solution
print("Submitting your SQL solution...")
submission_data = {
    "finalQuery": final_sql_query
}

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submit_response = requests.post(
    webhook_url,
    headers=headers,
    json=submission_data
)

if submit_response.status_code == 200:
    print("Submission successful!")
else:
    print("Submission failed. Status Code:", submit_response.status_code)
    print(submit_response.text)