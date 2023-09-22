import streamlit as st
import pandas as pd
import time 
import os
from datetime import datetime
import numpy as np
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title='face-attendance')

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

folder_path = "Attendance"  # Thay thế đường dẫn này bằng đường dẫn thư mục của bạn
days = []
months=[]
for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file_name)):
        # Trích xuất ngày từ tên file
        day = file_name.split("_")[1].split(".")[0]  # Giả sử ngày được lưu trong tên file trước dấu chấm
        month=file_name.split("-")[1].split("-")[0]
        days.append(day)
        months.append(month)

col1, col2 = st.columns([3, 2])
print(months)
# Định vị ảnh trong cột đầu tiên
with col1:
    st.header('Điểm danh học sinh')
    st.subheader(date )

    df=pd.read_csv("Attendance/Attendance_" + date + ".csv", names=["MSSV", "NAME", "TIME","TOTAL"],skiprows=1)
    total_students = df.shape[0]

    # Hiển thị tổng số sinh viên
    #st.write(f"Tổng số sinh viên: {total_students}")
    st.markdown(f"Tổng số sinh viên: **{total_students}**")


    #  st.dataframe(df.style.highlight_max())
    st.dataframe(df.style.apply(lambda x: ['background: yellow' if x.name == total_students else '' for i in x], axis=0))


# Định vị tiêu đề trong cột thứ hai
with col2:
    st.image("Resources/logobachkhoatoi.png", width=300)

    selected_date = st.selectbox("Chọn ngày", days)

    if selected_date in days:
        st.write(f"Dữ liệu sinh viên ngày {selected_date}")
        df=pd.read_csv("Attendance/Attendance_" + selected_date + ".csv", names=["MSSV", "NAME", "TIME","TOTAL"],skiprows=1)
        total_student = df.shape[0]
        st.markdown(f"Tổng số sinh viên: **{total_student}**")
        show_data = st.button("Hiển thị danh sách")
        if show_data:
            st.dataframe(df.style.apply(lambda x: ['background: yellow' if x.name == total_students else '' for i in x], axis=0))
    else:
    
        st.write("Ngày không hợp lệ")




count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")



if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
else:
    st.write(f"Count: {count}")



#df=pd.read_csv("Attendance/Attendance_" + date + ".csv", names=["MSSV", "NAME", "TIME","TOTAL"],skiprows=1)
#total_students = df.shape[0]

# Hiển thị tổng số sinh viên
#st.write(f"Tổng số sinh viên: {total_students}")
#st.markdown(f"Tổng số sinh viên: **{total_students}**")


#st.dataframe(df.style.highlight_max())
#st.dataframe(df.style.apply(lambda x: ['background: yellow' if x.name == total_students else '' for i in x], axis=0))
