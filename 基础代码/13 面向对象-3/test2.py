class Camera:
    def take_photo(self):
        print("拍照")


class PlayGame:
    def paly_games(self):
        print('玩游戏')


class Phone(Camera, PlayGame):
    def calls(self):
        print('打电话')

    def send_message(self):
        print('发短信')


iphone = Phone()


class A:
    def print_attr(self):
        print("这是A类的方法")
class B(A):
    def print_attr(self):
        print("这是B类的方法")

b = B()
b.print_attr()