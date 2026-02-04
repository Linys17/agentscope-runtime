# -*- coding: utf-8 -*-
from typing import Optional

from agentscope_runtime.sandbox.utils import build_image_uri
from agentscope_runtime.sandbox.registry import SandboxRegistry
from agentscope_runtime.sandbox.enums import SandboxType
from agentscope_runtime.sandbox.box.sandbox import Sandbox
from agentscope_runtime.sandbox.constant import TIMEOUT

SANDBOX_TYPE = "custom"

@SandboxRegistry.register(
    build_image_uri("runtime-sandbox-{SANDBOX_TYPE}"),
    sandbox_type=SANDBOX_TYPE,
    security_level="medium",
    timeout=TIMEOUT,
    description="Custom Sandbox",
)
class CustomSandbox(Sandbox):
    def __init__(
        self,
        sandbox_id: Optional[str] = None,
        timeout: int = 3000,
        base_url: Optional[str] = None,
        bearer_token: Optional[str] = None,
        sandbox_type: SandboxType = SANDBOX_TYPE,
        workspace_dir: Optional[str] = None,
    ):
        super().__init__(
            sandbox_id,
            timeout,
            base_url,
            bearer_token,
            sandbox_type,
            workspace_dir,
        )

    def run_ipython_cell(self, code: str):
        """
        Run an IPython cell.

        Args:
            code (str): IPython code to execute.
        """
        return self.call_tool("run_ipython_cell", {"code": code})

    def run_shell_command(self, command: str):
        """
        Run a shell command.

        Args:
            command (str): Shell command to execute.
        """
        return self.call_tool("run_shell_command", {"command": command})

