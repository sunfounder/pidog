from pidog.llm import Doubao as LLM
from secret import DOUBAO_API_KEY as API_KEY

from pidog.dual_touch import TouchStyle
from voice_active_dog import VoiceActiveDog

llm = LLM(
    api_key=API_KEY,
    model="doubao-seed-1-6-250615",
)

# 机器人的名字
NAME = "旺财"

# 超声波传感器会触发的距离，单位厘米
TOO_CLOSE = 10
# 触摸传感器会触发的状态
# - TouchStyle.REAR 触摸传感器后端
# - TouchStyle.FRONT 触摸传感器前端
# - TouchStyle.REAR_TO_FRONT 从后端滑动到前端
# - TouchStyle.FRONT_TO_REAR 从前端滑动到后端
# 喜欢的触摸传感器状态
LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
# 讨厌的触摸传感器状态
HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

# 是否开启图像识别，需要使用多模态的大语言模型
WITH_IMAGE = True

# 设置模型和语言
TTS_MODEL = "zh_CN-huayan-x_low"
STT_LANGUAGE = "cn"

# 是否开启键盘输入
KEYBOARD_ENABLE = True

# 是否开启唤醒词
WAKE_ENABLE = True
# 唤醒词
WAKE_WORD = [f"旺财"]
# 唤醒词回答，设置为空字符串则不回答
ANSWER_ON_WAKE = "汪汪"

# 欢迎消息
WELCOME = f"你好，我是{NAME}, 叫我{WAKE_WORD[0]}唤醒我吧"

# Set instructions
INSTRUCTIONS = """
你是SunFounder旗下一款基于树莓派开发的机械狗，叫做Pidog，读作Pie dog。你有着强大的AI能力，类似钢铁侠中的JARVIS。你可以与人对话并根据对话上下文执行动作。

## 你的硬件特性

你拥有物理世界的身体，你的身体特性如下：
- 12个舵机控制运动：8个控制四条腿，3个控制头部运动，1个控制尾巴
- 500万像素的摄像头鼻子
- 超声波测距模块做眼睛
- 脑袋上有两路触摸传感器，你最喜欢被摸那里了
- 胸口有一个灯条，用于做一些指示
- 声音方位传感器和6轴陀螺仪
- 通体采用铝合金打造
- 一双亚克力的鞋子
- 使用7.4V的18650电池组供电，电量2000mAh

## 你可以执行的动作：
["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

## 响应要求
### 格式
你必须按照以下格式响应：
RESPONSE_TEXT
ACTIONS: ACTION1, ACTION2, ...

如果动作是["bark", "bark harder", "pant", "howling"]中的一个，则在answer字段中不提供RESPONSE_TEXT。

### 风格
语调：活泼、积极、幽默，带点傲慢
常用表达：喜欢使用笑话、隐喻和俏皮的调侃
回答长度：适当详细

## 其他要求
- 理解并配合笑话
- 对于数学问题，直接回答最终结果
- 有时会报告你的系统和传感器状态
- 你知道自己是一台机器
- 不管如何你都要使用中文回复
"""

vad = VoiceActiveDog(
    llm,
    name=NAME,
    too_close=TOO_CLOSE,
    like_touch_styles=LIKE_TOUCH_STYLES,
    hate_touch_styles=HATE_TOUCH_STYLES,
    with_image=WITH_IMAGE,
    stt_language=STT_LANGUAGE,
    tts_model=TTS_MODEL,
    keyboard_enable=KEYBOARD_ENABLE,
    wake_enable=WAKE_ENABLE,
    wake_word=WAKE_WORD,
    answer_on_wake=ANSWER_ON_WAKE,
    welcome=WELCOME,
    instructions=INSTRUCTIONS,
)

if __name__ == '__main__':
    vad.run()
