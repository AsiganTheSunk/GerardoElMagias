from core.units.animations.animation_resource import AnimationResource
from core.units.animations.animation_type import AnimationType


MeleeBanditSet = [
    # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
    AnimationResource(AnimationType.IDLE, 8),
    AnimationResource(AnimationType.DEATH, 10),
    AnimationResource(AnimationType.ATTACK, 8),
    AnimationResource(AnimationType.HURT, 3),
    AnimationResource(AnimationType.BLOCK, 9),
    AnimationResource(AnimationType.MISS, 5)
]

MeleeBossSet = [
    # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
    AnimationResource(AnimationType.IDLE, 8),
    AnimationResource(AnimationType.DEATH, 10),
    AnimationResource(AnimationType.ATTACK, 8),
    AnimationResource(AnimationType.HURT, 3),
    AnimationResource(AnimationType.BLOCK, 9),
    AnimationResource(AnimationType.MISS, 5)
]

HeroSet = [
    # Index 0: Idle, 1: Death, 2: Attack, 3:Hurt, 4:Block, 5: Miss
    AnimationResource(AnimationType.IDLE, 8),
    AnimationResource(AnimationType.DEATH, 10),
    AnimationResource(AnimationType.ATTACK, 8),
    AnimationResource(AnimationType.HURT, 3),
    AnimationResource(AnimationType.BLOCK, 9),
    AnimationResource(AnimationType.MISS, 5)
]
