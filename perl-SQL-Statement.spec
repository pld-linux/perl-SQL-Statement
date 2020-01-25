#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	SQL
%define		pnam	Statement
Summary:	SQL::Statement - SQL parsing and processing engine
Summary(pl.UTF-8):	SQL::Statement - silnik do przetwarzania i analizy SQL
Name:		perl-SQL-Statement
Version:	1.412
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SQL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa3653325bb627e32021240ff0af3b05
URL:		http://search.cpan.org/dist/SQL-Statement/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Clone >= 0.30
BuildRequires:	perl-Math-Base-Convert
BuildRequires:	perl-Math-Complex >= 1.56
BuildRequires:	perl-Math-BigInt >= 1.88
BuildRequires:	perl-Params-Util >= 1.00
BuildRequires:	perl-Scalar-List-Utils >= 1.0
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Simple >= 0.90
BuildRequires:	perl-Text-Balanced
BuildRequires:	perl-Text-Soundex >= 3.04
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Conflicts:	perl-DBD-AnyData < 0.09
Conflicts:	perl-DBD-CSV < 0.29
Conflicts:	perl-DBI < 1.611
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules from this package can be used stand-alone to parse SQL
statements or used with DBI and DBD::CSV, DBD::AnyData or other
drivers to create, modify, and query data in many kinds of formats
including XML, CSV, Fixed Length, Excel Spreadsheets and many others.

%description -l pl.UTF-8
Moduły z tego pakietu mogą być używane samodzielnie do analizy
poleceń SQL, jak też razem ze sterownikami DBI i DBD::CSV,
DBD::AnyData lub innymi, do tworzenia i modyfikacji danych oraz
do wykonywania zapytań przy użyciu danych w wielu formatach, włączając
XML, CSV, dane o stałym rozmiarze, arkusze Excela i wiele innych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/SQL/Dialects
%{perl_vendorlib}/SQL/Statement
%{perl_vendorlib}/SQL/Eval.pm
%{perl_vendorlib}/SQL/Parser.pm
%{perl_vendorlib}/SQL/Statement.pm
%{_mandir}/man3/SQL::Dialects::*.3pm*
%{_mandir}/man3/SQL::Eval.3pm*
%{_mandir}/man3/SQL::Parser.3pm*
%{_mandir}/man3/SQL::Statement*.3pm*
