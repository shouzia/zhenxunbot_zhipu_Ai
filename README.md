# 智谱清言AI-ZhenXunBot插件

## 安装

1. 克隆仓库到本地
2. 在ZhenXunBot的插件目录下创建一个名为`zhenxun_plugin_zhipu`的文件夹
3. 将仓库中的`__init__.py`文件复制到ZhenXunBot的插件目录下
4. 在bot.py的配置文件中添加插件配置

## 安装依赖

```shell
pip install --upgrade zhipuai
```

## 配置
   第一次启动会在真寻配置目录下的`config.yaml`文件中生成
   ```yaml
        chatglm_API_KEY:
        # 智谱清言AI
        # CHATGLM_KEY: 在 https://open.bigmodel.cn/usercenter/apikeys 登录后获取Key
        CHATGLM_KEY: XXXX
   ```
   修改`CHATGLM_KEY`为你的智谱清言API密钥，`model`为你要使用的模型名称，默认为`glm-4-flash`。

## 使用

在聊天中发送`@机器人 问题`即可使用智谱清言AI回复。

## 注意事项

1. 本插件使用智谱清言AI的API，需要申请API密钥。
2. 本插件使用智谱清言AI的API，可能需要支付费用。