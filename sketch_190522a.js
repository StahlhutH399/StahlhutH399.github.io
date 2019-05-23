int x;
int y; 
int Vx = 4;
int Vy = 2;
int r; 
void setup(){
  size(500, 700);
  x=100;
  y=200;
  r=30;
}
void draw(){
  background(0);
  ellipse(x, y, r, r);
  updatePosition();
  bounce();
  gravity();
}
void gravity(){
  if(Vx > 0){
  Vx *= -1;
  }
  if(Vy > 0){
  Vx *= -1;
  }
}
void bounce(){
  if(x > width - r/2){
  Vx *= -1;
  }
  if(y > height - r/2){
  Vy *= -1;
  }
  if(x < 0 + r/2){
  Vx *= -1;
  }
  if(y < 0 + r/2){
  Vy *= -1;
  }
}
void updatePosition(){
  x += Vx;
  y += Vy;
}
