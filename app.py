import streamlit as st

# ฟังก์ชันสำหรับวิเคราะห์คำสั่ง
def analyze_command(command):
    if "คอมพิวเตอร์" in command:
        return "ปัญหาคอมพิวเตอร์"
    elif "ที่อยู่จัดส่ง" in command:
        return "การแก้ไขที่อยู่จัดส่ง"
    else:
        return "คำสั่งไม่รู้จัก"

# ระบบการแจ้งเตือน (อาจใช้ฐานข้อมูลหรือโครงสร้างข้อมูลชั่วคราว)
notifications = []

# ส่วน UI ของแอพ
st.title("AI Communication Assistant")

# รับข้อมูลจากผู้ใช้
user_input = st.text_area("กรุณาพิมพ์คำสั่งหรือปัญหาที่ต้องการให้ช่วยวิเคราะห์", "")

if st.button("วิเคราะห์คำสั่ง"):
    if user_input:
        command_type = analyze_command(user_input)
        st.success(f"ประเภทคำสั่ง: {command_type}")

        # เพิ่มการแจ้งเตือนภายในแอพ
        notification_message = f"ปัญหา '{user_input}' ได้ถูกส่งไปยังทีมที่เกี่ยวข้อง: {command_type}"
        notifications.append(notification_message)
        st.success(notification_message)
    else:
        st.warning("กรุณากรอกข้อความก่อนวิเคราะห์")

# แสดงการแจ้งเตือนที่เกิดขึ้น
if notifications:
    st.subheader("การแจ้งเตือน:")
    for notification in notifications:
        st.write(notification)
