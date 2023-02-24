import cv2
import pandas as pd

# Read CSV file containing x, y coordinate points
df = pd.read_csv('coor.csv')

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set video width and height
cap.set(3, 640)
cap.set(4, 480)

# Set font and font scale for text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1

# Initialize current point index
current_index = 0

# Loop through video frames
while True:
    # Read video frame
    ret, frame = cap.read()

    # If reading video frame is successful
    if ret:
        # Get the next 20 points from the CSV file
        points = df[current_index:current_index+20]
        
        # Loop through the points and display them on the video stream
        for index, row in points.iterrows():
            x = int(row['x'])
            y = int(row['y'])
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
            cv2.putText(frame, f"({x}, {y})", (x, y), font, font_scale, (0, 0, 255), 2)
        
        # Display the video frame
        cv2.imshow('frame', frame)

        # Check if the 'd' button is pressed
        if cv2.waitKey(1) & 0xFF == ord('d'):
            # Update the current index to display the next 20 points
            current_index += 20
        
        # Check if the 'q' button is pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()

