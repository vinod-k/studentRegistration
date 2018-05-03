#!"C:\xampp\perl\bin\perl.exe"
print "Content-type: text/html\n\n";
 
use CGI;
$query = new CGI;
print $query->h1('Success');
