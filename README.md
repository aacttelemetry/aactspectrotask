# aactspectrotask
Code used to handle the multi-camera system used to deal with the Spectrographic Analysis task of the NASA HERC.  

**camera.py:** Base code that takes one picture from each camera on execution. Runs once.  
**camera-button-only.py**: Code that waits for button input before taking the four pictures. Runs indefinitely.  
**camera-heartbeat.py**: Code that, in addition to the above, will occasionally print to the shell to let the user know that the script is still running.

