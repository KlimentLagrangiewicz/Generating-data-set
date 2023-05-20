from sklearn.datasets import make_blobs, make_swiss_roll, make_moons
import sys

def getStrMatrix(X):
    res = ""
    for a in X:
        for elem in a:
            res = res + str(f'{elem:.20f}') + " "
        res = res + str("\n")
    return  res

def getStrArray(arr):
    res = ""
    for a in arr:
        res = res + str(f'{a:.0f}') + "\n"        
    return  res


try:
    if (int(len(sys.argv)) < 3):
        print("Not enough parameters...\n")
        sys.exit(1)
    if int(sys.argv[1]) == 0:
        x, y = make_moons(n_samples = int(sys.argv[2]))
        with open('testMoons' + sys.argv[2] + '.txt', 'w') as f:
            f.write(getStrMatrix(x)) 
        with open('idealSplittingMoons' + sys.argv[2] + '.txt', 'w') as f:
            f.write(getStrArray(y))   
    elif int(sys.argv[1]) == 1:
        x, y = make_swiss_roll(n_samples = int(sys.argv[2]))
        with open('testSwissRoll' + sys.argv[2] + '.txt', 'w') as f:
            f.write(getStrMatrix(x))   
    else:
        if (int(len(sys.argv)) > 4):  
            x, y = make_blobs(n_samples = int(sys.argv[2]), centers = int(sys.argv[4]), n_features = int(sys.argv[3]), random_state = 0) 
            with open('testBlobs' + sys.argv[2] + "_" + sys.argv[3] + "_" + sys.argv[4] + '.txt', 'w') as f:
                f.write(getStrMatrix(x)) 
            with open('idealBlobs' + sys.argv[2] + "_" + sys.argv[3] + "_" + sys.argv[4] + '.txt', 'w') as f:
                f.write(getStrArray(y))   
        elif (int(len(sys.argv)) > 3):
            x, y = make_blobs(n_samples = int(sys.argv[2]), centers = 2, n_features = int(sys.argv[3]), random_state = 0) 
            with open('testBlobs' + sys.argv[2] + "_" + sys.argv[3] + "_2" + '.txt', 'w') as f:
                f.write(getStrMatrix(x)) 
            with open('idealBlobs' + sys.argv[2] + "_" + sys.argv[3] + "_2" + '.txt', 'w') as f:
                f.write(getStrArray(y)) 
        else:
            x, y = make_blobs(n_samples = int(sys.argv[2]), centers = 2, n_features = 2, random_state = 0) 
            with open('testBlobs' + sys.argv[2] + "_2_2" + '.txt', 'w') as f:
                f.write(getStrMatrix(x)) 
            with open('idealBlobs' + sys.argv[2] + "_2_2" + '.txt', 'w') as f:
                f.write(getStrArray(y)) 
except:
    print("Something went wrong...") 