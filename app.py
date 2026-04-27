import streamlit as st

if "login" not in st.session_state:
    st.session_state.login = False

if "data" not in st.session_state:
    st.session_state.data = []

if not st.session_state.login:
    st.title("Sistem Penilaian Mahasiswa")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Masuk"):
        if username == "Angga" and password == "2313010605":
            st.session_state.login = True
            st.success("Berhasil Masuk")
        else:
            st.error("Username atau Password Salah")

else:
    st.title("Sistem Penilaian Mahasiswa")

    nama = st.text_input("Nama Mahasiswa")
    nilai = st.number_input("Nilai", min_value=0, max_value=100)

    if nilai >= 85:
        grade = "A"
    elif nilai >= 75:
        grade = "B"
    elif nilai >= 65:
        grade = "C"
    else:
        grade = "D"

    if st.button("Simpan Data"):
        if nama == "":
            st.warning("Nama Tidak Boleh Kosong")
        else:
            st.session_state.data.append({
                "Nama": nama,
                "Nilai": str(nilai),
                "Grade": grade
            })
            st.success("Data Berhasil Disimpan")

    st.subheader("Data Mahasiswa")

    if len(st.session_state.data) > 0:
        st.table(st.session_state.data)
    else:
        st.write("Tidak Ada Data")

    if st.button("Hapus Data"):
        st.session_state.data = []
        st.warning("Data Telah Dihapus")

    if st.button("Keluar"):
        st.session_state.login = False
        st.success("Berhasil Keluar")