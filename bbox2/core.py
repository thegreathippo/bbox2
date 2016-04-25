
import operator
import math


class Geo2(object):
	pass


class Point2(Geo2):
	
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def collides(self, geo2):
		return geo2.collides_with_point2(self)

	def touches(self, geo2):
		return geo2.collides_with_point2(self, _touching=True)

	def collides_with_point2(self, point2, _touching=False):
		return _point2_collides_with_point2(self, point2, _touching)

	def collides_with_box2(self, box2, _touching=False):
		return _point2_collides_with_box2(self, box2, _touching)

	def collides_with_circle2(self, circle2, _touching=False):
		return _point2_collides_with_circle2(self, circle2, _touching)

	@property
	def x(self):
		return self._x
	
	@property
	def y(self):
		return self._y

	def __repr__(self):
		return "{0}({1}, {2})".format(
			type(self).__name__, self.x, self.y)


class Box2(Point2):

	def __init__(self, x, y, w, h):
		super().__init__(x, y)
		self._w = w
		self._h = h

	def collides(self, geo2):
		return geo2.collides_with_box2(self)
	
	def touches(self, geo2):
		return geo2.collides_with_box2(self, _touching=True)

	def collides_with_point2(self, point2, _touching=False):
		return _point2_collides_with_box2(point2, self, _touching)

	def collides_with_box2(self, box2, _touching=False):
		return _box2_collides_with_box2(self, box2, _touching)

	def collides_with_circle2(self, circle2, _touching=False):
		return _box2_collides_with_circle2(self, circle2, _touching)

	@property
	def w(self):
		return self._w
	
	@property
	def h(self):
		return self._h

	@property
	def size(self):
		return self._w, self._h

	@property
	def right(self):
		return self.x + self.w
	
	@property
	def bottom(self):
		return self.y + self.h
	
	@property
	def left(self):
		return self.x
	
	@property
	def top(self):
		return self.y

	width, height = w, h

	def __repr__(self):
		return "{0}({1}, {2}, {3}, {4})".format(
			type(self).__name__, self.x, self.y, self.w, self.h)


class Circle2(Point2):
	
	def __init__(self, x, y, radius):
		super().__init__(x, y)
		self._radius = radius

	def collides(self, geo2):
		return geo2.collides_with_circle2(self)
	
	def touches(self, geo2):
		return geo2.collides_with_circle2(self, _touching=True)
	
	def collides_with_point2(self, point2, _touching=False):
		return _point2_collides_with_circle2(point2, self, _touching)

	def collides_with_box2(self, box2, _touching=False):
		return _box2_collides_with_circle2(box2, self, _touching)
	
	def collides_with_circle2(self, circle2, _touching=False):
		return _circle2_collides_with_circle2(self, circle2, _touching)

	@property
	def radius(self):
		return self._radius

	def __repr__(self):
		return "{0}({1}, {2}, radius: {3})".format(
			type(self).__name__, self.x, self.y,
			self.radius)


def _point2_collides_with_point2(p1, p2, touching=False):
	return (p1.x == p2.x and p1.y == p2.y)


def _point2_collides_with_box2(p, b, touching=False):
	if touching:
		op = operator.lt
	else:
		op = operator.le
	return not (op(p.x, b.x) or
				op(b.right, p.x) or
				op(p.x, b.y) or
				op(b.bottom, p.y))


def _point2_collides_with_circle2(p, c, touching=False):
	if touching:
		op = operator.le
	else:
		op = operator.lt
	return (op((p.x - c.x)**2 + (p.y - c.y)**2, c.radius**2))


def _box2_collides_with_box2(b1, b2, touching=False):
	if touching:
		op = operator.le
	else:
		op = operator.lt
	return (op(abs(b1.x - b2.x) * 2, (b1.w + b2.w)) and
			op(abs(b1.y - b2.y) * 2, (b1.h + b2.h)))


def _box2_collides_with_circle2(b, c, touching=False):
	return False


def _circle2_collides_with_circle2(c1, c2, touching=False):
	if touching:
		op = operator.le
	else:
		op = operator.lt
	distance = math.sqrt((c1.x - c2.x) ** 2 + (c1.y + c2.y) ** 2)
	return not op(c1.radius + c2.radius, distance)





p1 = Point2(4, 9)
p2 = Point2(10, 10)
b1 = Box2(0, 0, 10, 10)
b2 = Box2(10, 10, 10, 10)
c1 = Circle2(15, 10, radius=10)
c2 = Circle2(5, 0, radius=3)
print(_circle2_collides_with_circle2(c1, c2))
