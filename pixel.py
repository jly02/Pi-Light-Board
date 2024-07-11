class Pixel():
    def __init__(self, grb, how_bright):
        self.color = grb
        self.brightness = how_bright

    def brightness(value):
        self.brightness = value

    def __repr__(self):
        return f"({self.grb}, {self.brightness})"
    
        
class PixelArray():
    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        self.pixels = [Pixel() for _ in range(num_pixels)]
        
    def set_pixel(self, index, grb, brightness=1.0):
        if 0 <= index < self.num_pixels:
            self.pixels[index].set_color(grb)
            self.pixels[index].set_brightness(brightness)

    def fill(grb):
        list(map(lambda c: c.color = grb, self.pixels))

    def __repr__(self):
        return ' - '.join(self.pixels)
