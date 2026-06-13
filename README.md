# Eksperimen_SML_RaihanFahrezi

Repository ini berisi eksperimen awal untuk proyek akhir **Membangun Sistem Machine Learning** menggunakan dataset **Telco Customer Churn**.

## Dataset
Dataset yang digunakan adalah Telco Customer Churn. Dataset ini digunakan untuk memprediksi apakah pelanggan akan berhenti berlangganan layanan telekomunikasi atau tidak.

Target:
- `Churn = Yes` berarti pelanggan berhenti berlangganan.
- `Churn = No` berarti pelanggan tetap berlangganan.

Sumber dataset:
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv

## Struktur Repository

```text
Eksperimen_SML_RaihanFahrezi
├── telco_churn_raw.csv
├── preprocessing
│   ├── Eksperimen_RaihanFahrezi.ipynb
│   ├── automate_RaihanFahrezi.py
│   └── telco_churn_preprocessed.csv
├── requirements.txt
└── README.md
```

## Tahapan Eksperimen

1. Perkenalan dataset
2. Import library
3. Memuat dataset
4. Exploratory Data Analysis (EDA)
5. Data preprocessing
6. Export dataset hasil preprocessing
7. Automasi preprocessing menggunakan file Python

## Cara Menjalankan Notebook

Jalankan seluruh cell pada file berikut:

```text
preprocessing/Eksperimen_RaihanFahrezi.ipynb
```

Notebook akan menghasilkan file:

```text
preprocessing/telco_churn_preprocessed.csv
```

## Cara Menjalankan Automasi Preprocessing

```bash
cd preprocessing
python automate_RaihanFahrezi.py
```

Output:

```text
telco_churn_preprocessed.csv
```
# Eksperimen_SML_RaihanFahrezi
