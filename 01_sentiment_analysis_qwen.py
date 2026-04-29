import os
from http import HTTPStatus

import dashscope


MODEL_NAME = 'qwen-turbo'


def load_env_file(path='.env'):
    if not os.path.exists(path):
        return

    with open(path, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue

            key, value = line.split('=', 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env_file()
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')


# 封装模型响应函数
def get_response(messages):
    if not dashscope.api_key:
        raise RuntimeError('请先配置 DASHSCOPE_API_KEY 环境变量，或者在项目根目录创建 .env 文件。')

    response = dashscope.Generation.call(
        model=MODEL_NAME,
        messages=messages,
        result_format='message'  # 将输出设置为message形式
    )

    if response.status_code != HTTPStatus.OK:
        raise RuntimeError(f'模型调用失败：{response.code} - {response.message}')

    return response


def main():
    review = '这款音效特别好 给你意想不到的音质。'

    messages = [
        {"role": "system", "content": "你是一名舆情分析师，帮我判断产品口碑的正负向，回复请用一个词语：正向 或者 负向"},
        {"role": "user", "content": review}
    ]

    response = get_response(messages)
    print(response.output.choices[0].message.content)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'运行失败：{error}')
