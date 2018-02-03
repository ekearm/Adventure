from sys import exit
from random import randint

#locations
class Scene(object):
	def enter(self):
		print "Not done"
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.openingScene()

		while True:
			print "\n-------"
			nextSceneName = current_scene.enter()
			current_scene = self.scene_map.nextScene(nextSceneName)

class gameOver(Scene):
	ending = "You have fallen Game Over."

	def enter(self):
		print ending
		exit(1)

class Intro(Scene):
	def enter (self):
		print "The Necromancer Maraek has threatened the world!\n"
		print "She will raise an army of the undead until nothing remains\n"
		print "All of this has been fortold by an acient prophecy that one hero will defeat her."
		print "Are you that hero?\n\n\n\n"

		print "Please hero select your gender M for male of F for female:"
		gender = raw_input(">")

		while gender != "M" or "F":
			gender = raw_input ("please enter either M or F capital please: ")

		print "Please select your hero:"
		print "Capital F for the fighter: high damage, low magic, low speed, high defense"
		print "Capital T for the theif: medium damage, low magic, high speed, medium defense"
		print "Capital W for wizard: medium damage, high magic, medium speed, low defense"
		print "Capital P for priest: low damage, high magic, medium speed, low defense"
		print "Capital B for Boxer: high damage, low magic, high speed, medium defense"

		hero = raw_input (">>")
		while hero != "F" or "T" or "W" or "P" or "B":
			hero = raw_input("Please select a hero.")


class worldMap (Scene):
	def openingScene():

	def firstArea ():
		print "You start off in a vast region directly behind you lies a castle and city.\n"
		print "In front of you there appears to be an incrossable mountain range\n"
		print "To the left you see a beach and the ship dock and the vast ocean\n"
		print "To the right is a field and forest"

class city()

class castle ()

class dungeon ()

# Fighting characters
class baddy (object):

class player (object):

#NPC's
class merchant()

class innkeeper()

class king ()