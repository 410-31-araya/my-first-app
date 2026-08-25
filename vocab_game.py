import time
import streamlit as st

st.title("🧠 เกมเติมคำศัพท์ภาษาอังกฤษ")

# =========================================================
# จุดที่ 1 : กำหนดค่าเริ่มต้นใน session_state
# =========================================================
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

# เพิ่มคำตอบข้อ 3 และข้อ 4
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "start" not in st.session_state:
    st.session_state.start = time.time()

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# =========================================================
# จุดที่ 2 : ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มใหม่
# =========================================================
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""

    # เพิ่มการเคลียร์ข้อ 3 และข้อ 4
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# =========================================================
# จุดที่ 3 : ฟังก์ชันแสดงผลใน Dialog
# =========================================================
@st.dialog("🎉 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()

    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

    # เพิ่มข้อ 3 และข้อ 4
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # -----------------------------------------------------
    # ตรวจข้อ 1
    # -----------------------------------------------------
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # -----------------------------------------------------
    # ตรวจข้อ 2
    # -----------------------------------------------------
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # -----------------------------------------------------
    # ตรวจข้อ 3
    # -----------------------------------------------------
    if u_ans3 == "doctor":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # -----------------------------------------------------
    # ตรวจข้อ 4
    # -----------------------------------------------------
    if u_ans4 == "book":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # -----------------------------------------------------
    # สรุปคะแนน
    # -----------------------------------------------------
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("😢 You lose!")


# =========================================================
# จุดที่ 6 : ช่องรับคำตอบ
# =========================================================

# ข้อ 1
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

# ข้อ 2
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val
)

# ข้อ 3
ans3 = st.text_input(
    "ข้อ 3: A `d _ c t o r` helps sick people. 👨‍⚕️",
    value=st.session_state.ans3_val
)

# ข้อ 4
ans4 = st.text_input(
    "ข้อ 4: I read a `b _ _ k` every day. 📖",
    value=st.session_state.ans4_val
)


# =========================================================
# จุดที่ 7 : อัปเดตค่าล่าสุดเข้า session_state
# =========================================================
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# =========================================================
# ปุ่มส่งคำตอบ
# =========================================================
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📤 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()


# =========================================================
# จุดที่ 8 : แสดง Dialog ผลลัพธ์
# =========================================================
if st.session_state.get("is_ended", False):
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


# =========================================================
# ปุ่มเริ่มเกมใหม่ + ระบบจับเวลา 30 วินาที
# =========================================================
st.divider()

# ปุ่มเริ่มเกมใหม่
st.button("🎮 เริ่มเล่นเกมใหม่", on_click=reset_game)


# ---------------------------------------------------------
# ตรวจสอบเวลา
# ---------------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()
