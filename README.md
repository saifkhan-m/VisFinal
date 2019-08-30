# Elevation extraction of surface using Marching Squares in 2D

Marching squares is a computer graphics algorithm that generates contours for a two-dimensional scalar field.
In this project, we have implemented this algorithm to extract the elevation map of the surface using a grayscale image. The gray levels in the image signify the elevation of that point in the image. Where 0 represents the lowest point and 255 represents the highest point. Other heights are mapped to intermediate gray levels from 0 to 255.

The code is configured to handle different color bins and cell sizes.
### Different Bins
For example, if the number of bins is two, then the algorithm threshold all the heights into two gray levels corresponding to each bin.
### Different Cell Sizes
For example, if the cell size is 1 then the algorithm will consider a grid of 4 pixels and make operations on those 4 pixels. If the cell size is 2 then the algorithm will consider the grid of 16 pixels.

## Observations
The number of color bins is inversely proportional to the speed of the algorithm. Less the number of bins, faster the algorithm.
The number of cell sizes is directly proportional to the speed of the algorithm. More the cell size, the faster the algorithm.

## Running the Code
Install python 3. Add packages numpy, open-cv, matplotlib

    pip install numpy
    pip install opencv-python
    pip install matplotlib
After the initial configuration, download the code as zip and fire up the command prompt. Then follow the instructions on the command line.

    python FinalVis.py
    ############################################################
    ############################################################
    Program to generate Elevation Map. Press CTRL+C to exit
    Enter the size of cells: 1 or 2
    1
    Enter the number of color bins : 2 or 4 or 8 or 16
    16
    You chose the cofiguration as cell=1 and bin=16
    Elevation Map of cellsize | 1 | with | 16 | bins took | 38.1481819152832 | seconds
    Elevation_Map_of_cellsize_1_and_16_bins.png written successfully

## Timing summary obtained using diffrent cellsizes and bins

 - [Elevation Map of cellsize | 1 | with | 2 | bins took | 27.388566493988037 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_1_and_2_bins.png)
 - [Elevation Map of cellsize | 1 | with | 4 | bins took | 30.472742795944214 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_1_and_4_bins.png)
 - [Elevation Map of cellsize | 1 | with | 8 | bins took | 36.58209228515625 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_1_and_8_bins.png)
 - [Elevation Map of cellsize | 1 | with | 16 | bins took | 48.84179353713989 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_1_and_16_bins.png)
 - [Elevation Map of cellsize | 2 | with | 2 | bins took | 13.666781902313232 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_2_and_2_bins.png)
 - [Elevation Map of cellsize | 2 | with | 4 | bins took | 16.837963104248047 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_2_and_4_bins.png)
 - [Elevation Map of cellsize | 2 | with | 8 | bins took | 22.900309801101685 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_2_and_8_bins.png)
 - [Elevation Map of cellsize | 2 | with | 16 | bins took | 35.064005613327026 | seconds](https://github.com/saifkhan-m/VisFinal/blob/master/Elevation_Map_of_cellsize_2_and_16_bins.png)
