var choice = prompt(
  "Welcome to Perimeter Calculator. \n Please Enter your Choice. \n1.Perimeter of Rectangle. \n2.Perimeter of Triangle. \n3.Perimeter of Circle. \n4.Perimeter of Parallelogram"
);

if (choice == "1") {
  var l = prompt("Enter the Length");
  var b = prompt("Enter the width");
  var result =(Number(l) + Number(b)) * 2 ;
  alert("The Perimeter is " + result);
}
if (choice == "2") {
  var h = prompt("Enter the height");
  var b = prompt("Enter the base");
  var c = prompt("Enter side c");
  var result = (Number(h) + Number(b) + Number(c)) ;
  alert("The Perimeter is " + result);
}

if (choice == "3") {
  var r = prompt("Enter the radius");
  var result = 3.14 * Number(r) * 2;
  alert("The Perimeter is " + result);
}

if (choice == "4") {
  var h = prompt("Enter the height");
  var cb = prompt("Enter the corresponding base");
  var result = (Number(h) + Number(cb)) * 2;
  alert("The Perimeter is " + result);
  
}

