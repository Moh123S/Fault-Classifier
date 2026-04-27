## The Engineering Logic
In mechanical systems, a bearing crack produces periodic impacts. These impacts are detected using:

RMS (Root Mean Square): Measures the overall energy of the vibration.

Kurtosis: A statistical measure of "spikiness." High Kurtosis is a gold-standard indicator of structural cracks in bearings.

Peak-to-Peak: Captures the maximum intensity of impacts.

## How to Run
1. Setup Environment
Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
2. Generate and Process Data
Bash

python generate_data.py
python src/preprocess.py
3. Train the AI Model
Bash

python src/train.py
4. Launch Dashboard
Bash

streamlit run app.py
## 📈 Results
The model successfully identifies simulated bearing faults with high precision. By adjusting the Kurtosis and RMS sliders in the dashboard, users can see the real-time transition from a "Healthy" state to an "Alert" state.