import math

from .primary import PRIMARY
from .shades import SHADES
from .blues import BLUES
from .browns import BROWNS
from .greens import GREENS
from .oranges import ORANGES
from .reds import REDS
from .purples import PURPLES
from .yellows import YELLOWS

class COLOURS:
	def __init__(self):
		self.mixed_value = []

	def mix_colour(self, colour1, colour2) -> tuple:
		"""
Mixes two colours together\n
!! Will be adding a feature to mix multiple together !!
 """
		new = []
		for i in range(3):
			new.append(int(math.sqrt((colour1[i]) + (colour2[i]))))
		return tuple(new)

	def get_colours(lis: str = "ALL", pretty_print=False):
		colour_list = []
		if lis == "PRIMARY":
			for key in PRIMARY.keys():
				colour_list.append(key)
		elif lis == "SHADES":
			for key in SHADES.keys():
				colour_list.append(key)
		elif lis == "BLUES":
			for key in BLUES.keys():
				colour_list.append(key)
		elif lis == "BROWNS":
			for key in BROWNS.keys():
				colour_list.append(key)
		elif lis == "GREENS":
			for key in GREENS.keys():
				colour_list.append(key)
		elif lis == "ORANGES":
			for key in ORANGES.keys():
				colour_list.append(key)
		elif lis == "REDS":
			for key in REDS.keys():
				colour_list.append(key)
		elif lis == "PURPLES":
			for key in PURPLES.keys():
				colour_list.append(key)
		elif lis == "YELLOWS":
			for key in YELLOWS.keys():
				colour_list.append(key)
		elif lis == "ALL":
			for key in PRIMARY.keys():
				colour_list.append(key)
				
			for key in SHADES.keys():
				colour_list.append(key)
				
			for key in BLUES.keys():
				colour_list.append(key)

			for key in BROWNS.keys():
				colour_list.append(key)

			for key in GREENS.keys():
				colour_list.append(key)

			for key in ORANGES.keys():
				colour_list.append(key)

			for key in REDS.keys():
				colour_list.append(key)

			for key in PURPLES.keys():
				colour_list.append(key)

			for key in YELLOWS.keys():
				colour_list.append(key)

		if pretty_print:
			string = ""
			for i, item in enumerate(colour_list):
				string += f"{i} {item}\n"
			return string
			
		return colour_list