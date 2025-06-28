import numpy as np
import tensorflow as tf
import joblib  # for loading encoders

def predict_user_input(model, label_encoders):
    age = float(input("Age: "))
    hypertension = int(input("Hypertension (0 = No, 1 = Yes): "))
    heart_disease = int(input("Heart Disease (0 = No, 1 = Yes): "))
    avg_glucose_level = float(input("Average Glucose Level: "))
    bmi = float(input("BMI: "))

    gender = input("Gender (Male, Female, Other): ")
    ever_married = input("Ever Married (Yes, No): ")
    work_type = input("Work Type (Private, Self-employed, Govt_job, children, Never_worked): ")
    residence_type = input("Residence Type (Urban, Rural): ")
    smoking_status = input("Smoking Status (formerly smoked, never smoked, smokes, Unknown): ")

    gender_encoded = label_encoders['gender'].transform([gender])[0]
    ever_married_encoded = label_encoders['ever_married'].transform([ever_married])[0]
    work_type_encoded = label_encoders['work_type'].transform([work_type])[0]
    residence_type_encoded = label_encoders['Residence_type'].transform([residence_type])[0]
    smoking_status_encoded = label_encoders['smoking_status'].transform([smoking_status])[0]

    input_data = np.array([[age, hypertension, heart_disease, avg_glucose_level, bmi,
                            gender_encoded, ever_married_encoded, work_type_encoded,
                            residence_type_encoded, smoking_status_encoded]])

    prediction = model.predict(input_data)
    print(f"Predicted stroke risk (probability): {prediction[0][0]:.4f}")
    print("High risk!" if prediction[0][0] > 0.5 else "Low risk.")
    
if __name__ == "__main__":
    # Load your trained model
    model = tf.keras.models.load_model('stroke_model.keras')

    # Load your label encoders (saved with joblib or pickle)
    label_encoders = {
        'gender': joblib.load('le_gender.pkl'),
        'ever_married': joblib.load('le_ever_married.pkl'),
        'work_type': joblib.load('le_work_type.pkl'),
        'Residence_type': joblib.load('le_Residence_type.pkl'),
        'smoking_status': joblib.load('le_smoking_status.pkl')
    }

    predict_user_input(model, label_encoders)