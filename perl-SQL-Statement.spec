%include	/usr/lib/rpm/macros.perl
%define	pdir	SQL
%define	pnam	Statement
Summary:	SQL::Statement perl module
Summary(pl):	Modu³ perla SQL::Statement
Name:		perl-SQL-Statement
Version:	1.004
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-warning.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQL::Statement - SQL parsing and processing engine.

%description -l pl
SQL::Statement - mechanizm przetwarzania SQL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_mandir}/man3/*
%{perl_sitelib}/SQL/*.pm
%{perl_sitelib}/SQL/Statement
%{perl_sitelib}/SQL/Dialects/*.pm
