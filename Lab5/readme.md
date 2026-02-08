# Lab 5 Mini-Project Submission


### Main Script
- `main_rpi.py`  
  The main Raspberry Pi program that runs the camera and monitoring system.

### Helper Functions
- `helper_functions/__init__.py`  
  Initializes the helper functions package.
- `helper_functions/camera.py`  
  Functions for capturing images and videos using the camera.
- `helper_functions/computer_vision.py`  
  Functions for processing images and detecting movement.
- `helper_functions/sensehat.py`  
  Functions for interfacing with the Sense HAT (LEDs, sensors).

## webstreaming.py
- Starts a web server on the Raspberry Pi.
- Streams live video from the Pi camera to a browser using MJPEG.

### Notes
- Ensure `data/images/` exists before running `main_rpi.py`.


