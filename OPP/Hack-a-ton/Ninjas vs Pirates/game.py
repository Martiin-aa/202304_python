from classes.ninja import Ninja
from classes.pirate import Pirate

kakashi = Ninja("Kakashi")

jack_sparrow = Pirate("Jack Sparrow")

kakashi.attack(jack_sparrow).show_stats()
jack_sparrow.attack(kakashi).show_stats()
