from pydantic import BaseModel, ConfigDict, Field

class EffectsBase(BaseModel):
    ful_min:float=Field(...,ge=-30.0, description='등락하한')
    flu_max:float=Field(...,le=30.0, description='등락상한')
    category_name:str=Field(...,max_length=20)
    news_id:int=Field(...)

class EffectsRead(EffectsBase):
    effect_id:int
    
    model_config = ConfigDict(from_attributes=True)