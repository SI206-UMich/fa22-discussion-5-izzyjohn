import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == "a":
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		if(len(self.items) == 0):
			return None
		itemMax = None
		numMax = 0
		for x in self.items:
			if(item.stock > numMax):
				maxNum = item.stock
				itemMax = item
		return itemMax
		pass

		
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		if(len(self.items) == 0):
			return None
		itemMax = None
		numMax = 0
		for x in self.items:
			if(item.price > numMax):
				maxNum = item.price
				itemMax = item
		return itemMax
		pass



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a(self.item1.name), 0, "Testing Beer")
		self.assertEqual(count_a(self.item2.name), 0, "Testing Cider")
		self.assertEqual(count_a(self.item3.name), 1, "Testing Water")
		self.assertEqual(count_a(self.item4.name), 2, "Testing Fanta")
		self.assertEqual(count_a(self.item5.name), 2, "Testing CocaCola")
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouse = Warehouse()

		self.warehouse.add_item(self.item1)
		self.assertEqual(self.warehouse.add_item(self.item1), self.warehouse.items, "Testing item1 addition")

		self.warehouse.add_item(self.item2)
		self.assertEqual(self.warehouse.add_item(self.item2), self.warehouse.items, "Testing item2 addition")

		pass


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.warehouse2 = Warehouse()
		self.warehouse2.add_item(self.item1)
		self.warehouse2.add_item(self.item2)
		self.assertEqual(self.warehouse2.get_max_stock(), self.item2, "Testing Max Stock")

		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.warehouse3 = Warehouse()
		self.assertEqual(self.warehouse3.get_max_price(), None, "Testing max price with empty list")
		self.warehouse.add_item(self.item3)
		self.warehouse.add_item(self.item4)
		self.assertEqual(self.warehouse.get_max_price(), self.item3, "Testing Max price")
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()