import cv2


img=cv2.imread("eeeeee/solar-system.jpg")


cv2.putText(
        img,
        "Sun",
        (30,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (0,0,0)

)
cv2.putText(
        img,
        "mercury",
        (130,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)

)
cv2.putText(
        img,
        "venus",
        (230,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)

)
cv2.putText(
        img,
        "earth",
        (330,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)


)
cv2.putText(
        img,
        "moon",
        (330,180),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)


)
cv2.putText(
        img,
        "mars",
        (430,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)

)
cv2.putText(
        img,
        "jupiter",
        (530,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)

)
cv2.putText(
        img,
        "saturn",
        (730,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)

)
cv2.putText(
        img,
        "uranus",
        (1030,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)

)
cv2.putText(
        img,
        "neptune",
        (1130,230),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)

)
cv2.imshow(" solar system image that is infuriatingly not to scale . why ? because i do not know ",img)
cv2.waitKey(-1)
cv2.imwrite ("_solar_system_image_that_is_infuriatingly_not to scale__why__because_i_do_not_know__Now_with_text_.jpg",img)