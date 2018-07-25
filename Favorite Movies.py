import fresh_tomatoes
import movie

'''
The following 6 instances are of the Movie class from the movie file.
Each one of them represents one of my favorite movies and takes in the
title of the movie,
a description of the plot, a poster image, and a link to the movie trailer
'''
the_prestige = movie.Movie(
    "The Prestige",
    "An illusion gone horribly wrong"
    " pits two 19th-century magicians,"
    " Alfred Borden(Christian Bale)"
    " and Rupert Angier(Hugh Jackman),"
    " against each other in a bitter battle for supremacy."
    "Terrible consequences loom when the pair escalate their feud,"
    " each seeking not just to outwit -- but to destroy -- the other man.",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
    "https://www.youtube.com/watch?v=ijXruSzfGEc"
)

baby_driver = movie.Movie(
    "Baby Driver",
    "Talented getaway driver Baby(Ansel Elgort) relies"
    " on the beat of his personal soundtrack to be the best in the game."
    " After meeting the woman(Lily James) of his dreams,"
    " he sees a chance to ditch his shady lifestyle and make a clean break."
    " Coerced into working for a crime boss(Kevin Spacey),"
    " Baby must face the music as a doomed heist threatens his life,"
    " love and freedom.",
    "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
    "https://www.youtube.com/watch?v=GTkaKeB4BKY"
)

the_fast_and_the_furious = movie.Movie(
    "The Fast and the Furious",
    "Los Angeles police officer Brian O'Connor must decide where"
    " his loyalty really lies when he becomes enamored"
    " with the street racing world he has been sent undercover to destroy.",
    "https://upload.wikimedia.org/wikipedia/en/5/54/Fast_and_the_furious_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ZsJz2TJAPjw"
)

dirty_dancing = movie.Movie(
    "Dirty Dancing",
    "Baby(Jennifer Grey) is one listless summer away from the Peace Corps."
    " Hoping to enjoy her youth while it lasts,"
    " she's disappointed when her summer plans deposit"
    " her at a sleepy resort in the Catskills with her parents."
    " Her luck turns around, however, when the resort's dance instructor,"
    " Johnny(Patrick Swayze), enlists Baby as his new partner,"
    " and the two fall in love. Baby's father forbids"
    " her from seeing Johnny,"
    " but she's determined to help him perform the"
    " last big dance of the summer.",
    "https://upload.wikimedia.org/wikipedia/en/0/00/Dirty_Dancing.jpg",
    "https://www.youtube.com/watch?v=g_ptDXkByuQ"
)

grease = movie.Movie(
    "Grease",
    "Experience the friendships, romances and adventures"
    " of a group of high school kids in the 1950s."
    " Welcome to the singing and dancing world of Grease,"
    " the most successful movie musical of all time."
    " A wholesome exchange student(Olivia Newton-John)"
    " and a leather-clad Danny(John Travolta) have a summer romance,"
    " but will it cross clique lines?",
    "https://upload.wikimedia.org/wikipedia/en/e/e2/Grease_ver2.jpg",
    "https://www.youtube.com/watch?v=XTBtQodOkTU"
)

deadpool = movie.Movie(
    "Deadpool",
    "Wade Wilson(Ryan Reynolds) is a former Special Forces"
    " operative who now works as a mercenary."
    " His world comes crashing down when evil scientist Ajax(Ed Skrein)"
    " tortures, disfigures and transforms him into Deadpool."
    " The rogue experiment leaves Deadpool with accelerated"
    " healing powers and a twisted sense of humor."
    " With help from mutant allies Colossus and"
    " Negasonic Teenage Warhead(Brianna Hildebrand),"
    " Deadpool uses his new skills to hunt down"
    " the man who nearly destroyed his life.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Deadpool_poster.jpg/220px-Deadpool_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=0LmwToJlefE"
)

# creates a list of the movie instances
movies = [the_prestige, baby_driver, the_fast_and_the_furious,
          dirty_dancing, grease, deadpool]

'''
calls a method found in the fresh_tomatoes file which generate an
html page that displays the movie posters,
the names of the movie, and links to the
movie trailers when the poster is clicked on
'''
fresh_tomatoes.open_movies_page(movies)
