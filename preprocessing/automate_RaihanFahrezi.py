import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder


RAW_DATA_URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"


def preprocess_telco_churn(input_path="../telco_churn_raw.csv", output_path="telco_churn_preprocessed.csv"):
    """Melakukan preprocessing dataset Telco Customer Churn secara otomatis.

    Tahapan preprocessing dibuat sama dengan tahapan pada notebook eksperimen:
    1. Memuat dataset raw.
    2. Menghapus kolom customerID.
    3. Mengubah TotalCharges menjadi numerik.
    4. Menangani missing value pada TotalCharges dengan median.
    5. Melakukan encoding pada seluruh fitur kategorikal.
    6. Menyimpan dataset hasil preprocessing.
    """
    if os.path.exists(input_path):
        df = pd.read_csv(input_path)
    else:
        print("File raw tidak ditemukan. Dataset akan diunduh dari sumber publik.")
        df = pd.read_csv(RAW_DATA_URL)
        df.to_csv(input_path, index=False)

    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

    encoder = LabelEncoder()
    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:
        df[column] = encoder.fit_transform(df[column].astype(str))

    df.to_csv(output_path, index=False)

    print("Preprocessing selesai.")
    print(f"Dataset hasil preprocessing disimpan ke: {output_path}")
    print(f"Shape dataset hasil preprocessing: {df.shape}")

    return df


if __name__ == "__main__":
    preprocess_telco_churn()
