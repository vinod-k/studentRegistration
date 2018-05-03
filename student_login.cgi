#!"C:\xampp\perl\bin\perl.exe"
use CGI qw(:standard);
use CGI::Pretty qw(:all);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use DBI;
use DBD::mysql;
use DBI qw(:sql_types);
my $query = new CGI;

my $error;

use CGI qw/:standard/;


print "Content-type: text/html\n\n";
print <<"HEADER";
<!DOCTYPE html>
<html><h1>Student Login</h1>

<form method=POST action="">


<p>Name: <p><INPUT type="text" name="User" size=25 maxlength=25 required></p>
</p>

<p>Password:<p><INPUT TYPE=PASSWORD NAME="mypassword" id = "Password" size = "15" maxlength = "15" tabindex = "1"/ required></p>
</p>


<form name="input" action="success.cgi" method="post">
<p><input type="submit" value="Submit" /><INPUT TYPE="reset" name = "Reset" value = "Reset"></p>

</form>
</html>
HEADER
#logic for submit button functionality :-----------------

my $redirect = 0;
if (param('User') and param('mypassword'))
{
	$usr=ucfirst(lc(param('User')));
	$pwd=ucfirst(lc(param('mypassword')));


	my $dsn      = "dbi:mysql:vk_db:localhost:3306";	
	my $dbh      = DBI->connect($dsn,'root','',
							   { RaiseError => 1 }) or die "unable to connect:$DBI::errstr\n";	
							   
	$sth=$dbh->prepare("Select emailid from student where emailid='$usr'") || die "$DBI::errstr\n";
	$sth->execute() || die "$DBI::errstr\n";
	#$x=$sth->fetchrow();
			
				
	$sth1 = $dbh->prepare("Select password from student where password='$pwd'") or &dbdie;
	$sth1->execute() || die "$DBI::errstr\n";
	#$y=$sth1->fetchrow_array;

	
	
	if ($x=$sth->fetchrow())
	{
		if ($y=$sth1->fetchrow())
		{   
			$redirect = 1;
			#print $cgi->redirect(-url => 'http://localhost/cgi-bin/success.cgi');
			print "Correct Password";
		}
		else
		{
		print "Incorrect Password";
		}
	}
	else
	{
		print "Incorrect Email";
	}
$dbh->disconnect || die "$DBI::errstr\n";
}

if ($redirect){
    print '<meta http-equiv="refresh" content="1;url=http://localhost/cgi-bin/success.cgi/">';
}