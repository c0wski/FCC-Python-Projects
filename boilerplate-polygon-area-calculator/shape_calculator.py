class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal
      
    # Returns a string that represents the shape using lines of "*"
    def get_picture(self):
        pic_length = self.width
        pic_height = self.height
        if pic_length > 50 or pic_height > 50:
            return "Too big for picture."
        row = ''
        for x in range(pic_length):
            row += '*'
        line = row + '\n'
        lines = []
        for y in range(pic_height):
            lines.append(line)
        picture = ''.join(lines)
        return picture

    # returns how many of a second shape fit in this shape
    def get_amount_inside(self, shape):
        amount_inside = int(self.get_area() / shape.get_area())
        return amount_inside

    def __str__(self):
        string = 'Rectangle(width={}, height={})'.format(self.width, self.height)
        return string

# subclass    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_side):
        super().set_height(new_side)
        super().set_width(new_side)
      
    def __str__(self):
        string = 'Square(side={})'.format(self.width)
        return string
      
