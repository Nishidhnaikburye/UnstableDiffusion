# UnstableDiffusion
# Numerical Anslysis of Diffusion using mean valye of temperature at nodes having coincinging Boundary Conditons 


This Python script simulates heat diffusion in a 2D grid and generates an animation of the temperature distribution along with a plot showing the variation of mean temperature over time.
Requirements

    Python 3.x
    Required libraries: numpy, matplotlib, imageio

Install the required libraries using:

bash

pip install numpy matplotlib imageio

Usage

    Clone or download the repository.

    Open a terminal and navigate to the directory containing the script.

    Run the script:

bash

python heat_diffusion_simulation.py

This will generate two outputs:

    temperature_distribution0p01.gif: An animated gif showing the temperature distribution over simulation steps.

    mean_temperature_variation.png: A plot illustrating the variation of mean temperature with time.

Parameters

You can customize the simulation parameters in the script:

    N: Grid resolution.
    D: Diffusion coefficient.
    dt: Time step.
    num_steps: Number of simulation steps.

Feel free to adjust these parameters based on your requirements.
Note

Ensure you have ImageMagick installed to save the animation as a gif. You can install it using:

bash

sudo apt-get install imagemagick  # For Ubuntu

or

bash

brew install imagemagick  # For macOS

Output

After running the script, you will find the animation gif and the mean temperature variation plot saved in the same directory.
