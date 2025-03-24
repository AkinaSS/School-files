# All methods explain
All methods using here involves the calculation of distances between 2 descriptors, which seems like a vectors of pixels
For more information, we used these source to create these methods. You can check them out here:

[OpenCV Python Feature Matching (Algorithm and Code)](https://youtu.be/AsU9Uy5w5mI?si=g1dPLPdEvRnMYrk7)
[OpenCV Python Feature Matching Homography (Algorithm and Code)](https://youtu.be/DKkDVHhJ8_M?si=t0d-ITuXvAeV480N)

## Brute Force
This is the method that compares 2 pictures by checking each vectors one by one and compare their distance
So far this one's match most if not all outlines and features, not even the other advance method can do
```py
def bruteForce():
    root = os.getcwd()
    img1path = os.path.join(root, "data/onePic.jpg")
    img2path = os.path.join(root, "data/secPic.jpg")
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    orb = cv.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True) # Brute Force Matcher
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x:x.distance)
    nMatches = 30
    imgMatch = cv.drawMatches(img1, kp1, img2, kp2, matches[:nMatches], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    plt.figure()
    plt.imshow(imgMatch)
    plt.show()
```

## KNN Brute Force
The same to brute force, but used [K-nearest-neighbor](https://www.ibm.com/think/topics/knn#:~:text=The%20k%2Dnearest%20neighbors%20(KNN)%20algorithm%20is%20a%20non,used%20in%20machine%20learning%20today.) methods
```py
def knnBruteForce():
    root = os.getcwd()
    img1path = os.path.join(root, "data/onePic.jpg")
    img2path = os.path.join(root, "data/secPic.jpg")
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    sift = cv.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    bf = cv.BFMatcher()
    nNeightbors = 2
    matches = bf.knnMatch(des1, des2, k=nNeightbors)
    goodmatches = []
    testratio = 0.75
    for m,n in matches:
        if m.distance < testratio * n.distance:
            goodmatches.append([m])
            
    imgMatch = cv.drawMatchesKnn(img1, kp1, img2, kp2, goodmatches, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    plt.figure()
    plt.imshow(imgMatch)
    plt.show()
```

## FLANN
Short for Fast Library for Approximate Nearest Neighbor, which includes using KD trees and K-means clustering for finding features
```py
def FLANN():
    root = os.getcwd()
    img1path = os.path.join(root, "data/onePic.jpg")
    img2path = os.path.join(root, "data/secPic.jpg")
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    sift = cv.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    FLANN_INDEX_KDTREE = 1
    nKdtrees = 5
    nLeafChecks = 50
    nNeighbors = 2
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=nKdtrees)
    searchParams = dict(checks=nLeafChecks)
    flann = cv.FlannBasedMatcher(indexParams, searchParams)
    matches = flann.knnMatch(des1, des2, k=nNeighbors)
    matchesMask = [[0,0] for i in range(len(matches))]
    testRatio = 0.75
    for i, (m, n) in enumerate(matches):
        if m.distance < testRatio * n.distance:
            matchesMask[i] = [1,0]
    drawParams = dict(matchColor=(0,255,0), singlePointColor=(255,0,0), matchesMask=matchesMask, flags=cv.DrawMatchesFlags_DEFAULT)
    imgMatch = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **drawParams)
    
    plt.figure()
    plt.imshow(imgMatch)
    plt.show()
```

## Homography
The same as FLANN but supposedly removing bad/wrong matches in the same time
This is suppose to be the best and strongest method of all 4, but runs the worst, probably because we use it at the wrong feature, we should have use the transformation I think
```py
def homography():
    root = os.getcwd()
    img1path = os.path.join(root, "data/onePic.jpg")
    img2path = os.path.join(root, "data/secPic.jpg")
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    sift = cv.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    FLANN_INDEX_KDTREE = 1
    nKdtrees = 5
    nLeafChecks = 50
    nNeighbors = 2
    
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=nKdtrees)
    searchParams = dict(checks=nLeafChecks)
    flann = cv.FlannBasedMatcher(indexParams, searchParams)
    matches = flann.knnMatch(des1, des2, k=nNeighbors)
    
    goodMatches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            goodMatches.append(m)
            
    minGoodMatches = 20
    
    if len(goodMatches) > minGoodMatches:
        srcPts = np.float32([kp1[m.queryIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
        desPts = np.float32([kp2[m.queryIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
        errorThreshold = 5
        M, mask = cv.findHomography(srcPts, desPts, cv.RANSAC, errorThreshold)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape
        imgBorder = np.float([[0,0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1,1,2)
        warpedImgBorder = cv.perspectiveTransform(imgBorder, M)
        img2 = cv.polylines(img2, [np.int32(warpedImgBorder)], True, 255, 3, cv.LINE_AA)
    else:
        print("Not enough matches found.")
        matchesMask = None
        
    green = (0, 255, 0)
    drawParams = dict(matchColor=green, singlePointColor=None, matchesMask=matchesMask, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    imgMatch = cv.drawMatches(img1, kp1, img2, kp2, goodMatches, None, **drawParams)
    
    plt.figure()
    plt.imshow(imgMatch, 'gray')
    plt.show()
```