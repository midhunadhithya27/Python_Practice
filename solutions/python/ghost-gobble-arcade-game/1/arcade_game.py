def eat_ghost(power_pellet,pac_ghost):
    return (power_pellet and pac_ghost)
def score(touch_pellet,touch_dot):
    return (touch_pellet or touch_dot)
def lose(power_pellet_active,touching_ghost):
    return (not(power_pellet_active)and touching_ghost)
def win(eaten_dots,power_pellets,pacman_ghost):
    return eaten_dots and not(lose(power_pellets,pacman_ghost))