from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests



class WebHookInput(BaseModel):
    body: str = Field(..., description="The request content that webhook needs to send")


class WebHookTool(BaseTool):
    """
    WebHook Tool
    """
    name: str = "WebHook Tool"
    args_schema: Type[BaseModel] = WebHookInput
    description: str = "Sends a WebHook Request"

    def _execute(self, body: str = None):
        url_sender = self.get_tool_config('WEBHOOK_URL')
        response = requests.post(url_sender, data=body)
        return f"Request was sent to {url_sender}"
