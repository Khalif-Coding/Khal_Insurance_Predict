import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():
    st.write('# Insurance')
    st.markdown("""<div style='text-align: center;'>
    <img src='https://media.istockphoto.com/id/1153620019/photo/hand-holding-piece-of-puzzle-with-word-insurance-risk.jpg?s=612x612&w=0&k=20&c=Nyrc740sEDh064YHWrxT3BEXW3kEXxjrsm-1RCaIDcA=' width='400'>
    </div>""", unsafe_allow_html=True)

    st.write('# Description')
    st.write('''Asuransi kesehatan penting untuk memberikan perlindungan finansial terhadap risiko kesehatan yang tidak terduga. 
                Project ini bertujuan untuk memprediksi premi asuransi kesehatan secara lebih akurat berdasarkan profil peserta. 
                Model dikembangkan menggunakan algoritma Linear Regression dan dievaluasi dengan Mean Absolute Error (MAE) sebagai metrik kinerja.''')

    # Dataframe
    df = pd.read_csv('Medicalpremium.csv')
    st.write('# Dataset')
    st.write(df)

    # Plot 1
    st.write('# Exploratory Data Analysis')
    st.write('## Jumlah Peserta Asuransi Berdasarkan Kelompok Umur')
    bins = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    labels = ['20–24', '25–29', '30–34', '35–39', '40–44', 
            '45–49', '50–54', '55–59', '60–64', '65–69']
    age_group = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    counts = age_group.value_counts().sort_index()
    fig = plt.figure(figsize=(12,5))
    sns.barplot(x=counts.index, y=counts.values, color='green')
    plt.xlabel('Kelompok Usia')
    plt.ylabel('Jumlah Peserta')
    plt.title('Jumlah Peserta Asuransi per Kelompok Usia')
    plt.tight_layout()
    st.pyplot(fig)
    st.write('''Insight: Berdasarkan distribusi sampel data, peserta asuransi berada pada rentang usia 20–69 tahun. 
                Kelompok usia 65–69 memiliki jumlah peserta paling sedikit (di bawah 60 orang), sedangkan kelompok usia lainnya rata-rata memiliki lebih dari 80 peserta. 
                Hal ini kemungkinan disebabkan premi yang lebih mahal pada usia lanjut, sehingga sebagian besar peserta sudah memiliki asuransi sejak usia lebih muda.''')

    # Plot 2
    st.write('## Jumlah Peserta Asuransi Berdasarkan Kelompok Umur')
    bmi = df['Weight'] / ((df['Height'] / 100) ** 2)

    fig2 = plt.figure(figsize=(20,6))
    sns.scatterplot(x=bmi,y=df['PremiumPrice'],color='green',alpha=0.6)
    plt.title('BMI vs Harga Premi')
    plt.xlabel('BMI')
    plt.ylabel('Harga Premi')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig2)
    st.write('''Insight: Berdasarkan Hasil Pengecekan Distribusi BMI Dengan PremiumPrice Terlihat Bahwa Distribusi Tersebar Cukup Merata
                Tetapi Jika Dilihat Lagi Ternyata BMI Kurang Berpengaruh Terhadap Harga Premi Terlihat Dari Visual Bahwa Malah Variasi PremiumPrice
                Tersebar Lebih Banyak Di BMI Yang Rendah Hal Ini Dimungkinkan Juga Karena Sedikitnya BMI Yang Tinggi Sehingga Tetap Jaga BMI Untuk Hidup Lebih Sehat.''')

    # Plot 3
    st.write('## Distribusi Peserta Asuransi Berdasarkan NumberOfMajorSurgeries?')
    fig3 = plt.figure(figsize=(20,6))
    sns.countplot(x=df['NumberOfMajorSurgeries'], color='green')
    plt.title('Distribusi Jumlah Operasi Besar')
    plt.xlabel('Jumlah Operasi Besar')
    plt.ylabel('Jumlah Peserta')
    plt.tight_layout()
    plt.show() 
    st.pyplot(fig3)
    st.write('''Insight: Berdasarkan Hasil Visualisasi Terkait NumberOfMajorSurgeries Terlihat Bahwa Orang Dengan NumberOfMajorSurgeries 0 Lebih Aware Terkait Proteksi
                Financial Mereka Dibuktikan Dari Distribusinya. Tetapi Bisa Juga Terjadi Dikarenakan Semakin Tinggi NumberOfMajorSurgeries Maka PremiumPrices Akan Lebih Mahal.''')


    # Plot 4
    st.write('## Distribusi Peserta Asuransi Berdasarkan NumberOfMajorSurgeries?')
    fig4 = plt.figure(figsize=(20,6))
    num_df = pd.DataFrame({
    'Age': df['Age'],
    'BMI': bmi,
    'NumberOfMajorSurgeries': df['NumberOfMajorSurgeries'],
    'PremiumPrice': df['PremiumPrice']})
    corr = num_df.corr(method='spearman')
    sns.heatmap(corr, annot=True, cmap='Greens', fmt='.2f')
    plt.title('Correlation Numerical Feature Dengan Target (PremiumPrice)')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig4)
    st.write('''Insight: Terlihat Bahwa Umur Paling Mempengaruhi Harga Asuransi Sehingga Semakin Muda Anda Memiliki Asuransi Maka Semakin Murah PremiumPricenya.''')

    # Plot 5
    st.write('## Berdasarkan Hasil Correlation Numerical Dengan Target, Apakah Benar Bahwa Hubungan Age dengan PremiumPrice Itu Adalah "Strong Correlation"?')
    fig5 = plt.figure(figsize=(20, 6))
    sns.scatterplot(x='Age', y='PremiumPrice', data=df, color='green', alpha=0.6)
    plt.title('Hubungan Age dengan PremiumPrice')
    plt.xlabel('Age')
    plt.ylabel('PremiumPrice')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig5)
    st.write('Insight: Setelah Melihat Visualisasi Ternyata Benar Bahwa Age Memiliki Korelasi Yang Berdasarkan Sebarannya Bahwa Umur Lebih Tua Maka PremiumPrice Semakin Mahal Untuk Itu Memiliki Asuransi Semakin Cepat Maka Semakin Murah')
    
    # Plot 6
    st.write('## Bagaimana Penyebaran BMI dalam Kelompok Diabetes?')
    fig6 = plt.figure(figsize=(20,6))
    sns.boxplot(x='Diabetes', y=bmi, data=df,hue= df['Diabetes'], palette='Greens')
    plt.title('Distribusi BMI pada Peserta Diabetes')
    plt.xlabel('Status Diabetes')
    plt.ylabel('BMI')
    plt.show()
    st.pyplot(fig6)
    st.write('Insight: Setelah Melihat Visualisasi Ternyata BMI Antara Orang Diabetes Dan Tidak Diabetes Tidak Terlalu Memiliki Pengaruh Terlihat Dari Sebarannya Berdasarkan Boxplot.')

    # Plot 7
    st.write('## Bagaimana Korelasi Antara NumberOfMajorSurgeries & Diabetes Vs Target?')
    fig7 = plt.figure(figsize=(20,6))
    sns.barplot(
    x='NumberOfMajorSurgeries', 
    y='PremiumPrice', 
    hue='Diabetes', 
    data=df, 
    estimator='mean', 
    palette='Greens')
    plt.title("Average PremiumPrice by Number of Major Surgeries & Diabetes")
    plt.xlabel("Number of Major Surgeries")
    plt.ylabel("Mean PremiumPrice")
    plt.legend(title='Diabetes')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig7)
    st.write('Insight: Setelah Melihat Visualisasi Terlihat Bahwa NumberOfMajorSurgeries Terlihat Lebih Memiliki Pengaruh Dibandingkan Dengan Diabetes.')

    st.write('# Conclusion')
    st.write('''
                Berdasarkan Hasil EDA, Bahwa Ada Beberapa Faktor Yang Mempengaruhi Harga Asuransi Mulai Dari Yang Sangat Berpengaruh Dan Yang Tidak Terlalu Berpengaruh.
                Tetapi, Berdasarkan Kesimpulan Singkat Bahwa Yang Paling Mempengaruhi PremiumPrice Adalah Age. Sehingga, Membuka Rekening Asuransi Semakin Cepat Maka Semakin Baik,
                Dimana Aset Dapat Terlindungi Dan PremiumPrice Juga Relatif Lebih Murah.
                ''')


if __name__ == '__main__':
    run()
