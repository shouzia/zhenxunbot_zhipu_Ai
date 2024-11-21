from zhipuai import ZhipuAI
from typing import List

from nonebot import on_message
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me
from nonebot_plugin_alconna import UniMsg
from nonebot_plugin_session import EventSession

from zhenxun.configs.config import BotConfig, Config
from zhenxun.configs.utils import PluginExtraData, RegisterConfig
from zhenxun.models.friend_user import FriendUser
from zhenxun.models.group_member_info import GroupInfoUser
from zhenxun.services.log import logger
from zhenxun.utils.depends import UserName
from zhenxun.utils.message import MessageUtils

from .data_source import get_chat_result, hello, no_result


__plugin_meta__ = PluginMetadata(
    name="智谱清言AI",
    description="智谱清言Ai",
    usage=f"""
    与{BotConfig.self_nickname}普普通通的对话吧！
    """.strip(),
    extra=PluginExtraData(
        author="shouzi",
        version="0.1",
        configs=[
            RegisterConfig(
                module="chatglm_API_KEY",
                key="ChatGLM_KEY",
                value=None,
                help="在 https://open.bigmodel.cn/usercenter/apikeys 登录后获取token",
            ),
        ],
    ).dict(),
)


ai = on_message(rule=to_me(), priority=998)

@ai.handle()
async def handle_message(message: UniMsg, session: EventSession, uname: str = UserName()):
    user_input = str(message.extract_plain_text()).strip()  # 获取并去除消息的首尾空格
    if not user_input:
        return
    # 调用 Google Generative AI 生成内容
    answer = Get_Zhipu_AI(user_input)
    await ai.finish(answer)

def Get_Zhipu_AI(user_input):
    
    client = ZhipuAI(api_key=Config.get_config("chatglm_API_KEY", "ChatGLM_KEY"))  # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4-flash",  # 请填写您要调用的模型名称
        messages=[
            {"role": "system", "content": "你现在是真寻机器人 你需要在我回答的文本内容多加一些日本二次元风格,不要加入表情 你的回答中不要出现你是什么机器人，只能在问你是谁的时候才能回答我是什么机器人"},
            {"role": "user", "content": user_input},

        ],
    )
    return response.choices[0].message.content