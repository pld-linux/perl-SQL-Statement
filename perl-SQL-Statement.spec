#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SQL
%define		pnam	Statement
Summary:	SQL::Statement - SQL parsing and processing engine
Summary(pl):	SQL::Statement - silnik do przetwarzania i analizy SQL
Name:		perl-SQL-Statement
Version:	1.005
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6299480a95c16ba60e0f69e6a4c0cb9d
Patch0:		%{name}-warning.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules from this package can be used stand-alone to parse SQL
statements or used with DBI and DBD::CSV, DBD::AnyData or other
drivers to create, modify, and query data in many kinds of formats
including XML, CSV, Fixed Length, Excel Spreadsheets and many others.

%description -l pl
Modu³y z tego pakietu mog± byæ u¿ywane samodzielnie do analizy
poleceñ SQL, jak te¿ razem ze sterownikami DBI i DBD::CSV,
DBD::AnyData lub innymi, do tworzenia i modyfikacji danych oraz
do wykonywania zapytañ przy u¿yciu danych w wielu formatach, w³±czaj±c
XML, CSV, dane o sta³ym rozmiarze, arkusze Excela i wiele innych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/SQL/Dialects
%{perl_vendorlib}/SQL/Statement
%{perl_vendorlib}/SQL/*.pm
%{_mandir}/man3/*
