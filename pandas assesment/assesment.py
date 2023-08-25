import pandas as pd

# Load the data into the DataFrame
df = pd.read_csv("student_data.csv")  # Replace with your actual file path

## 1. Select the rows where the subject is English and the score is less than 30.
english_below_30 = df[(df["English_Lit"] < 30)]

## 3. Calculate the highest scorer of Spanish
highest_scorer_spanish = df.loc[df["Spanish"].idxmax()]["Name"]

## 4. Calculate which student had the lowest attendance
df["Total_Attendance"] = df[["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]].apply(lambda row: row.value_counts().get("Present", 0), axis=1)
lowest_attendance_student = df.loc[df["Total_Attendance"].idxmin()]["Name"]

## 8. Which day had the most absences
absence_counts = df[["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]].apply(lambda col: col.value_counts().get("Absent", 0))
most_absent_day = absence_counts.idxmax()

## 9. Which person scored the most marks in Maths and Science.
df["Maths_Science_Sum"] = df["Maths"] + df["Science"]
highest_maths_science_scorer = df.loc[df["Maths_Science_Sum"].idxmax()]["Name"]

## 11. How many students were present in all 5 days
count_present_all_5_days = df[(df["Day 1"] == "Present") & (df["Day 2"] == "Present") & (df["Day 3"] == "Present")
                             & (df["Day 4"] == "Present") & (df["Day 5"] == "Present")].shape[0]

## 12. How many students were absent for 2 days
absent_for_2_days = df[(df["Day 1"] == "Absent") & (df["Day 2"] == "Absent") & (df["Day 3"] != "Absent") & (df["Day 4"] != "Absent")]
count_absent_for_2_days = absent_for_2_days.shape[0]

## 13. How many students were present for 4 days
present_for_4_days = df[(df["Day 1"] == "Present") & (df["Day 2"] == "Present") & (df["Day 3"] == "Present") & (df["Day 4"] == "Present")]
count_present_for_4_days = present_for_4_days.shape[0]

## 14. How many students score more than 25 in all subjects
above_25_all_subjects = df[(df["English_Lit"] > 25) & (df["Science"] > 25) & (df["Maths"] > 25)
                           & (df["Geography"] > 25) & (df["Spanish"] > 25) & (df["French"] > 25)]
count_above_25_all_subjects = above_25_all_subjects.shape[0]

## 15. How many students score below 30 in all subjects
below_30_all_subjects = df[(df["English_Lit"] < 30) & (df["Science"] < 30) & (df["Maths"] < 30)
                           & (df["Geography"] < 30) & (df["Spanish"] < 30) & (df["French"] < 30)]
count_below_30_all_subjects = below_30_all_subjects.shape[0]

#3 Print the answers
print("1. Students with English scores below 30:\n", english_below_30)
print("2. Total sum of English scores:", total_english_scores)
print("3. Highest scorer of Spanish:", highest_scorer_spanish)
print("4. Student with lowest attendance:", lowest_attendance_student)
print("5. Mean score for French:", mean_french_score)
print("6. Mode score for Science:", mode_science_score)
print("7. Day with the most presents:", most_present_day)
print("8. Day with the most absences:", most_absent_day)
print("9. Highest scorer in Maths and Science:", highest_maths_science_scorer)
print("10. Student with lowest total score:", lowest_total_score_student)
print("11. Students present in all 5 days:", count_present_all_5_days)
print("12. Students absent for 2 days:", count_absent_for_2_days)
print("13. Students present for 4 days:", count_present_for_4_days)
print("14. Students scoring above 25 in all subjects:", count_above_25_all_subjects)
print("15. Students scoring below 30 in all subjects:", count_below_30_all_subjects)