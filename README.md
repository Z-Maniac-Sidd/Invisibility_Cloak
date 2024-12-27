# Invisibility Cloak Effect with OpenCV

This project implements a Harry Potter-inspired invisibility cloak effect using OpenCV and Python. By detecting specific color ranges, the program replaces the selected area of the video feed with a static background, creating the illusion of invisibility.

---

## How It Works

1. **Capture Background**:
   - The program first captures the background image by recording a video frame for 30 iterations while the user stays out of the frame.

2. **Detect Specific Colors**:
   - It detects specific colors (e.g., red) from the live video feed by converting the frames to the HSV color space and applying color masks.

3. **Generate Masks**:
   - Two masks are generated to cover a wide range of red hues. These masks are combined and processed to isolate the selected area.

4. **Replace Selected Area**:
   - The detected color area is replaced with the previously captured background, creating the invisibility effect.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- OpenCV
- NumPy

You can install the required libraries using pip:

```bash
pip install opencv-python-headless numpy
```

---

## Usage

1. Clone this repository or copy the Python script.
2. Run the Python script using:

   ```bash
   python invisibility_cloak.py
   ```

3. Stay out of the camera frame for the first 30 frames to allow the program to capture the background.
4. Use a red cloth or any red-colored object to create the invisibility effect.
5. Press `Esc` to exit the program.

---

## Output

The output will display a video feed where the selected red-colored areas appear invisible, seamlessly blending with the background.

---

## Customization

- **Change the Color Range**:
  - To detect a different color, update the `lower_bound1`, `upper_bound1`, `lower_bound2`, and `upper_bound2` arrays with the HSV values of your chosen color.

- **Adjust Morphological Transformations**:
  - Modify the kernel size in `np.ones((7, 7), np.uint8)` to tweak the mask smoothing process.

---

## Demonstration

Below is an example of the invisibility effect:

![Invisibility Effect Example](example.gif)

---

## Known Issues

- The program may not work well under poor lighting conditions.
- Overlapping or similar colors in the frame may reduce accuracy.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as you like.

---

## Acknowledgments

This project was inspired by the magical invisibility cloak from the Harry Potter series and serves as an educational example of OpenCV capabilities.

