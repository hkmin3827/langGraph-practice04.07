from app.core.llm_setup import model
from app.tools.calc_tools import tools

model_with_tools = model.bind_tools(tools)

