import asyncio
import websockets
import cv2
import base64
import json
import numpy as np
from tracker import Tracker
import streamlit as st

cap = cv2.VideoCapture("08fd33_4.mp4")  # Webcam (or "path/to/video.mp4")
class_names = ["ball","goalkeeper","player","refree"]  # From your data.yaml

# Async function to process video and communicate with WebSocket
async def process_video(websocket, placeholder):
    while cap.isOpened():

            if not st.session_state.get("running", True):
              break
            ret, frame = cap.read()
            if not ret:
                break
            
            # Compress and encode frame to base64
            _, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            img_str = base64.b64encode(buffer).decode("utf-8")
            await websocket.send(img_str)
            
            # Receive detection results
            data = await websocket.recv()
            detections = json.loads(data)
            
            # Draw bounding boxes on the frame
            for det in detections:
                        
                label = class_names[det["label"]]
                box = det["box"]
                x1, y1, x2, y2 = map(int, box)

                # Determine text to display
                track_id = det.get("track_id", None)
                team = det.get("team", None)
                label_text = ""
                color = det.get("team_color", None)

                if label == "player":
                    
                    if team is not None:
                        label_text += f" Team {team}"
                    frame = Tracker.draw_ellipse(frame, box, color,track_id)
                
                elif label == "refree":
                    
                    frame = Tracker.draw_ellipse(frame, box, (0, 255, 255),track_id)

                elif label == "ball":
                    frame = Tracker.draw_traingle(frame, box, (0, 255, 0))

                # Draw the label text above the box
                cv2.putText(
                    frame, label_text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2
                )
            

            
         # Display the frame in Streamlit
            placeholder.image(frame, channels="BGR", caption="Football Detection")
# Main Streamlit app
def main():
    st.title("Football Detection App")

    # Placeholder for video display
    video_placeholder = st.empty()

    # Control buttons
    if "running" not in st.session_state:
        st.session_state.running = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start"):
            st.session_state.running = True
    with col2:
        if st.button("Stop"):
            st.session_state.running = False

    # WebSocket connection and video processing
    async def run_websocket():
        uri = "ws://4.tcp.ngrok.io:14158"  # Replace with your ngrok address
        async with websockets.connect(uri) as websocket:
            await process_video(websocket, video_placeholder)

    if st.session_state.running:
        asyncio.run(run_websocket())

    # Cleanup when app stops
    if not st.session_state.running:
        cap.release()

if __name__ == "__main__":
    main()