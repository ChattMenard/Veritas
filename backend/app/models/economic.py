"""Economic evidence models for tracking wealth transfer and small business destruction."""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, Text


class EconomicIndicator(SQLModel, table=True):
    """Economic indicators tracking wealth gap and business health."""
    
    __tablename__ = "economic_indicators"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(index=True)
    indicator_type: str = Field(index=True)  # "small_business_count", "inflation_rate", "wealth_gap", etc.
    value: float
    source: str
    region: str = Field(default="Canada")
    notes: Optional[str] = Field(default=None, sa_type=Text)


class BusinessMetrics(SQLModel, table=True):
    """Business performance metrics by size and sector."""
    
    __tablename__ = "business_metrics"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(index=True)
    business_size: str = Field(index=True)  # "small", "medium", "large", "corporate"
    sector: str = Field(index=True)
    total_sales: float
    total_profits: float
    operating_expenses: float
    employee_count: int
    closure_rate: Optional[float] = Field(default=None)
    source: str
    region: str = Field(default="Canada")


class PolicyAction(SQLModel, table=True):
    """Government policy actions and their claimed vs actual impacts."""
    
    __tablename__ = "policy_actions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(index=True)
    policy_type: str = Field(index=True)  # "inflation", "tax", "regulation", "emergency"
    policy_name: str
    description: str = Field(sa_type=Text)
    claimed_purpose: str = Field(sa_type=Text)  # What government said it would do
    actual_impact: str = Field(sa_type=Text)   # What it actually did
    affected_groups: str = Field(default="all")  # Who was actually affected
    source_url: Optional[str] = Field(default=None)
    source_document: Optional[str] = Field(default=None)


class HypocrisyTracker(SQLModel, table=True):
    """Track government statements vs. their actions that harm citizens."""
    
    __tablename__ = "hypocrisy_tracker"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(index=True)
    official: str = Field(index=True)  # Who made the statement
    statement: str = Field(sa_type=Text)  # What they said
    statement_date: datetime
    contradictory_action: str = Field(sa_type=Text)  # What they actually did
    action_date: datetime
    harm_caused: str = Field(sa_type=Text)  # How it harmed citizens
    evidence_urls: str = Field(default="")  # Comma-separated URLs
    verified: bool = Field(default=False)


class WealthTransfer(SQLModel, table=True):
    """Document specific mechanisms of wealth transfer from citizens to elite."""
    
    __tablename__ = "wealth_transfer"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(index=True)
    mechanism: str = Field(index=True)  # "inflation_tax", "regulatory_capture", "subsidy", etc.
    amount: float  # Estimated amount transferred
    from_group: str  # Who lost wealth (e.g., "small_businesses", "working_class")
    to_group: str   # Who gained wealth (e.g., "corporations", "government")
    method: str = Field(sa_type=Text)  # How the transfer worked
    policy_reference: Optional[str] = Field(default=None)
    evidence_summary: str = Field(sa_type=Text)
    source_urls: str = Field(default="")
