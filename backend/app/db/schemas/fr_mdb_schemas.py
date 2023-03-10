from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Json

##########################################################################################################################
##########################       TASK SCHEMAS       #######################################################################
##########################################################################################################################
class TaskLogBase(BaseModel):
    oid: Optional[str]
    task_log: Optional[Json]
