import cv2
import numpy as np
import tensorflow as tf

with open("labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

cap = cv2.VideoCapture(0)

print("Model is Running..........Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (width, height))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    input_data = np.expand_dims(img, axis=0).astype(np.uint8)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    predicted_label = labels[np.argmax(output_data)]

    cv2.putText(frame, predicted_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break