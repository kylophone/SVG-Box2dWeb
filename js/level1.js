function level1(world) {
	var b2BodyDef = Box2D.Dynamics.b2BodyDef;
	var b2Body = Box2D.Dynamics.b2Body;
	var b2FixtureDef = Box2D.Dynamics.b2FixtureDef;
	var b2Fixture = Box2D.Dynamics.b2Fixture;
	var b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape;
	var b2CircleShape = Box2D.Collision.Shapes.b2CircleShape;
	var b2Vec2 = Box2D.Common.Math.b2Vec2;
	var SCALE = 30;


	//rect1 (rect)
	var bodyDefrect1 = new b2BodyDef;
	var fixDefrect1 = new b2FixtureDef;
	fixDefrect1.density = 0.5;
	fixDefrect1.friction = 0.5;
	fixDefrect1.restitution = 0.2;
	bodyDefrect1.type = b2Body.b2_staticBody;
	fixDefrect1.shape = new b2PolygonShape;
	fixDefrect1.shape.SetAsBox(150.0 / SCALE, 10.0 / SCALE);
	bodyDefrect1.position.Set(150.0 / SCALE, 290.0 / SCALE);
	world.CreateBody(bodyDefrect1).CreateFixture(fixDefrect1);


	//circle1 (circle)
	var bodyDefcircle1 = new b2BodyDef;
	var fixDefcircle1 = new b2FixtureDef;
	fixDefcircle1.density = 0.5;
	fixDefcircle1.friction = 0.5;
	fixDefcircle1.restitution = 0.6;
	bodyDefcircle1.type = b2Body.b2_dynamicBody;
	fixDefcircle1.shape = new b2CircleShape(40 / SCALE);
	bodyDefcircle1.position.Set(50 / SCALE, 50 / SCALE);
	world.CreateBody(bodyDefcircle1).CreateFixture(fixDefcircle1);


	//polygon1 (polygon)
	var bodyDefpolygon1 = new b2BodyDef;
	var fixDefpolygon1 = new b2FixtureDef;
	fixDefpolygon1.density = 0.5;
	fixDefpolygon1.friction = 0.5;
	fixDefpolygon1.restitution = 0.4;
	bodyDefpolygon1.type = b2Body.b2_staticBody;
	fixDefpolygon1.shape = new b2PolygonShape;
	bodyDefpolygon1.position.Set(100 / SCALE, 100 / SCALE);
	fixDefpolygon1.shape.SetAsArray([
		new b2Vec2(0, 0),
		new b2Vec2(50.0 / SCALE, 0.0 / SCALE),
		new b2Vec2(50.0 / SCALE, 50.0 / SCALE),
	], 3);
	world.CreateBody(bodyDefpolygon1).CreateFixture(fixDefpolygon1);


}
