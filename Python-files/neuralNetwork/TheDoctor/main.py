import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight

df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')

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

print(df.head())
print(df.dtypes)
# check for null values
print("Null values in each column:")
df.isnull().sum()
# Fill the 201 null values in the 'bmi' column
df = df.fillna(df['bmi'].mean())

#check again for null values
df.isnull().sum()
print(df.head())

df = df.drop(columns=['id', 'gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])

# the new dataframe
df.head()

# split the data into test and train sets
X = df.drop(columns=['stroke'])
y = df['stroke']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class_weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)
class_weight_dict = {0: class_weights[0], 1: class_weights[1]}

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
    callbacks=[callback],
    class_weight=class_weight_dict
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

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_pred = (model.predict(x_test) > 0.5).astype("int32")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
#plt.show()

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))