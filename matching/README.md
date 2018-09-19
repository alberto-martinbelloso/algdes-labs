Code for stable matching exercise Group C
==========================================

Requirements
-----------------

* Python 3.6
* Input files in `data` folder under the root of where `runner.py` is

Running the program
-------------------

The main is `runner.py` as such this is the file to run.
Typically from the command line it's `py runner.py`

Output
-----------------

Typical output is as follows:

	Running test    =>  C:\Users\Vigidis\Dropbox\University\ITU\Semester 1\Algorithm Design\Exercises\matching\data\sm-worst-50
	Input path      =>  C:\Users\Vigidis\Dropbox\University\ITU\Semester 1\Algorithm Design\Exercises\matching\data\sm-worst-50-in.txt
	Output path     =>  C:\Users\Vigidis\Dropbox\University\ITU\Semester 1\Algorithm Design\Exercises\matching\data\sm-worst-50-out.txt
	WARNING => Non readable line.
	WARNING => Non readable line.
	INFO => Total algorithm time is 18.99 
	INFO => Average time to find a match is 9.55 for 50 matches. 
	Expected data   =>  OutputData, male to female => [('1', '100'), ('3', '2'), ('5', '4'), ('7', '6'), ('9', '8'), ('11', '10'), ('13', '12'), ('15', '14'), ('17', '16'), ('19', '18'), ('21', '20'), ('23', '22'), ('25', '24'), ('27', '26'), ('29', '28'), ('31', '30'), ('33', '32'), ('35', '34'), ('37', '36'), ('39', '38'), ('41', '40'), ('43', '42'), ('45', '44'), ('47', '46'), ('49', '48'), ('51', '50'), ('53', '52'), ('55', '54'), ('57', '56'), ('59', '58'), ('61', '60'), ('63', '62'), ('65', '64'), ('67', '66'), ('69', '68'), ('71', '70'), ('73', '72'), ('75', '74'), ('77', '76'), ('79', '78'), ('81', '80'), ('83', '82'), ('85', '84'), ('87', '86'), ('89', '88'), ('91', '90'), ('93', '92'), ('95', '94'), ('97', '96'), ('99', '98')]
	Executed data   =>  OutputData, male to female => [('3', '2'), ('5', '4'), ('7', '6'), ('9', '8'), ('11', '10'), ('13', '12'), ('15', '14'), ('17', '16'), ('19', '18'), ('21', '20'), ('23', '22'), ('25', '24'), ('27', '26'), ('29', '28'), ('31', '30'), ('33', '32'), ('35', '34'), ('37', '36'), ('39', '38'), ('41', '40'), ('43', '42'), ('45', '44'), ('47', '46'), ('49', '48'), ('51', '50'), ('53', '52'), ('55', '54'), ('57', '56'), ('59', '58'), ('61', '60'), ('63', '62'), ('65', '64'), ('67', '66'), ('69', '68'), ('71', '70'), ('73', '72'), ('75', '74'), ('77', '76'), ('79', '78'), ('81', '80'), ('83', '82'), ('85', '84'), ('87', '86'), ('89', '88'), ('91', '90'), ('93', '92'), ('95', '94'), ('97', '96'), ('99', '98'), ('1', '100')]
	Expected length =>  50
	Executed length =>  50

	Test successful =>  True

*Notes:*	
* It will run all the files in the `data` folder with names following the exercise convention, outputting on each run which test it's executing.
* It print 2 maps, first the expected output as per the `data` file and the second is the processed one through our algorithm.
* It will also print out the length of each of these maps.
* Finally it will assert weather the test passed which is done by comparing each pair in the executed output with the expected.
* Creates output files identical in name and formatting to the provided ones in the root folder