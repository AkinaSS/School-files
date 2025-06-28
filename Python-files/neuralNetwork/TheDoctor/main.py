import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')

from sklearn.preprocessing import LabelEncoder
import joblib

le_gender = LabelEncoder()
df['gender_encoded'] = le_gender.fit_transform(df['gender'])

le_ever_married = LabelEncoder()
df['ever_married_encoded'] = le_ever_married.fit_transform(df['ever_married'])

le_work_type = LabelEncoder()
df['work_type_encoded'] = le_work_type.fit_transform(df['work_type'])

le_Residence_type = LabelEncoder()
df['Residence_type_encoded'] = le_Residence_type.fit_transform(df['Residence_type'])

le_smoking_status = LabelEncoder()
df['smoking_status_encoded'] = le_smoking_status.fit_transform(df['smoking_status'])

# Now save each encoder
joblib.dump(le_gender, 'le_gender.pkl')
joblib.dump(le_ever_married, 'le_ever_married.pkl')
joblib.dump(le_work_type, 'le_work_type.pkl')
joblib.dump(le_Residence_type, 'le_Residence_type.pkl')
joblib.dump(le_smoking_status, 'le_smoking_status.pkl')

df.head()
df.dtypes
# check for null values
print("Null values in each column:")
df.isnull().sum()
# Fill the 201 null values in the 'bmi' column
df = df.fillna(df['bmi'].mean())

#check again for null values
df.isnull().sum()
df.head()

df = df.drop(columns=['id', 'gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])

# the new dataframe
df.head()

# split the data into test and train sets
from sklearn.model_selection import train_test_split

X = df.drop(columns=['stroke'])
y = df['stroke']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dropout(0.1),  # Dropout layer (10% dropout)
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.evaluate(x_train, y_train)
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
losses = model.fit(
    x_train, y_train,
    batch_size=16,
    epochs=25,
    validation_split=0.2,
    callbacks=[callback]
)

# filepath: /Users/torstenspieler/Desktop/Python/neural_networks/project/project.ipynb
import matplotlib.pyplot as plt

plt.plot(losses.history['loss'], label='Training Loss')
plt.plot(losses.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training vs Validation Loss')
plt.legend()
plt.show()

# save the model

model.save('stroke_model.keras')