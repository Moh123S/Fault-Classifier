import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib # Model ko save karne ke liye

def train_model():
    try:
        # 1. Processed data load karna
        df = pd.read_csv('../data/processed_features.csv')
        
        # Features (X) aur Target (y) alag karna
        X = df.drop('label', axis=1) # rms, kurtosis, peak
        y = df['label']              # 0 (Healthy) or 1 (Faulty)

        # 2. Data ko Train aur Test set mein todna (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # 3. Model Build karna (Random Forest)
        print("⚙️ Training the Industrial Classifier...")
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # 4. Accuracy check karna
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        print(f"✅ Training Complete! Accuracy: {acc * 100:.2f}%")
        print("\n--- Classification Report ---")
        print(classification_report(y_test, y_pred))

        # 5. Model ko save karna (Baad mein use karne ke liye)
        joblib.dump(model, '../models/bearing_model.pkl')
        print("💾 Model saved in 'models/bearing_model.pkl'")

    except Exception as e:
        print(f"❌ Error during training: {e}")

if __name__ == "__main__":
    train_model()