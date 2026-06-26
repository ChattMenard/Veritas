"""Economic evidence schemas for API request/response models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class EconomicIndicatorBase(BaseModel):
    date: datetime
    indicator_type: str
    value: float
    source: str
    region: str = "Canada"
    notes: Optional[str] = None


class EconomicIndicatorCreate(EconomicIndicatorBase):
    pass


class EconomicIndicatorRead(EconomicIndicatorBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class BusinessMetricsBase(BaseModel):
    date: datetime
    business_size: str
    sector: str
    total_sales: float
    total_profits: float
    operating_expenses: float
    employee_count: int
    closure_rate: Optional[float] = None
    source: str
    region: str = "Canada"


class BusinessMetricsCreate(BusinessMetricsBase):
    pass


class BusinessMetricsRead(BusinessMetricsBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class PolicyActionBase(BaseModel):
    date: datetime
    policy_type: str
    policy_name: str
    description: str
    claimed_purpose: str
    actual_impact: str
    affected_groups: str = "all"
    source_url: Optional[str] = None
    source_document: Optional[str] = None


class PolicyActionCreate(PolicyActionBase):
    pass


class PolicyActionRead(PolicyActionBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class HypocrisyTrackerBase(BaseModel):
    date: datetime
    official: str
    statement: str
    statement_date: datetime
    contradictory_action: str
    action_date: datetime
    harm_caused: str
    evidence_urls: str = ""
    verified: bool = False


class HypocrisyTrackerCreate(HypocrisyTrackerBase):
    pass


class HypocrisyTrackerRead(HypocrisyTrackerBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class WealthTransferBase(BaseModel):
    date: datetime
    mechanism: str
    amount: float
    from_group: str
    to_group: str
    method: str
    policy_reference: Optional[str] = None
    evidence_summary: str
    source_urls: str = ""


class WealthTransferCreate(WealthTransferBase):
    pass


class WealthTransferRead(WealthTransferBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
