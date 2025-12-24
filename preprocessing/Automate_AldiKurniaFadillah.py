import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Drop ID
    df = df.drop(columns=["student_id"])

    # Remove duplicate
    df = df.drop_duplicates()

    # Handle outlier (IQR)
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Scaling
    scaler = StandardScaler()
    feature_cols = df.columns.drop("exam_score")
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    # Save
    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    input_file = 'student_exam_scores_raw.csv'
    output_file = 'preprocessing/student_score_clean.csv'

    preprocess_data(input_file, output_file)
