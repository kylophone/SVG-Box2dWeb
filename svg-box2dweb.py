from xml.dom import minidom
import sys


def print_circle_list(circle_list):
	for s in circle_list:
		this_cx = s.attributes['cx'].value
		this_cy = s.attributes['cy'].value
		this_r = s.attributes['r'].value
		this_id = s.attributes['id'].value
		thisBodyDef = "bodyDef" + this_id
		thisFixDef = "fixDef" + this_id

		print "\t//" + this_id + " (circle)"
		print "\tvar " + thisBodyDef + " = new b2BodyDef;"
		print "\tvar " + thisFixDef + " = new b2FixtureDef;"
		print "\t" + thisFixDef + ".density = 0.5;"
		print "\t" + thisFixDef + ".friction = 0.5;" 
		print "\t" + thisFixDef + ".restitution = 0.6;"
		print "\t" + thisBodyDef + ".type = b2Body.b2_dynamicBody;"
		print "\t" + thisFixDef + ".shape = new b2CircleShape(" + this_r + " / SCALE);"
		print "\t" + thisBodyDef + ".position.Set(" + this_cx + " / SCALE, " + this_cy + " / SCALE);"
		print "\tworld.CreateBody(" + thisBodyDef + ").CreateFixture(" + thisFixDef + ");"
		print "\n"


def print_rect_list(rect_list):
	for s in rect_list:
		this_x = s.attributes['x'].value
		this_y = s.attributes['y'].value
		this_height = s.attributes['height'].value
		this_width = s.attributes['width'].value
		this_id = s.attributes['id'].value
		this_half_height = str(float(this_height) / 2)
		this_half_width = str(float(this_width) / 2)
		this_cy = str(float(this_y) + (float(this_height) / 2))
		this_cx = str(float(this_x) + (float(this_width) / 2))
		thisBodyDef = "bodyDef" + this_id
		thisFixDef = "fixDef" + this_id

		print "\t//" + this_id + " (rect)"
		print "\tvar " + thisBodyDef + " = new b2BodyDef;"
		print "\tvar " + thisFixDef + " = new b2FixtureDef;"
		print "\t" + thisFixDef + ".density = 0.5;"
		print "\t" + thisFixDef + ".friction = 0.5;"
		print "\t" + thisFixDef + ".restitution = 0.2;"
		print "\t" + thisBodyDef + ".type = b2Body.b2_staticBody;"
		print "\t" + thisFixDef + ".shape = new b2PolygonShape;"
		print "\t" + thisFixDef + ".shape.SetAsBox(" + this_half_width + " / SCALE, " + this_half_height + " / SCALE);"
		print "\t" + thisBodyDef + ".position.Set(" + this_cx + " / SCALE, " + this_cy + " / SCALE);"
		print "\tworld.CreateBody(" + thisBodyDef + ").CreateFixture(" + thisFixDef + ");"
		print "\n"


def print_polygon_list(polygon_list):
	for s in polygon_list:
		this_id = s.attributes['id'].value
		these_points = s.attributes['points'].value.split()
		number_of_verticies = len(these_points)
		origin_x = these_points[0].split(',')[0]
		origin_y = these_points[0].split(',')[1]
		thisBodyDef = "bodyDef" + this_id
		thisFixDef = "fixDef" + this_id

		print "\t//" + this_id + " (polygon)"
		print "\tvar " + thisBodyDef + " = new b2BodyDef;"
		print "\tvar " + thisFixDef + " = new b2FixtureDef;"
		print "\t" + thisFixDef + ".density = 0.5;"
		print "\t" + thisFixDef + ".friction = 0.5;"
		print "\t" + thisFixDef + ".restitution = 0.4;"
		print "\t" + thisBodyDef + ".type = b2Body.b2_staticBody;"
		print "\t" + thisFixDef + ".shape = new b2PolygonShape;"
		print "\t" + thisBodyDef + ".position.Set(" + origin_x  + " / SCALE, " + origin_y + " / SCALE);"
		print "\t" + thisFixDef + ".shape.SetAsArray(["
		print "\t\tnew b2Vec2(0, 0),"

		for this_point in these_points[1:]:
			this_x = str(float(this_point.split(',')[0]) - float(origin_x))
			this_y = str(float(this_point.split(',')[1]) - float(origin_y))
			print "\t\tnew b2Vec2(" + this_x + " / SCALE, " + this_y + " / SCALE),"

		print "\t], " + str(number_of_verticies) + ");"
		print "\tworld.CreateBody(" + thisBodyDef + ").CreateFixture(" + thisFixDef + ");"
		print "\n"	


def print_top():
	print "function level1(world) {"
	print "\tvar b2BodyDef = Box2D.Dynamics.b2BodyDef;"
	print "\tvar b2Body = Box2D.Dynamics.b2Body;"
	print "\tvar b2FixtureDef = Box2D.Dynamics.b2FixtureDef;"
	print "\tvar b2Fixture = Box2D.Dynamics.b2Fixture;"
	print "\tvar b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape;"
	print "\tvar b2CircleShape = Box2D.Collision.Shapes.b2CircleShape;"
	print "\tvar b2Vec2 = Box2D.Common.Math.b2Vec2;"
	print "\tvar SCALE = 30;"
	print "\n"


def print_bottom():
	print "}"


def main():
	svgdoc = minidom.parse(sys.argv[1])
	polygon_list = svgdoc.getElementsByTagName('polygon')
	circle_list = svgdoc.getElementsByTagName('circle')
	rect_list = svgdoc.getElementsByTagName('rect')

	print_top()
	print_rect_list(rect_list)
	print_circle_list(circle_list)
	print_polygon_list(polygon_list)
	print_bottom()


if __name__ == "__main__": 
	main()