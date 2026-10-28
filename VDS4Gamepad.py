import vgamepad
import time

# 创建一个虚拟DS4手柄
gamepad = vgamepad.VDS4Gamepad()

# 定义所有的DS4游戏手柄按键
NONE      = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE
NORTHWEST = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTHWEST
WEST      = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST
SOUTHWEST = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTHWEST
SOUTH     = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH
SOUTHEAST = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTHEAST
EAST      = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST
NORTHEAST = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTHEAST
NORTH     = vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH

LEFT_THUMB     = vgamepad.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT
RIGHT_THUMB    = vgamepad.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT
LEFT_SHOULDER  = vgamepad.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT
RIGHT_SHOULDER = vgamepad.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT

SHARE         = vgamepad.DS4_BUTTONS.DS4_BUTTON_SHARE
OPTIONS       = vgamepad.DS4_BUTTONS.DS4_BUTTON_OPTIONS
TRIGGER_LEFT  = vgamepad.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT
TRIGGER_RIGHT = vgamepad.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT

TRIANGLE = vgamepad.DS4_BUTTONS.DS4_BUTTON_TRIANGLE
CIRCLE   = vgamepad.DS4_BUTTONS.DS4_BUTTON_CIRCLE
CROSS    = vgamepad.DS4_BUTTONS.DS4_BUTTON_CROSS
SQUARE   = vgamepad.DS4_BUTTONS.DS4_BUTTON_SQUARE

PS          = vgamepad.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS
TOUCHPADBTN = vgamepad.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD

def LEFT_TRIGGER(value):
    gamepad.left_trigger(value)
    # 左扳机轴 值为 0 到 255 之间的整数
def RIGHT_TRIGGER(value):
    gamepad.right_trigger(value)
    # 右扳机轴 值为 0 到 255 之间的整数

def LEFT_JOYSTICK(x_value, y_value) :
    # 左摇杆XY轴 值为 0 到 255 之间的整数
    gamepad.left_joystick(x_value, -y_value)
    # DS4手柄摇杆Y轴和XBOX360摇杆Y轴参数是相反的 所以设置成相反参数 -y_value
def RIGHT_JOYSTCIK(x_value, y_value):
    # 右摇杆XY轴 值为 0 到 255 之间的整数
    gamepad.right_joystick(x_value, -y_value)
    # DS4手柄摇杆Y轴和XBOX360摇杆Y轴参数是相反的 所以设置成相反参数 -y_value

def LEFT_TRIGGER_FLOAT(value_float):
    gamepad.left_trigger_float(value_float)
    # 左扳机轴 值为 0.0 到 1.0 之间的浮点值
def RIGHT_TRIGGER_FLOAT(value_float):
    gamepad.right_trigger_float(value_float)
    # 右扳机轴 值为 0.0 到 1.0 之间的浮点值

def LEFT_JOYSTICK_FLOAT(x_value_float, y_value_float):
    # 左摇杆XY轴 值为 -1.0 到 1.0 之间的浮点值
    gamepad.left_joystick_float(x_value_float, -y_value_float)
    # DS4手柄摇杆Y轴和XBOX360摇杆Y轴参数是相反的 所以设置成相反参数 -y_value_float
def RIGHT_JOYSTCIK_FLOAT(x_value, y_value):
    # 右摇杆XY轴 值为 -1.0 到 1.0 之间的浮点值
    gamepad.right_joystick_float(x_value_float, -y_value_float)
    # DS4手柄摇杆Y轴和XBOX360摇杆Y轴参数是相反的 所以设置成相反参数 -y_value_float

def ACCELEROMETER(x_value, y_value, z_value) :
    gamepad.accelerometer(x_value, y_value, z_value)
    # 加速度计 值为 -32768 到 32767 之间的整数
def GYROSCOPE(x_value, y_value, z_value):
    gamepad.gyroscope(x_value, y_value, z_value)
    # 陀螺仪 值为 -32768 到 32767 之间的整数
def TOUCHPAD(finger1, finger2):
    gamepad.touchpad(finger1, finger2)
    # 触摸板 x 值为 0 到 1919 之间, y 值为 0 到 941 之间的整数, (0, 0) 为左上角, (1919, 941) 为右下角

for a in range(10):
    print('连续按下松开交叉圈圈方块三角键')
    for i in range(3):
        gamepad.press_button(TRIANGLE)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(TRIANGLE)
        gamepad.update()
        gamepad.press_button(CIRCLE)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(CIRCLE)
        gamepad.update()
        gamepad.press_button(CROSS)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(CROSS)
        gamepad.update()
        gamepad.press_button(SQUARE)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(SQUARE)
        gamepad.update()
        time.sleep(0.1)
        gamepad.press_special_button(PS) # PS和TOUCHPAD按钮记得用gamepad.press_special_button()
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_special_button(PS) # PS和TOUCHPAD按钮记得用gamepad.release_special_button()
        gamepad.update()
    print('逐渐增大左扳机轴和左摇杆XY轴')
    for i in range(114514):
        LEFT_TRIGGER_FLOAT(i/100000)
        LEFT_JOYSTICK_FLOAT(-i/100000 , i/100000)
        gamepad.update()
        # time.sleep(0.1)
    print("1秒钟后重置虚拟手柄 ")
    time.sleep(1)
    gamepad.reset()#按键扳机摇杆全部重置成初始状态
    gamepad.update()
del gamepad
print("虚拟手柄已销毁")
# 代码段修改自：https://www.bilibili.com/opus/888637598382161922