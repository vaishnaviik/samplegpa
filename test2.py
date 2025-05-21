import streamlit as st

subjects={"Semester 1":[("CD111",3),("CD112",3),("CD113",3),("CD114",4),("CD151",1),("CD152",1),("CD153",1.5),("CD154",2),("CD153",0.5)],
          "Semester 2":[("CD121", 3), ("CD122", 2), ("CD123", 2), ("CD124", 3), ("CD125", 2), ("CD126", 4), ("CD161", 1), ("CD162", 1), ("CD163", 1), ("CD164", 1.5), ("CD165", 0.5)]
          }
data={}
gradepoints= {"A+": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "F": 0}

st.set_page_config(page_title="CGPA Caluculator")

def get_sgpa(sem):
  global subjects,data
  courseskey=f"Semester {sem}"
  if courseskey not in subjects:
    st.error("Invalid semester")
    return
  courses=subjects.get(courseskey)
  totalpoints=totalcredits=0

  grades = {}
  for subject,credit in courses:
    grades[(subject, credit)] = st.selectbox(f"Enter {subject} grade:", list(gradepoints.keys()), key=f"{courseskey}_{subject}_{credit}")
  
  if st.button("Calculate SGPA"):
    for (subject, credit), grade in grades.items():
      points=gradepoints.get(grade,None)
      if points==None:
        st.error("Invalid grade")
        return
      totalpoints+=points*credit
      totalcredits+=credit
    sgpa=round(totalpoints/totalcredits,2)
    data[sem]=(sgpa,totalcredits)
    st.success(f"SGPA: {sgpa}")

def finalcgpa():
  if not data:
    st.warning("No previous data available")
    return
  totalpoints=0
  totalcredits=0

  for sem,(sgpa,credits) in data.items():
    totalpoints+=sgpa*credits
    totalcredits+=credits

  finalcgpa=round(totalpoints/totalcredits,2)
  st.info(f"Final CGPA: {finalcgpa}")

st.title("SGPA & CGPA Calculator")

choice=st.selectbox("Choose an option",["Calculate SGPA", "Calculate CGPA"])

if choice=="Calculate SGPA":
  sem=st.number_input("Enter semester:", min_value=1, step=1)
  get_sgpa(sem)
elif choice=="Calculate CGPA":
  finalcgpa()
