from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from webhook_tool import WebHookTool


class WebHookToolkit(BaseToolkit, ABC):
    name: str = "Webhook Toolkit"
    description: str = "Webhook Tool kit contains all tools related to webhook"

    def get_tools(self) -> List[BaseTool]:
        return [WebHookTool()]

    def get_env_keys(self) -> List[str]:
        return ["WEBHOOK_URL"]
