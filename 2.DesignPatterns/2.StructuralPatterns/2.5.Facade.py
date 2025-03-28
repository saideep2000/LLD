
# Problem Statement:

# In many applications, a complex subsystem consists of multiple interacting classes 
# (e.g., DVD players, projectors, sound systems, and lighting controls in a home theater) 
# that together provide a range of functionalities. However, most clients of the subsystem 
# need only a few of these features, and they don't want to manage the interactions between 
# 'these various components directly. The problem is to simplify the client’s experience by 
# 'providing a unified, high-level interface that encapsulates and coordinates the subsystem’s complexity. 
# This way, clients can perform complex operations (like "watch movie" or "end movie") 
# without needing to know the underlying details of each component.

# This demonstrates the Facade Design Pattern by encapsulating a home theater subsystem. 
# The HomeTheaterFacade class provides a simplified interface to the complex subsystem that 
# includes a DVD player, projector, sound system, and lights.

# Subsystem classes with their own complex interfaces.

class DVDPlayer:
    def on(self):
        print("DVD Player: turning on")
    def play(self, movie):
        print(f"DVD Player: playing movie '{movie}'")
    def off(self):
        print("DVD Player: turning off")

class Projector:
    def on(self):
        print("Projector: turning on")
    def wide_screen_mode(self):
        print("Projector: setting wide screen mode")
    def off(self):
        print("Projector: turning off")

class SoundSystem:
    def on(self):
        print("Sound System: turning on")
    def set_volume(self, level):
        print(f"Sound System: setting volume to {level}")
    def off(self):
        print("Sound System: turning off")

class Lights:
    def dim(self, level):
        print(f"Lights: dimming to {level}%")

# Facade class that provides a unified interface to the subsystem.
class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system, lights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim(10)  # Dim the lights for a cinematic experience.
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound_system.on()
        self.sound_system.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.lights.dim(100)  # Restore the lights.
        self.projector.off()
        self.sound_system.off()
        self.dvd_player.off()

# Client code demonstrating the use of the Facade.
if __name__ == "__main__":
    # Instantiate subsystem components.
    dvd = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()
    lights = Lights()

    # Create the Facade, passing in the subsystem components.
    home_theater = HomeTheaterFacade(dvd, projector, sound_system, lights)

    # The client uses the simple interface provided by the Facade.
    home_theater.watch_movie("Inception")
    home_theater.end_movie()


# python3 2.DesignPatterns/2.StructuralPatterns/2.5.Facade.py