import secrets
import time 

image_path = [
    "/static/images/apilsin.png",
    "/static/images/bell.png",
    "/static/images/fire.png",
    "/static/images/podkova.png",
    "/static/images/seven.png",
    "/static/images/strawberry.png",
    "/static/images/vishnya.png",
    "/static/images/watermelon.png",
] 

def spin_reels():
    num_one = secrets.choice(range(len(image_path)))
    num_two = secrets.choice(range(len(image_path)))
    num_three = secrets.choice(range(len(image_path)))

    result = [num_one, num_two, num_three]

    if num_one == num_two == num_three:
        message = "ДЖЕКПОТ!"
    if num_one == 4 and num_two == 4 and num_three == 4:
        message = "СУКА ЧЕРТ ВСЕ СЕМЕРКИ!!!"
    else:
        message = "Попробуй еще раз!"
        
    return {
            "reels": result,
            "images": [image_path[result[0]], image_path[result[1]], image_path[result[2]]],
            "message": message,
            "win": num_one == num_two == num_three
        }
