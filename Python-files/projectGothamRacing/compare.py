import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def bruteForce(img1path, img2path):

    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    img1 = cv.resize(img1, (600, 600))
    img2 = cv.resize(img2, (600, 600))
    
    # Initiate ORB detector
    orb = cv.ORB_create()
    
    # detect keypoints and descriptors for both images
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    # Bruteforce matcher
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True) #orb uses hamming distance
    
    # perform brute-force matching by comparing descriptors from both images
    matches = bf.match(des1, des2)
    
    # Sort matches by distance (lower distance means better match)
    matches = sorted(matches, key=lambda x:x.distance)
    nMatches = 20
    # Draw the first nMatches matches
    imgMatch = cv.drawMatches(img1, kp1, img2, kp2, matches[:nMatches], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    plt.figure()
    plt.imshow(imgMatch)
    plt.gcf().canvas.manager.set_window_title('Brute Force')
    plt.show()

def knnBruteForce(img1path, img2path):
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    img1 = cv.resize(img1, (600, 600))
    img2 = cv.resize(img2, (600, 600))
    
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
    plt.gcf().canvas.manager.set_window_title('KNN Brute Force')
    plt.show()
    
    
def Flann(img1path, img2path):
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    img1 = cv.resize(img1, (600, 600))
    img2 = cv.resize(img2, (600, 600))

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
    plt.gcf().canvas.manager.set_window_title('Flann')
    plt.show()


def homography(img1path, img2path):
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    
    img1 = cv.resize(img1, (600, 600))
    img2 = cv.resize(img2, (600, 600))
    
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
            
    minGoodMatches = 2
    if len(goodMatches) > minGoodMatches:
        srcPts = np.float32([kp1[m.queryIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
        desPts = np.float32([kp2[m.queryIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
        errorThreshold = 5
        M, mask = cv.findHomography(srcPts, desPts, cv.RANSAC, errorThreshold)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape
        imgBorder = np.float32([[0,0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1,1,2)
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
    plt.gcf().canvas.manager.set_window_title('Homography')
    plt.show()