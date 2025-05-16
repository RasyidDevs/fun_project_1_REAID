import streamlit as st
from streamlit_card import card
from streamlit_modal import Modal

st.header("🧠Kamu ingin tahu apa hari ini?")
tab1, tab2, tab3 = st.tabs(["Seputar Cinta", "Seputar Teknologi" , "Seputar Investasi"])


#Soal Cinta
with tab1:
    
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
    if st.button("Lihat Hasil Cinta"):
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
        @st.dialog("Hasil kamu:")
        def show_dialog():
            st.success("Love language kamu adalah: " + love_language_tertinggi)
            st.image(f"assets/love/{nama_gambar}.gif")
            st.write(description)
            if st.button("Close"):
                st.rerun()
        show_dialog()
#pertanyaan teknologi
with tab2:
    st.header("Pilih bidang teknologi yang kamu minati:")
    # Inisialisasi skor
    webdev = 0
    ai = 0
    data = 0

    # Pertanyaan 1
    q1 = st.radio("1. Mana yang paling kamu sukai?", [
        "Membuat website interaktif",     
        "Menganalisis data dan visualisasi", 
        "Membangun model AI yang cerdas", 
    ])
    if q1 == "Membuat website interaktif":
        webdev += 1
    elif q1 == "Membangun model AI yang cerdas":
        ai += 1
    elif q1 == "Menganalisis data dan visualisasi":
        data += 1

    # Pertanyaan 2
    q2 = st.radio("2. Tools mana yang paling ingin kamu kuasai?", [
        "React/Vue/Next.js", 
        "Tableau/Power BI",  
        "TensorFlow/PyTorch", 
        
    ])
    if q2 == "TensorFlow/PyTorch":
        ai += 1
    elif q2 == "Tableau/Power BI":
        data += 1
    elif q2 == "React/Vue/Next.js":
        webdev += 1

    # Pertanyaan 3
    q3 = st.radio("3. Tantangan yang paling seru untukmu?", [
        "Deploy aplikasi web ke internet", 
        "Membuat dashboard dari data besar", 
        "Melatih AI agar akurat dan efisien"
    ])
    if q3 == "Membuat dashboard dari data besar":
        data += 1
    elif q3 == "Deploy aplikasi web ke internet":
        webdev += 1
    elif q3 == "Melatih AI agar akurat dan efisien":
        ai += 1
    
    if st.button("Lihat Hasil Teknologi"):
        asset = ""
        description = ""
        judul = ""
        max_score = max(webdev, ai, data)
        if max_score == webdev:
            judul = "Kamu cocok di bidang Web Developer!"
            description = "Kamu suka membuat website yang menarik dan interaktif. Kamu memiliki kreativitas dalam desain dan pengembangan web."
            asset = "web-development"
        elif max_score == ai:
            judul = "Kamu cocok di bidang AI/ML!"
            description = "Kamu tertarik dengan kecerdasan buatan dan pembelajaran mesin. Kamu suka tantangan dalam membangun model AI yang cerdas."
            asset = "AI"
        elif max_score == data:
            judul = "Kamu cocok di bidang Data Analyst!"
            description = "Kamu suka menganalisis data dan membuat visualisasi yang menarik. Kamu memiliki kemampuan dalam mengolah data besar."
            asset = "data-analyst"
        @st.dialog("Hasil kamu:")
        def show_dialog_1():
            st.success(judul)
            st.image(f"assets/tech/{asset}.gif")
            st.write(description)
            if st.button("Close"):
                st.rerun()
        show_dialog_1()
        
with tab3:
    st.header("Seputar Investasi")
    # Inisialisasi skor
    high = 0
    medium = 0
    low = 0

    # Pertanyaan 1
    q1 = st.radio("1. Pilihan investasi yang paling menarik untukmu?", [
        "Saham atau crypto",
        "Reksa dana campuran",
        "Deposito atau emas"
    ])
    if q1 == "Saham atau crypto":
        high += 1
    elif q1 == "Reksa dana campuran":
        medium += 1
    elif q1 == "Deposito atau emas":
        low += 1

    # Pertanyaan 2
    q2 = st.radio("2. Jika harga investasi turun, apa yang kamu lakukan?", [
        "Beli lagi, yakin akan naik",
        "Tunggu dan pantau",
        "Langsung jual atau pindah ke aman"
    ])
    if q2 == "Beli lagi, yakin akan naik":
        high += 1
    elif q2 == "Tunggu dan pantau":
        medium += 1
    elif q2 == "Langsung jual atau pindah ke aman":
        low += 1

    # Pertanyaan 3
    q3 = st.radio("3. Tujuan utama kamu berinvestasi?", [
        "Cuan besar dalam waktu singkat",
        "Pertumbuhan stabil jangka menengah",
        "Keamanan dan stabilitas dana"
    ])
    if q3 == "Cuan besar dalam waktu singkat":
        high += 1
    elif q3 == "Pertumbuhan stabil jangka menengah":
        medium += 1
    elif q3 == "Keamanan dan stabilitas dana":
        low += 1

    if st.button("Lihat Hasil Investasi"):
        max_score = max(high, medium, low)
        asset = ""
        description = ""
        judul = ""
        if max_score == high:
            judul = "Kamu cenderung High Risk Taker!"
            description = "Kamu suka tantangan dan berani mengambil risiko besar untuk mendapatkan keuntungan tinggi. Investasi saham atau crypto cocok untukmu."
            asset = "high-risk"
        elif max_score == medium:
            judul = "Kamu cenderung Medium Risk Taker!"
            description = "Kamu lebih suka investasi yang seimbang antara risiko dan imbal hasil. Reksa dana campuran bisa jadi pilihan yang baik."
            asset = "medium-risk"
        elif max_score == low:
            judul = "Kamu cenderung Low Risk Taker!"
            description = "Kamu lebih suka investasi yang aman dan stabil. Deposito atau emas adalah pilihan yang tepat untukmu."
            asset = "low-risk"
        @st.dialog("Hasil kamu:")
        def show_dialog_1():
            st.success(judul)
            st.image(f"assets/investment/{asset}.gif")
            st.write(description)
            if st.button("Close"):
                st.rerun()
        show_dialog_1()