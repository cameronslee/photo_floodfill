# Photo Flood Fill
## Install Dependencies
OpenCV
```
$ pip install opencv 
```
## Objective
Determine the most prominent color in target image, and replace that color with
a new color using the flood fill algorithm.

## Example
<div style="display: flex flex-direction: row">
    <img src="res/examples/george.jpg" alt="Image 1" width="200" />
    <img src="res/examples/george_out.jpg" alt="Image 1" width="200" />
</div>

As you can see, the background of the example image is replaced with a new color.

However, there are multiple shades of yellow present. I will be looking to address this with a "flood range" or "color tolerance" setting 

## Usage
```
$ python source.py <filename>
```
Output photos are ../res/output


