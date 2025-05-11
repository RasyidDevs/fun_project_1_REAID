import streamlit as st


st.header("Masukan nama anda!!")
nama = st.text_input("Masukkan nama anda terlebih dahulu....: ")

if nama:
    nama = nama[0].upper() + nama[1:]

    st.header(f"Selamat datang {nama}!! di aplikasi tebak LOVE💖 Language✨")
    st.write("Silakan jawab 5 pertanyaan berikut:")

    # Inisialisasi skor love language
    words = 0
    time = 0
    touch = 0
    service = 0
    gift = 0

    # Pertanyaan 1
    q1 = st.radio("1. Ketika kamu sedang merasa sedih, apa yang paling membuatmu merasa tenang?", 
        ["Mendengar kata-kata penyemangat", 
         "Seseorang menghabiskan waktu bersamaku", 
         "Dipeluk erat", 
         "Diperhatikan", 
         "Menerima hadiah kecil yang menghibur"])

    if q1 == "Mendengar kata-kata penyemangat":
        words += 1
    elif q1 == "Seseorang menghabiskan waktu bersamaku":
        time += 1
    elif q1 == "Dipeluk erat":
        touch += 1
    elif q1 == "Diperhatikan":
        service += 1
    elif q1 == "Menerima hadiah kecil yang menghibur":
        gift += 1

    # Pertanyaan 2
    q2 = st.radio("2. Apa yang paling kamu hargai dari pasanganmu?", 
        ["Ucapan pujian atau apresiasi", 
         "Waktu berkualitas bersama", 
         "pegangan tangan atau pelukan", 
         "Suka di antar jemput", 
         "Memberikan kejutan atau hadiah spontan"])

    if q2 == "Ucapan pujian atau apresiasi":
        words += 1
    elif q2 == "Waktu berkualitas bersama":
        time += 1
    elif q2 == "pegangan tangan atau pelukan":
        touch += 1
    elif q2 == "Suka di antar jemput":
        service += 1
    elif q2 == "Memberikan kejutan atau hadiah spontan":
        gift += 1

    # Pertanyaan 3
    q3 = st.radio("3. Saat ulang tahunmu, apa yang paling kamu harapkan dari orang terdekat?", 
        ["Ucapan selamat yang tulus dan menyentuh", 
         "Melakukan sesuatu bersama hangout", 
         "Pelukan hangat dan kasih sayang", 
         "Di bantu menyiapkan atau merayakan ulang tahun", 
         "Mendapat kado yang kamu suka"])

    if q3 == "Ucapan selamat yang tulus dan menyentuh":
        words += 1
    elif q3 == "Melakukan sesuatu bersama hangout":
        time += 1
    elif q3 == "Pelukan hangat dan kasih sayang":
        touch += 1
    elif q3 == "Di bantu menyiapkan atau merayakan ulang tahun":
        service += 1
    elif q3 == "Mendapat kado yang kamu suka":
        gift += 1

    # Pertanyaan 4
    q4 = st.radio("4. Bagaimana kamu menunjukkan kasih sayang kepada orang lain?", 
        ["Dengan memberi pujian atau motivasi", 
         "Dengan meluangkan waktu bersama mereka", 
         "Dengan mengenggam atau memeluk mereka", 
         "Dengan membantu mereka dalam tugas sehari-hari", 
         "Dengan memberi hadiah"])

    if q4 == "Dengan memberi pujian atau motivasi":
        words += 1
    elif q4 == "Dengan meluangkan waktu bersama mereka":
        time += 1
    elif q4 == "Dengan mengenggam atau memeluk mereka":
        touch += 1
    elif q4 == "Dengan membantu mereka dalam tugas sehari-hari":
        service += 1
    elif q4 == "Dengan memberi hadiah":
        gift += 1

    # Pertanyaan 5
    q5 = st.radio("5. Saat sedang rindu, apa yang membuatmu merasa lebih dekat dengan orang tersayang?", 
        ["Mendengar suara mereka dan kata-kata manis", 
         "Video call panjang hanya untuk ngobrol", 
         "Mengingat momen-momen indah bersama", 
         "Tiba-tiba dibantu dalam hal kecil via chat", 
         "Menerima kiriman barang dari mereka"])

    if q5 == "Mendengar suara mereka dan kata-kata manis":
        words += 1
    elif q5 == "Video call panjang hanya untuk ngobrol":
        time += 1
    elif q5 == "Mengingat momen-momen indah bersama":
        touch += 1
    elif q5 == "Tiba-tiba dibantu dalam hal kecil via chat":
        service += 1
    elif q5 == "Menerima kiriman barang dari mereka":
        gift += 1

    # Tampilkan hasil jika tombol ditekan
    if st.button("Lihat Hasil"):
        st.subheader("Hasil Love Language Kamu Adalah:")
        
        nama_gambar = ""
        description = ""
        max_score = max(words, time, touch, service, gift)  
        if max_score == words:
            love_language_tertinggi = "Words of Affirmation"
            nama_gambar = "word-of-affirmation"
            description = "Kamu adalah orang yang menghargai kata-kata penyemangat dan pujian dari orang terkasih. Kata-kata yang tulus dapat membuatmu merasa dicintai dan dihargai."
        elif max_score == time:
            love_language_tertinggi = "Quality Time"
            nama_gambar = "quality-time"
            description = "Kamu adalah orang yang menghargai waktu berkualitas bersama pasangan. Momen-momen berharga saat bersama adalah hal yang paling berarti bagimu."
        elif max_score == touch:
            love_language_tertinggi = "Physical Touch"
            nama_gambar = "physical-touch"
            description = "Kamu adalah orang yang menghargai sentuhan fisik seperti pelukan, pegangan tangan, dan keintiman. Sentuhan dapat membuatmu merasa dekat dengan pasangan."
        elif max_score == service: 
            love_language_tertinggi = "Acts of Service"
            nama_gambar = "act-of-service"
            description = "Kamu adalah orang yang menghargai tindakan nyata dari pasangan, seperti membantu dalam tugas sehari-hari. Tindakan ini menunjukkan perhatian dan cinta."
        elif max_score == gift:
            love_language_tertinggi = "Receiving Gifts"  
            nama_gambar = "gift"    
            description = "Kamu adalah orang yang menghargai hadiah dan kejutan dari pasangan. Hadiah kecil yang penuh makna dapat membuatmu merasa dicintai."
        st.success(f"✨ {love_language_tertinggi} ✨")
        st.image(f"assets/{nama_gambar}.gif", caption=f"Love Language: {love_language_tertinggi}")
        st.write(description)
       
