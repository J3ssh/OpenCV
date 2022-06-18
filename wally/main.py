import cv2 as cv

puzzle_img = cv.imread('complex.jpg', cv.IMREAD_UNCHANGED) #image to search in
wally_img = cv.imread('cwally.JPG', cv.IMREAD_UNCHANGED) #image to find

result = cv.matchTemplate(puzzle_img, wally_img, cv.TM_CCOEFF_NORMED) # find match
#debug code
#cv.imshow('results', result)
#cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) #get match location

print('Best Match Top Left Postion: %s' % str(max_loc)) # Output location
print('Best Match Confidence: %s' % max_val) # output confidence of the match

threshhold = 0.6
if max_val < threshhold:
        print('Wally not found')

else:
    print('Found Wally')

    # getting wally size
    wally_w = wally_img.shape[1]
    wally_h = wally_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + wally_w, top_left[1] + wally_h)

    cv.rectangle(puzzle_img, top_left, bottom_right,
                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('results', puzzle_img)
    cv.waitKey()
