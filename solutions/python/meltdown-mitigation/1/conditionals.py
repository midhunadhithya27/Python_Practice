"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    p = temperature*neutrons_emitted
    if (temperature<800 and neutrons_emitted>500 and p<500000):
        return True
    else:
        return False
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    g_p = (voltage*current)
    per = (g_p/theoretical_max_power)*100
    if per>=80:
        return "green"
    elif per<80 and per>=60:
        return "orange"
    elif per<60 and per>=30:
        return "red"
    else:
        return "black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    c = temperature*neutrons_produced_per_second
    if c<(threshold*0.9):
        return 'LOW'
    elif (threshold*0.9)<=c<=(threshold*1.1):
        return 'NORMAL'
    else:
        return 'DANGER'

    
