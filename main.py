import argparse
import os
from http import HTTPStatus

import dashscope
from dashscope import Generation


SYSTEM_PROMPT = (
    "\u4f60\u662f\u4e00\u540d\u60c5\u611f\u5206\u6790\u5e08\uff0c"
    "\u8bf7\u5224\u65ad\u7528\u6237\u8bc4\u8bba\u662f\u6b63\u5411\u8fd8\u662f\u8d1f\u5411\u3002"
    "\u53ea\u5141\u8bb8\u56de\u590d\u4e00\u4e2a\u8bcd\uff1a"
    "\u6b63\u5411 \u6216 \u8d1f\u5411\u3002"
)

POSITIVE = "\u6b63\u5411"
NEGATIVE = "\u8d1f\u5411"


def normalize_label(text: str) -> str:
    cleaned = text.strip()
    if POSITIVE in cleaned or cleaned == "\u6b63":
        return POSITIVE
    if NEGATIVE in cleaned or cleaned == "\u8d1f":
        return NEGATIVE
    return cleaned


def get_response(review: str, model: str) -> tuple[str, str]:
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "\u672a\u627e\u5230 DASHSCOPE_API_KEY\u3002"
            "\u8bf7\u5148\u5728\u73af\u5883\u53d8\u91cf\u4e2d\u914d\u7f6e\u4f60\u7684 DashScope API Key\u3002"
        )

    dashscope.api_key = api_key

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": review},
    ]

    response = Generation.call(
        model=model,
        messages=messages,
        result_format="message",
    )

    if response.status_code != HTTPStatus.OK:
        raise RuntimeError(
            f"API call failed: status_code={response.status_code}, "
            f"code={response.code}, message={response.message}"
        )

    raw_content = response.output.choices[0].message.content.strip()
    label = normalize_label(raw_content)
    return label, raw_content


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Qwen sentiment analysis starter demo")
    parser.add_argument(
        "--review",
        default="\u8fd9\u6b3e\u97f3\u6548\u7279\u522b\u597d\uff0c\u7ed9\u4f60\u610f\u60f3\u4e0d\u5230\u7684\u97f3\u8d28\u3002",
        help="Review text to classify",
    )
    parser.add_argument(
        "--model",
        default="qwen-plus",
        help="DashScope model name",
    )
    parser.add_argument(
        "--show-raw",
        action="store_true",
        help="Show the model's raw output",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        label, raw_content = get_response(args.review, args.model)
    except Exception as exc:
        print(f"Error: {exc}")
        raise SystemExit(1) from exc

    print(f"\u8bc4\u8bba: {args.review}")
    print(f"\u60c5\u611f\u7ed3\u679c: {label}")
    if args.show_raw:
        print(f"\u539f\u59cb\u8f93\u51fa: {raw_content}")


if __name__ == "__main__":
    main()
