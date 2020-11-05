class Button:
    def click(self):
        self.x += 1

    def click_count(self):
        return self.x

    def reset(self):
        self.x = 0
