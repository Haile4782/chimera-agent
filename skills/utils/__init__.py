# Skills Utilities Package
"""Shared utilities for agent skills."""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class SkillInput(BaseModel):
    """Standard input contract for all skills."""
    skill_name: str
    parameters: Dict[str, Any]
    context: Optional[Dict[str, Any]] = None
    request_id: str = Field(..., description="Unique request identifier")
    
class SkillOutput(BaseModel):
    """Standard output contract for all skills."""
    success: bool
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    confidence: float = Field(..., ge=0.0, le=1.0)
    processing_time: float
    request_id: str
    
class SkillBase:
    """Base class for all skills."""
    
    def __init__(self, skill_name: str, version: str = "1.0.0"):
        self.skill_name = skill_name
        self.version = version
        
    def validate_input(self, input_data: Dict[str, Any]) -> SkillInput:
        """Validate and parse skill input."""
        return SkillInput(**input_data)
        
    def execute(self, input_data: Dict[str, Any]) -> SkillOutput:
        """Execute the skill - to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement execute method")
        
    def get_metadata(self) -> Dict[str, Any]:
        """Get skill metadata for discovery."""
        return {
            "name": self.skill_name,
            "version": self.version,
            "description": "Base skill class",
            "input_schema": SkillInput.schema(),
            "output_schema": SkillOutput.schema()
        }