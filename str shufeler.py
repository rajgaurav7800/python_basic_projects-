import random
temp = ""
x = ["Why does a light ray incident on a rectangular glass slab immersed in any medium emerges parallel to itself? Explain using a diagram.",
     "A pencil when dipped in water in a glass tumbler appears to be bent at the interface of air and water. Will the pencil appears to be bent to the same extent, if instead of water we use liquids like, kerosene or turpentine. Support your answer with reason.",
     "Refractive index of diamond with respect to glass is 1.6 and absolute refractive index of glass is 1.5. Find out the absolute refractive index of diamond.",
     "A convex lens of focal length 20 cm can produce a magnified virtual as well as real image. Is this a correct statement? If yes, where shall the object be placed in each case for obtaining these images?",
     "Under what condition in an arrangement of two plane mirrors, incident ray and reflected ray will always be parallel to each other, whatever may be angle of incidence. Show the same with the help of diagram.",
     "Draw ray diagrams showing the image formation by a convex mirror when an object is placed \n\t(a) at infinity \n\t(b) at finite distance from the mirror",
     "The image of a candle flame formed by a lens is obtained on a screen placed on the other side of the lens. If the image is three times the size of the flame and the distance between lens and image is 80 cm, at what distance should the candle be placed from the lens? What is the nature of the image at a distance of 80 cm and the lens?",
     "Define power of a lens. What is its unit? One student uses a lens of focal length 50 cm and another of -50 cm. What is the nature of the lens and its power used by each of them?",
     "Why does a ray of light passing through the centre of curvature of a concave mirror gets reflected along same path after reflection?",
     "What kind of image is formed on a cinema screen?",
     "What do you mean by laterally inverted?",
     "The image formed by a convex mirror is observed to be virtual, erect and extremely diminished than the object, what should be the position of the object?",
     "Which type of spherical mirror has a larger field of view?",
     "If a ray of light is incident on a plane mirror such that it makes an angle of 30 with the mirror, then will be the angle of reflection?",
     "A spherical mirror has focal length -10 cm. What type of mirror is it likely to be?",
     "If the magnification of an image formed by a mirror is positive, what does it mean?",
     "What is the magnification produced by a rear view mirror fitted in vehicles?",
     "Rays from the sun converge at a point 15 cm in front of a concave mirror. Where an object should be placed, so that its image formed is equal to the size of the object?",
     "An object is placed at a distance of 8 cm form a convex mirror of focal length 12 cm. Find the position of the image formed?",
     "if the object distance for a concave mirror is 24 cm and image distance is 12 cm in front of a mirror. Then, find the magnification of the mirror",
     ]
z = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"
     ]
i = 0
while i!=(len(x)):
     y = random.randint(1, len(x))
     if str(x[y-1]) in temp:
          i -= 1
     else:
          if i<9:
               print(f"Q_{i + 1}   {x[y - 1]}")
          else:
               print(f"Q_{i + 1}  {x[y - 1]}")
     i += 1
     temp += str(x[y-1])



