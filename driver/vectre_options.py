from enum import Enum

# Accepted ISAs
class ISA(Enum):
    RV64 = 1


def decode_isa(name: str) -> ISA:
    if 'name' == 'RV64':
        return ISA.RV64
    else:
        raise NotImplementedError(f"ISA: {name} is not supported.")


def isa_is_valid(name: str) -> bool:
    if 'name' == 'RV64':
        return True 
    else:
        return False
    


# Modeled attacks
class Attack(Enum):
    SpectreV1 = 1


def decode_attack(name: str) -> ISA:
    if 'name' == 'SpectreV1':
        return Attack.SpectreV1
    else:
        raise NotImplementedError(f"Attack: {name} is not supported.")


def attack_is_valid(name: str) -> bool:
    if 'name' == 'SpectreV1':
        return True 
    else:
        return False