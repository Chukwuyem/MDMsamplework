/*
 Author: Chukwuyem J Onyibe
 Live project url: soosytwubbles.herokuapp.com
*/


var personalTrends = [];
var worldwideTrends = [];
var myballs = [];

var personalballs = [];
var worldwideballs = [];

var words;

var personalSketch = function(p) {

	var ball = function(p) {
		this.x = Math.random() * p.width;
		this.y = Math.random() * p.height;
		this.diameter = 40;
		this.speed = -1;
	}

	ball.prototype.move = function(){
		
		var movx = Math.round(Math.random() * 1); // decide if it will be += or -=
		if(movx == 1){
			//this.x += ((Math.random() * (this.speed*2)) -this.speed);
			this.x += ((Math.random() * (this.speed*2)) );
			//this.x += random(-this.speed, this.speed);
		}
		else{
			//this.x -= ((Math.random() * (this.speed*2)) -this.speed);
			this.x -= ((Math.random() * (this.speed*2)) );
			//this.x -= random(-this.speed, this.speed);
		}
		//make sure it doesn't leave
		if(this.x >= p.width){
			this.x = p.width;
		}
		else if(this.x <= 0){
			this.x = 0;
		}

		var movy = Math.round(Math.random() * 1); //round(random(0, 1));
		if(movy == 1){
			//this.y += ((Math.random() * (this.speed*2)) -this.speed);
			this.y += ((Math.random() * (this.speed*2)) );
			//this.y += random(-this.speed, this.speed);
		}
		else{
			//this.y -= ((Math.random() * (this.speed*2)) -this.speed);
			this.y -= ((Math.random() * (this.speed*2)) );
			//this.y -= random(-this.speed, this.speed);
		}
		//make sure it doesn't leave
		if(this.y >= p.height){
			this.y = p.height;
		}
		else if(this.y <= 0){
			this.y = 0;
		}
	}

	ball.prototype.display = function(trend_str){
		p.ellipse(this.x, this.y, this.diameter, this.diameter);
		var r = this.diameter/2
		p.rectMode(p.CORNER);
		p.fill(0);
		p.text(trend_str, this.x-r/2, this.y-r/2, this.diameter/2, this.diameter/2);

	}

	p.preload = function(){
		personalTrends = p.loadStrings("personalTrendsData.txt");
		console.log(personalTrends);
	};

	p.setup = function(){
		var div_h = $("#personal-trends").height();
		var div_w = $("#personal-trends").width();

		var persTrendsCnv = p.createCanvas(div_w, div_h);
		persTrendsCnv.parent('personal-trends');
		persTrendsCnv.id('persTrendsCnv');

		for (var i = 0; i < personalTrends.length; i++) {
			ball_obj = new ball(p);
			personalballs.push(ball_obj);
		}

		p.frameRate(15);
	};

	p.draw = function(){
		p.background(192, 192, 192);

		p.fill(255, 255, 255);
		p.strokeWeight(0.25);

		for (var i = 0; i < personalballs.length; i++) {
			p.fill(255, 255, 255);
			personalballs[i].move();
			personalballs[i].display(personalTrends[i].split(" , ")[0]);
		};
	};
};

var worldwideSketch = function(p) {

	var ball = function(p) {
		this.x = Math.random() * p.width;
		this.y = Math.random() * p.height;
		this.diameter = 60;
		this.speed = 2;
	}

	ball.prototype.move = function(){
		
		var movx = Math.round(Math.random() * 1); // decide if it will be += or -=
		if(movx == 1){
			this.x += ((Math.random() * (this.speed*2)) );
			//this.x += random(-this.speed, this.speed);
		}
		else{
			this.x -= ((Math.random() * (this.speed*2)) );
			//this.x -= random(-this.speed, this.speed);
		}
		//make sure it doesn't leave
		if(this.x >= p.width){
			this.x = p.width;
		}
		else if(this.x <= 0){
			this.x = 0;
		}

		var movy = Math.round(Math.random() * 1); //round(random(0, 1));
		if(movy == 1){
			this.y += ((Math.random() * (this.speed*2)) );
			//this.y += random(-this.speed, this.speed);
		}
		else{
			this.y -= ((Math.random() * (this.speed*2)) );
			//this.y -= random(-this.speed, this.speed);
		}
		//make sure it doesn't leave
		if(this.y >= p.height){
			this.y = p.height;
		}
		else if(this.y <= 0){
			this.y = 0;
		}
	}

	ball.prototype.display = function(trend_str){
		p.ellipse(this.x, this.y, this.diameter, this.diameter);
		var r = this.diameter/2
		p.rectMode(p.CORNER);
		p.fill(0);
		p.text(trend_str, this.x-r/2, this.y-r/2, this.diameter/2, this.diameter/2);

	}

	p.preload = function(){
		worldwideTrends = p.loadStrings("worldTrendsData.txt");
		console.log(worldwideTrends);
	};


	p.setup = function(){
		var div_h = $("#worldwide-trends").height();
		var div_w = $("#worldwide-trends").width();

		var worldTrendsCnv = p.createCanvas(div_w, div_h);
		worldTrendsCnv.parent('worldwide-trends');
		worldTrendsCnv.id('worldTrendsCnv');

		for (var i = 0; i < worldwideTrends.length; i++) {
			ball_obj = new ball(p);
			worldwideballs.push(ball_obj);
		}

		p.frameRate(15);
	};

	p.draw = function(){
		p.background(192, 192, 192);

		p.fill(255, 255, 255);
		p.strokeWeight(0.25);

		for (var i = 0; i < worldwideballs.length; i++) {
			p.fill(255, 255, 255);
			worldwideballs[i].move();
			worldwideballs[i].display(worldwideTrends[i]);
		};
	};
};



$(document).ready(function(){
	console.log("We're ready!");

	//var pers_Sketch = new personalSketch(p5);
	//var world_Sketch = new worldwideSketch(p5);
	var my_personal = new p5(personalSketch);
	var my_worldwide = new p5(worldwideSketch);
	//new personalSketch(p5);
	//new p5(worldwideSketch);

	console.log("these are words");
	
	$.get("personalTrendsData.txt", function(data) {
		//console.log(data);
		for (var i = 0; i < data.split("\n").length; i++) {
			//console.log(data.split("\n")[i]);
			$("#personal-list").append("<p>" + data.split("\n")[i].split(" , ")[0] + "</p>");
		};
	});
	
	$.get("worldTrendsData.txt", function(data) {
		//console.log(data);
		for (var i = 0; i < data.split("\n").length; i++) {
			//console.log(data.split("\n")[i]);
			$("#worldwide-list").append("<p>" + data.split("\n")[i] + "</p>");
		};
	});

});