from squirrel import Squirrel

squirrel = Squirrel()
fur_colors = squirrel.get_fur_list()
squirrel.count_colors(fur_colors)
squirrel.create_report()