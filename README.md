# Generating-data-set
Command line script in Python for generating a primitive data set from sklearn_datasets...  
+ First argument of command line is type of data set:  
  +  0 — two moons data set;  
  +  1 — swiss roll data set;  
  +  else (for example 2) — blobs data set.  
+ Second argument is number of points/objects/instance.  

For blobs dataset you may also to determine number of properties/attributes and number of centrums/clusters/classes. Respectively, that third and fourth arguments.  

## WARNING:   
For using script you must install sklearn package. For OS based on Debian you can install it from terminal:  
```
sudo apt install python3-sklearn
``` 

## Example of usage:
```
git clone https://github.com/KlimentLagrangiewicz/Generating-data-set  
cd Generating-data-set/  
python3 file.py 2 60 5 2  
```
 