import pandas as pd
import numpy as np
from scipy.stats import kurtosis

def process_vibration_data():
    try:
        # 1. Data load karna (Relative path use kar rahe hain)
        # '../data/machine_data.csv' ka matlab: ek folder piche jao fir data mein jao
        df = pd.read_csv('data/machine_data.csv') 
        
        print("✅ Data loaded successfully!")

        # 2. Healthy aur Faulty data ko segments mein todna
        # Hum 100-100 points ke tukde karenge taaki AI patterns seekh sake
        segment_size = 100
        features_list = []

        for i in range(0, len(df), segment_size):
            segment = df.iloc[i : i + segment_size]
            if len(segment) < segment_size: break
            
            vib_signal = segment['vibration'].values
            label = segment['label'].iloc[0]

            # Feature Calculation
            features = {
                'rms': np.sqrt(np.mean(vib_signal**2)),
                'kurtosis': kurtosis(vib_signal),
                'peak': np.max(np.abs(vib_signal)),
                'label': 1 if label == 'Faulty' else 0 # AI numbers samajhta hai
            }
            features_list.append(features)

        # 3. New Feature DataFrame banana
        feature_df = pd.DataFrame(features_list)
        feature_df.to_csv('data/processed_features.csv', index=False)
        
        print(f"✅ Feature Engineering Complete! Total segments: {len(feature_df)}")
        print(feature_df.head()) # Pehle 5 rows dikhayega

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    process_vibration_data()