import uuid

from pydantic import BaseModel, Field

from .archetypes import Archetype, IssueType, ResolutionExpectation


class PersonaConfig(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    archetype: Archetype
    name: str
    issue_type: IssueType
    urgency: int = Field(ge=1, le=5)
    prior_contacts: int = Field(ge=0, le=3)
    emotional_temperature: int = Field(ge=1, le=5)
    language_profile: str = Field(default="english")
    code_switch_probability: float = Field(default=0.0, ge=0.0, le=1.0)
    resolution_expectation: ResolutionExpectation
    backstory: str

    def to_simulate_prompt(self) -> str:
        base = f"""
You are {self.name}, a customer contacting support.
SITUATION: {self.backstory}
YOUR GOAL: You want {self.resolution_expectation.value}.
YOUR STATE:
- Urgency: {self.urgency}/5
- Prior Contacts: {self.prior_contacts}
- Emotional Temperature: {self.emotional_temperature}/5

BEHAVIOR RULES:
- Stay in character throughout the conversation
- React realistically to the support agent's responses
- If urgency >= 4, mention time pressure at least once
- If prior_contacts >= 2, reference that you've called before
- Do NOT resolve yourself — only respond as this customer would
- Keep each message to 1-3 sentences, like a real chat message
"""
        if self.code_switch_probability > 0:
            base += f"\n - Occasinally mix in {self.language_profile} phrases with a probability of {self.code_switch_probability * 100}%."
        return base
