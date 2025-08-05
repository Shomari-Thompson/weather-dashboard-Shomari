def set_weather_background(canvas, condition):
    from PIL import Image, ImageTk

    weather_map = {
        "Clear": "Screenshot/sunny.jpg",
        "Clouds": "Screenshot/cloudy.jpg",
        "Rain": "Screenshot/rain.jpg",
        "Drizzle": "Screenshot/rain.jpg",
        "Thunderstorm": "Screenshot/stormy.jpg",
        "Snow": "Screenshot/snowy.jpg",
        "Mist": "Screenshot/cloudy.jpg",
        "Fog": "Screenshot/cloudy.jpg",
        "Haze": "Screenshot/cloudy.jpg",
    }

    image_path = weather_map.get(condition, "Screenshot/cloudy.jpg")

    try:
        bg_img = Image.open(image_path).resize((760, 160))
        bg_photo = ImageTk.PhotoImage(bg_img)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=bg_photo)
        canvas.image = bg_photo
    except Exception as e:
        print(f"[Background Error] {e}")
